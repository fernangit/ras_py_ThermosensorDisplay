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

### �C���X�g�[��
1. CircuitPython
```
sudo pip3 install adafruit-circuitpython-amg88xx
```

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
�Z���T�[�̏������̂Ƃ��ɃA�h���X��68�Ɏw�肵�܂��B  
sensor = adafruit_amg88xx.AMG88XX(i2c_bus, addr=0x68)  

## �Q�l���
RaspberryPi�ŐԊO���A���C�Z���TAMG8833(Grid-EYE)����f�[�^�擾  
https://qiita.com/tm_nagoya/items/904ba8a23868ddcdcc54
�ԊO���A���C�Z���TAMG8833(Grid-EYE)�̃f�[�^��\��
https://qiita.com/tm_nagoya/items/32d7e5becf73ba8a6110
AMG8833�̃f�[�^�V�[�g
https://www.mouser.jp/datasheet/2/315/panasonic_04262016_AMG88-1480161.pdf

