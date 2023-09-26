# 圖片更新

**MolelOLED** 支援透過**USB MSD**(USB Mass Storage Device)來更新內部圖片且支援多個圖片顯示.
更新方法大致如下

1. 選取想要放入的圖片, **將圖片轉換成64x48 pixel**

2. 利用**QMK** cli 將圖片轉換成QPF格式(Quantumn Painter Format). 

3. 將ModelOLED進入**MSD-USB mode**.

4. 打開USB drive將OLED.qpf 刪除後，將欲放入圖片放入，**按退出USB**，鍵盤將reset 如果順利圖片將會在OLED上顯示。

## 所需預安裝軟體

目前圖片轉換有兩種工具是透**QMK CLI**, 另外是[oled-utils](oled_util_guide.md)請選擇一個安裝

**QMK CLI**需自行將圖片裁切成**64x48**, **OLED-UTILS**則由提供自動化的工具。

### QMK CLI
1. Windows 使用者需安裝[QMK MSYS](https://msys.qmk.fm/)
2. Mac 使用者需安裝[QMK CLI](https://github.com/qmk/qmk_cli)

圖片轉換需要使用到**QMK** cli, 在cli(command-line interface)操作.
如果出現以下的圖示代表是在terminal/qmk msys視窗下執行。

=== "OSX/Terminal"
    ```
    qmk setup
    ```

=== "Windows/QMK MSYS" 
    ```
    qmk setup
    ```

如果安裝正確，應該會出現以下的output

```output
Ψ Found qmk_firmware at /Users/bigtreehouse/model_routine/keyboard/qmk_firmware.
Ψ QMK Doctor is checking your environment.
Ψ CLI version: 1.1.2
Ψ QMK home: /Users/bigtreehouse/model_routine/keyboard/qmk_firmware
Ψ Detected macOS 11.7.8 (Intel).
⚠ QMK home does not appear to be a Git repository! (no .git folder)
Ψ CLI installed in virtualenv.
Ψ All dependencies are installed.
Ψ Found arm-none-eabi-gcc version 10.2.1
Ψ Found avr-gcc version 8.4.0
Ψ Found avrdude version 7.0
Ψ Found dfu-programmer version 1.0.0
Ψ Found dfu-util version 0.11
Ψ Submodules are up to date.
Ψ Submodule status:
Ψ - lib/chibios: 2023-04-15 13:48:04 +0000 --  (11edb1610)
Ψ - lib/chibios-contrib: 2023-01-11 16:42:27 +0100 --  (a224be15)
Ψ - lib/googletest: 2021-06-11 06:37:43 -0700 --  (e2239ee6)
Ψ - lib/lufa: 2022-08-26 12:09:55 +1000 --  (549b97320)
Ψ - lib/vusb: 2022-06-13 09:18:17 +1000 --  (819dbc1)
Ψ - lib/printf: 2022-06-29 23:59:58 +0300 --  (c2e3b4e)
Ψ - lib/pico-sdk: 2023-02-12 20:19:37 +0100 --  (a3398d8)
Ψ - lib/lvgl: 2022-04-11 04:44:53 -0600 --  (e19410f)
Ψ QMK is ready to go, but minor problems were found
```

### OLED-UTILS

1. 如果使用[oled-utils](oled_util_guide.md)請參考安裝過程。

## 圖片轉換

轉換圖片有兩種方法

1. 圖片支持png, gif, 64x48, 利用繪圖編輯軟體將 圖片調整成64x48大小。
2. 使用[oled-utils](oled_util_guide.md)cli將image 轉換成64x48大小(安裝使用請參考[oled-util](oled_util_guide.md))。

=== "OSX/Terminal"
    ```
    oled-utils.osx {path/欲轉換得檔案.gif/.png} graphic-resize-format
    ```

=== "Windows/QMK MSYS" 
    ```
    oled-utils.win {path/欲轉換得檔案.gif/.png} graphic-resize-format
    ```


## 轉換成 **QMK QGF**

1. 使用QMK Cli
2. 使用**oled-utils**

### QMK Quantumn Painter 指令

=== "OSX/Terminal"
    ```
    qmk painter-convert-graphics -f rgb565 -i {path/欲轉換得檔案.gif/.png} -o {檔案輸出之path}
    ```

=== "Windows/QMK MSYS" 
    ```
    qmk painter-convert-graphics -f rgb565 -i {path/欲轉換得檔案.gif/.png} -o {檔案輸出之path}
    ```

### OLED-UTILS

如果使用OLED-UTILS使用方式如下

=== "OSX/Terminal"
    ```
    oled-utils.osx {path/欲轉換得檔案.gif/.png} graphic2qgf
    ```

=== "Windows/QMK MSYS" 
    ```
    oled-utils.win {path/欲轉換得檔案.gif/.png} graphic2qgf
    ```



## 將圖片上傳至**ModelOLED**

將**Model OLDE** 進入 USB-MSD mode

1. **Left Ctrl** + **Left ALT** + **ESC**
2. 按有定義**IMG_FLASH**的按鍵預設是OLED-switch。

此時電腦應會偵測到名叫MODEL-OLED的**USB MSD**.

### Windows User

打開USB drive將OLED.qpf 刪除後，將欲放入圖片放入，**按退出USB**，鍵盤將reset 如果順利圖片將會在OLED上顯示。

### Mac使用者 OSX Platform
由於Mac USB driver 的設計，他會額外多創建資料夾(.Trash, .DStore)等等，為了排除此問題，進入**USB-MSD mode**會需要使用```rsync```指令，


=== "OSX/Terminal"
    ```
    rsync {path/of/your/file.qpf} {path/of/mounted/usbpath}
    ```

舉例在我的系統我執行

=== "OSX/Terminal"
    ```
    rsync ./keyboards/ekow/model_oled/img/oyishi.qgf /Volumes/MODEL\ OLED
    ```

### **USB-MSD** VFS Impletation Notes

```note 
鍵盤使用STM32F411 MCU使用sector 5, 6, 7當作 圖片使用的空間，
目前**Model OLED**從sector 5的第一個address 開始讀Quantum Painter Format檔, 然後依照header的檔案大小讀下一個檔案，而每次進入USB-MSD的檔案為
128k *3 就是mcu sector 5, 6, 7的flash memory 內容，如果第一個header 的8個byte不是為 0x00FF 0x1200 0x0051 0x4746, 會是錯誤。鍵盤會讀回default image.
```


