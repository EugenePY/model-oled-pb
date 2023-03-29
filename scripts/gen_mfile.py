from core.kicad_parser import KicadPCB
#import sys
from core.dxf.parser import read_kle
from logging import getLogger
import json
import numpy as np

logger = getLogger(__name__)

layout = read_kle("./layout/oled-80.kle")
with open("./layout/switch_placement.json", "r") as f:
    switch_placement = json.load(f)
D_start = 1
data = {}
q = D_start
for i, row in enumerate(switch_placement):
    for j, c in enumerate(row):
        # Kicad using reverse y corodinate.
        k = layout[i][j][2]
        # led
        # switch
        c = np.array(c)
        data[k.keymap.upper_left] = c.tolist()
        #print(f"id={qid}, at={local_}")

        # diode
        # as target:
        #qid = f"D{q}"
        #local_ = c + (8.5, 0)
        #data[qid] = local_.tolist()
        q += 1
connectors_id = [["1", "3"], ["2", "4"], ["5", "7"], ["6", "8"], ["9", "11"],
                 ["10", "12"], ["15", "13"], ["18", "14"], ["21", "19"],
                 ["22", "20"]]

with open("./layout/conn_placement.json", "r") as f:
    conn_placement = json.load(f)

for i, _id in enumerate(connectors_id):
    a, b = conn_placement[i]
    data["J" + _id[0]] = a
    data["J" + _id[1]] = b

# controller board connector
controller_board_ref = [285.0639, -23.5250]
switch_coon_relative_placement = [0, -7]
shift_x = 4.4575

data["J16"] = [
    controller_board_ref[0] + switch_coon_relative_placement[0] + shift_x,
    controller_board_ref[1] - switch_coon_relative_placement[1]
]
data["O2"] = [333.3075, -24.1250]

# swithc board connector
data["J17"] = [
    controller_board_ref[0] + switch_coon_relative_placement[0], 62.8625
]
# JST
data["J23"] = [231.9471, -23.5250]
# mouse bite

locations = []
for i in range(8, 43+1):
    _id = f"H{i}"
    ...
pcb = KicadPCB.load('./kicad/main/main.kicad_pcb')
#logger.info('root values: ')
#for k in pcb:
#    logger.info('\t{}: {}'.format(k, pcb[k]))
i = 0
for fp in pcb["footprint"]:
    name = fp[0].split(":")[0][1:]
    ref_id = fp["fp_text"][0][1].replace('"', "")
    target_loc = data.get(ref_id, None)
    if target_loc is not None:
        logger.debug(f"{ref_id}, {target_loc}")
        i += 1
        fp["at"] = target_loc

#print(type(pcb.segment[0]._value["start"]._value))#._append(
#    Sexp(key="segment")
#    )
#pcb.segment._append(Sexp(key="segment"))
#pcb.segment[-1]._value.add(Sexp(key="start", value=[0, 0]))
#pcb.segment[-1]._value.add(Sexp(key="end", value=[1, 1]))
#pcb.segment[-1]._value.add(Sexp(key="width", value=0.25))
#pcb.segment[-1]._value.add(Sexp(key="layer", value="B.Cu"))
#pcb.segment[-1]._value.add(Sexp(key="net", value=37))

pcb.export("./kicad/main/main.kicad_pcb")
