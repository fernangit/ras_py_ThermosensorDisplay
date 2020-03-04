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

### インストール
1. Adafruit_AMG88xx_python取得  
```
sudo apt-get update
sudo apt-get install -y build-essential python-pip python-dev python-smbus git
git clone https://github.com/adafruit/Adafruit_Python_GPIO.git
cd Adafruit_Python_GPIO
sudo python3 setup.py install
sudo apt-get install -y python-scipy python-pygame
sudo pip3 install colour
cd ~/
git clone https://github.com/adafruit/Adafruit_AMG88xx_python.git
cd Adafruit_AMG88xx_python/Adafruit_AMG88xx/
```
2. Adafruit_AMG88xx.py(ライブラリ本体)を編集  
```
# AMG88xx_I2CADDR = 0x69 # default
AMG88xx_I2CADDR = 0x68 # new!
```
3. Adafruit_AMG88xx_pythonインストール  
```
cd .. # go back to Adafruit_AMG88xx_python/
python3 setup.py install
```

### プログラム実行
```
python3 ThermoIndication.py
```

## 参考情報
赤外線アレイセンサAMG8833(Grid-EYE)をRaspberry Piに繋げてデータを取得する．  
https://qiita.com/nobuyukioishi/items/499cb694b2d9286afdc3
RaspberryPiで赤外線アレイセンサAMG8833(Grid-EYE)からデータ取得  
https://qiita.com/tm_nagoya/items/904ba8a23868ddcdcc54  
赤外線アレイセンサAMG8833(Grid-EYE)のデータを表示  
https://qiita.com/tm_nagoya/items/32d7e5becf73ba8a6110  
AMG8833のデータシート  
https://www.mouser.jp/datasheet/2/315/panasonic_04262016_AMG88-1480161.pdf  

