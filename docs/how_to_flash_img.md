# Firmware Flashing

## Flash Main Firmware
1. Flashing Throught DFU or QMK Toolbox 

## Image Format OLED.IMG
the format of the OLED.IMG is 565RGB, and for a 64x48 image is 64 x 48 x 2 bytes.
IMG size RGB 64 x 48  
more detail please refer to `img_format.md`.

### Keymake
Keymake is a web application designed to upload and edit image to __Model OLED__.
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
will be disconnected, eject the USB-MSC, or replug the keyboard into the computer, 
the new image will be shown on the oled screen.

### OSX Platform


