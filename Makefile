DXF_BUILD = ./dxf/build

.PHONY: pcb-cutout


BREAKOUT_SRC := board-edge.dxf

PCBS_TARGETS = $(addprefix $(DXF_BUILD)/breakout/$(DXF_BUILD)/breakout ,$(PCBS_SRC))

PCB_MAIN_SRC := 

LAYOUT_TARGET := $(DXF_BUILD)/main/panel-edge-moved.dxf $(DXF_BUILD)/main/main_binding-moved.dxf $(DXF_BUILD)/main/main-inner-binding-moved.dxf 


pcb-cutout: $(PCBS_TARGETS)
main: $(LAYOUT_TARGET)

$(DXF_BUILD)/breakout/%.dxf: ./dxf/breakout.dxf
	keymake autodxf $< output-layer $(subst $(DXF_BUILD)/breakout $(basename $@)) $@

$(DXF_BUILD)/main/%.dxf: ./dxf/main.dxf
	keymake autodxf $< output-layer $(subst dxf/build/main/,,$(basename $@)) $@

dxf/pcb-ref.dxf:
	keymake layouttool ./layout/oled-80.json place-block-to-placement-ref --output dxf/pcb-ref.dxf

dxf/pcb-layout.dxf:
	keymake layouttool ./layout/oled-80.json output-to-placement-ref --output dxf/pcb-layout.dxf

layout/switch_placement.json: scripts/switch_board.py
	python scripts/switch_board.py

.PHONY: placing_pcb_switch
placing_pcb_switch: layout/switch_placement.json scripts/gen_mfile.py
	python scripts/gen_mfile.py

clean:
	rm -rf $(DXF_BUILD)/*
