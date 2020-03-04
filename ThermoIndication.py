# -*- coding: utf-8 -*-
import time
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

from Adafruit_AMG88xx import Adafruit_AMG88xx

sensor = Adafruit_AMG88xx()

# �Z���T�[�̏������҂�
time.sleep(.1)

# 8x8�s�N�Z���̉摜��bicubic��Ԃ������摜����ׂĕ\��������
#plt.subplots(figsize=(8, 4))

#�E�B���h�E�T�C�Y�ݒ�
#plt.figure(figsize=(19.2, 10.8)) #�t��HD
plt.figure()
#�t���T�C�Y�ŕ\��
mng = plt.get_current_fig_manager()
mng.resize(*mng.window.maxsize())

#�W��
coefficient = 1.1

# ���[�v�J�n
while True:
    # �f�[�^�擾�Anumpy�ϊ��A1������2�����z��
    sens88 = np.array(sensor.readPixels()).reshape([8, 8])*coefficient
#    print(sens88)

    #�ő剷�x�\��
#    temp = sensor.readThermistor()
    temp = sens88.max()
#    print(temp)
    plt.text(0.4, 0.6, str(round(temp, 1))+'��', color='black', fontsize=40)

#    # 8x8�s�N�Z���̃f�[�^
#    plt.subplot(1, 2, 1)
#    fig = plt.imshow(sensordata, cmap="inferno")
#    plt.colorbar()

    # bicubic��ԃf�[�^
#    plt.subplot(1, 2, 2)
#    fig = plt.imshow(sens88, cmap="inferno", interpolation="bicubic")
    fig = plt.imshow(sens88, cmap="coolwarm", interpolation="bicubic", vmin=25, vmax=38)
    plt.colorbar()

    # plt.show���Ǝ~�܂��Ă��܂��̂ŁApause���g�p
    # plt.clf���Ȃ��ƃJ���[�o�[�������\�������
#    plt.show()
    plt.pause(0.01)
    plt.clf()
