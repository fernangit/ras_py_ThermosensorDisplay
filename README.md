# ras_py_ThermosensorDisplay
Temperature measurement by thermosensor on the raspberry pie
---
* �T�[���Z���T�[  
  * AMG8833(Grid-EYE)����f�[�^�擾  


## HOW TO USE
### �ڑ�
AMG8833(3.3V) �� GPIO1(3.3V) 
AMG8833(GND) �� GPIO6(Ground)  
AMG8833(SDA) �� GPIO3(SDA)  
AMG8833(SCL) �� GPIO5(SCL)  

### I2C �L����
```
sudo raspi-config
-> 5 Interfacing Options
--> P5 I2C
```
�ڑ��m�F
```
i2cdetect -y 1
```

### �C���X�g�[��
1. Adafruit_AMG88xx_python�擾  
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
2. Adafruit_AMG88xx.py(���C�u�����{��)��ҏW  
```
# AMG88xx_I2CADDR = 0x69 # default
AMG88xx_I2CADDR = 0x68 # new!
```
3. Adafruit_AMG88xx_python�C���X�g�[��  
```
cd .. # go back to Adafruit_AMG88xx_python/
python3 setup.py install
```

### �v���O�������s
```
python3 ThermoIndication.py
```

## �Q�l���
�ԊO���A���C�Z���TAMG8833(Grid-EYE)��Raspberry Pi�Ɍq���ăf�[�^���擾����D  
https://qiita.com/nobuyukioishi/items/499cb694b2d9286afdc3
RaspberryPi�ŐԊO���A���C�Z���TAMG8833(Grid-EYE)����f�[�^�擾  
https://qiita.com/tm_nagoya/items/904ba8a23868ddcdcc54  
�ԊO���A���C�Z���TAMG8833(Grid-EYE)�̃f�[�^��\��  
https://qiita.com/tm_nagoya/items/32d7e5becf73ba8a6110  
AMG8833�̃f�[�^�V�[�g  
https://www.mouser.jp/datasheet/2/315/panasonic_04262016_AMG88-1480161.pdf  

