# Graphic Update

MolelOLED support update the internal Graphics using USB Mass Storage Device(USB-MSD),
Hold Left Shift Control and press ESC the image will go in __Graphic Update Mode__, which is a USB Drive (USB-MSD), but the keyboard function will be disable.


## Pre-requirements
1. For Windows User install [QMK MSYS](https://msys.qmk.fm/)
2. For Mac User install [QMK CLI](https://github.com/qmk/qmk_cli)


### QMK Quantumn Painter CLI

1. Upload PNG or GIF file that you want to upload to the keyboard 
2. Keymake will proccess the file into 64x48. 
3. press __ESC__ and __Left Shift__ wait for the browser detech the USB-MSC, then press upload.
4. When the upload is finished the keyboard will reset automatically.


### USB-MSC

1. Long press ESC and Left Shift, wait for computer to detech the USB-MSC device.
2. Deleted the default file OLED.IMG, then drag the new image to the device.

```note 
the keyboard is simulated as a USB-MSD the keyboard itself do not have a actual 
file system, so the file you download from ModelOLED is the flash memory block, 
not the actual image file that normaly you expected from getting from a USB thumb 
drive, the keyboard canonot really serve as a real usb thrumb drive.
```

3. When the upload is finished the keyboard will reset automatically, and USB-MSC 
will be disconnected. the new image will be shown on the oled screen.

### OSX Platform

```bash
rsync ./keyboards/ekow/model_oled/img/oyishi.qgf /Volumes/MODEL\ OLED
```
