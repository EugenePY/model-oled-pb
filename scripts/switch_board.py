"""
generate switch boarder
"""

from core.dxf.parser import read_kle
import os
import json
from core.dxf.geo import Box
import ezdxf
from ezdxf.entities import factory
import numpy as np
from shapely.geometry import box
from ezdxf.addons import geo
from core import LIB_PATH
import json

layout_json = "./layout/oled-80.json"
U = 19.05
with open(layout_json, "r") as f:
    data = json.load(f)
    source = data.pop("LAYOUT", None)
    root_dir = data.pop("ROOT", os.path.dirname(layout_json))
    layout = read_kle(f"{root_dir}/{source}")

ROWS = data["MATRIX_ROW_PINS"]
COLS = data["MATRIX_COL_PINS"]


def running_min(x, p):
    if p is None:
        return x
    return min(p, x)


def running_max(x, p):
    if p is None:
        return x
    return max(p, x)


doc = ezdxf.new()
#doc = ezdxf.readfile("dxf/main.dxf")
msp = doc.modelspace()

datas = []
m_w = None
flag = doc.blocks.new(name="MX")

template = ezdxf.readfile(f"{LIB_PATH}/mx_switch.dxf")
for entity in template.entities:
    flag.add_foreign_entity(entity)

switch_placement = []

shift_y = 0
pad_x = 12  # padding the x of the switchboard
pad_y = (16.6 - 19.05) / 2
## shift to the right
delta_x = 24.05 - U - 0.25 * U
shift_keys = {
    "PrtSc1": delta_x,
    "SL1": delta_x,
    "PB1": delta_x,
    "Insert1": delta_x,
    "Home1": delta_x,
    "PgUp1": delta_x,
    "Delete1": delta_x,
    "End1": delta_x,
    "PgDn1": delta_x,
    "Up1": delta_x,
    "Left1": delta_x,
    "Down1": delta_x,
    "Right1": delta_x
}

doc.layers.add(name=f"edge", color=7)

for i in range(len(ROWS)):
    row = layout[i]
    min_x = None
    min_y = None
    max_x = None
    max_y = None

    row_plc = []
    for j in range(len(row)):
        (x, y, k) = row[j]

        shift_key = shift_keys.get(k.keymap.upper_left, None)
        if shift_key is not None:
            shift_x = shift_key
        else:
            shift_x = 0

        x = x * U + shift_x
        y = y * U

        new_x = x + k.w * U
        row_plc.append((x, -(y - shift_y * i), k))
        min_x = running_min(x, min_x)
        min_y = running_min(y, min_y)
        max_x = running_max(new_x, max_x)
        max_y = running_max(y - U, max_y)

    a = (min_x - pad_x, min_y + pad_y - shift_y * i)
    b = (max_x + pad_x, max_y - pad_y - shift_y * i)
    m_w = running_max(max_x + pad_x, m_w)
    switch_placement.append(row_plc)
    datas.append((a, b))

# switch placement
s_placement = []
offset = np.array([-9.5250, -9.5250]).astype(np.float32)
for row in switch_placement:
    r = []
    i = 0
    for (x, y, k) in row:
        c = k.center(x, y, 19.05)
        offseted_c = np.round(c + offset, 5)
        r.append(tuple(offseted_c.tolist()))
        msp.add_blockref("MX", (c[0], -c[1]))
    s_placement.append(r)

delta_y = [
    switch_placement[i][0][1] - switch_placement[i - 1][0][1]
    for i in range(1, len(switch_placement))
]

conn_placement = [[np.array([-15.4750, 3.4]), np.array([344.325, 3.4])]]

for dy in delta_y:
    l = conn_placement[-1][0] + (0, dy -2*3.4)
    r = conn_placement[-1][1] + (0, dy -2*3.4)
    conn_placement.append([l, r])

    nl = l + (0, 2*3.4)
    nr = r + (0,  2*3.4)
    conn_placement.append([nl, nr])
conn_placement.pop()

# board placement
for i, (a, b) in enumerate(datas):
    bound = box(*a, m_w, b[1]).boundary
    entity_data = geo.dxf_entities(bound)
    for entity in entity_data:
        entity.update_dxf_attribs({"layer": f"edge"})
        msp.add_entity(entity)

doc.saveas("dxf/sw_ref.dxf")

with open("./layout/switch_placement.json", "w") as f:
    json.dump(s_placement, f)

mouse_bite_locations = []
for i in range(8, 43+1):
    _id = f"H{i}"
    ...

with open("./layout/mouse_bite_placement.json", "w") as f:
    json.dump(mouse_bite_locations, f)


with open("./layout/conn_placement.json", "w") as f:
    json.dump([[np.round(i[0], 5).tolist(), np.round(i[1], 5).tolist()] for i in conn_placement], f)
