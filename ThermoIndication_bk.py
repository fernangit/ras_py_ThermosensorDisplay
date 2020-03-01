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
flg, ax = plt.subplots()

#�E�B���h�E�T�C�Y�ݒ�
plt.figure(figsize=(4, 4), dpi=50)

# ���[�v�J�n
while True:
    # �f�[�^�擾�Anumpy�ϊ��A1������2�����z��
    sens88 = np.array(sensor.readPixels()).reshape([8, 8])
    print(sens88)

#    # 8x8�s�N�Z���̃f�[�^
#    plt.subplot(1, 2, 1)
#    fig = plt.imshow(sensordata, cmap="inferno")
#    plt.colorbar()

    # bicubic��ԃf�[�^
#    plt.subplot(1, 2, 2)
#    fig = plt.imshow(sens88, cmap="inferno", interpolation="bicubic")
#    plt.colorbar()

    im = ax.imshow(sens88, cmap="inferno", interpolation="bicubic")
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.1)
    plt.colorbar(im, cax=cax)

    # plt.show���Ǝ~�܂��Ă��܂��̂ŁApause���g�p
    # plt.clf���Ȃ��ƃJ���[�o�[�������\�������
#    plt.show()
    plt.pause(.1)
    plt.clf()
    