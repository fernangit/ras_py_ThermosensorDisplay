# -*- coding: utf-8 -*-
import time
import busio
import board

import adafruit_amg88xx

# I2C�o�X�̏�����
i2c_bus = busio.I2C(board.SCL, board.SDA)

# �Z���T�[�̏�����
# �A�h���X��68�Ɏw��
sensor = adafruit_amg88xx.AMG88XX(i2c_bus, addr=0x68)

# �Z���T�[�̏������҂�
time.sleep(.1)

# 8x8�̕\��
print(sensor.pixels)