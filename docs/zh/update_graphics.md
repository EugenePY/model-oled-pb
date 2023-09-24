# 圖片更新

MolelOLED 支援透過USB MSD(USB Mass Storage Device)來更新內部圖片且支援多個圖片顯示.
更新方法大致如下
1. 選取想要放入的圖片, 將圖片轉換成64x48 pixel

2. 利用QMK cli 將圖片轉換成QPF格式(Quantumn Painter Format). 

3. 將ModelOLED進入**MSD-USB mode**.

4. 打開USB drive將OLED.qpf 刪除後，將欲放入圖片放入，按退出USB 鍵盤將reset 如果順利圖片將會在OLED上顯示。

## 所需預安裝軟體

圖片轉換需要使用到QMK cli, 在cli(command-line interface)操作.
如果出現以下的圖示代表是在terminal/qmk msys視窗下執行。

=== "OSX/Terminal"
    ```
    qmk -V
    ```

=== "Windows/QMK MSYS" 
    ```
    qmk -V
    ```

1. Windows 使用者需安裝[QMK MSYS](https://msys.qmk.fm/)
2. Mac 使用者需安裝[QMK CLI](https://github.com/qmk/qmk_cli)

## 圖片轉換

1. 圖片支持png, gif, 64x48, 利用繪圖編輯軟體將 圖片調整成64x48大小。
2. 使用<a href="oled-util">oled-util</a> cli將image 轉換成64x48大小。

## 轉換成 QMK QPF

### QMK Quantumn Painter 指令

1. Upload PNG or GIF file that you want to upload to the keyboard 
2. Keymake will proccess the file into 64x48. 
3. press __ESC__ and __Left Shift__ wait for the browser detech the USB-MSC, then press upload.
4. When the upload is finished the keyboard will reset automatically.


3. When the upload is finished the keyboard will reset automatically, and USB-MSC 
will be disconnected. the new image will be shown on the oled screen.

### Mac使用者 OSX Platform
由於Mac USB driver 的設計，他會額外多創建資料夾(.Trash, .DStore)等等，為了排除此問題，進入**USB-MSD mode**會需要使用```rsync```指令，

```bash
rsync {path/of/your/file.qpf} {path/of/mounted/usbpath}
```

### USB-MSD VFS Impletation Notes

```note 
鍵盤使用STM32F411 MCU使用sector 5, 6, 7當作 圖片使用的空間，
目前**Model OLED**從sector 5的第一個address 開始讀Quantum Painter Format檔, 然後依照header的檔案大小讀下一個檔案，而每次進入USB-MSD的檔案為
128k *3 就是mcu sector 5, 6, 7的flash memory 內容，如果第一個header 的8個byte不是為 0x00FF 0x1200 0x0051 0x4746, 會是錯誤。鍵盤會讀回default image.
```


