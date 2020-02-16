# ras_py_ThermosensorDisplay
Temperature measurement by thermosensor on the raspberry pie
---
* サーモセンサー  
  * AMG8833(Grid-EYE)からデータ取得  


## HOW TO USE
### 接続
AMG8833(3.3V) ⇔ GPIO1(3.3V) 
AMG8833(GND) ⇔ GPIO6(Ground)  
AMG8833(SDA) ⇔ GPIO3(SDA)  
AMG8833(SCL) ⇔ GPIO5(SCL)  

### インストール
1. CircuitPython
```
sudo pip3 install adafruit-circuitpython-amg88xx
```

### I2C 有効化
```
sudo raspi-config
-> 5 Interfacing Options
--> P5 I2C
```
接続確認
```
i2cdetect -y 1
```
センサーの初期化のときにアドレスを68に指定します。  
sensor = adafruit_amg88xx.AMG88XX(i2c_bus, addr=0x68)  

## 参考情報
RaspberryPiで赤外線アレイセンサAMG8833(Grid-EYE)からデータ取得  
https://qiita.com/tm_nagoya/items/904ba8a23868ddcdcc54
赤外線アレイセンサAMG8833(Grid-EYE)のデータを表示
https://qiita.com/tm_nagoya/items/32d7e5becf73ba8a6110
AMG8833のデータシート
https://www.mouser.jp/datasheet/2/315/panasonic_04262016_AMG88-1480161.pdf

