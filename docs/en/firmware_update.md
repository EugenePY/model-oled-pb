# Flash Main Firmware

## Pre-requirements
1. Flashing Throught [DFU](https://dfu-util.sourceforge.net/) or [QMK Toolbox](
https://github.com/qmk/qmk_toolbox)

## DFU Mode

__DFU mode__ stands for direct firmware update mode of the keyboard. It a bootloader 
that program the device's flash memory. If we want to program the device we need our keyboard to get into this mode. For __Model OLED__ please follow the following steps to let the keyboard get into the __DFU mode__. 

1. Open __QMK Toolbox__.

2. Long press the button at the back of the controller board, then the QMK Toolbox will show stm32-dfu device.
