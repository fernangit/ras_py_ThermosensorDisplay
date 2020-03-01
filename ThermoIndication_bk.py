# -*- coding: utf-8 -*-
import time
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

from Adafruit_AMG88xx import Adafruit_AMG88xx

sensor = Adafruit_AMG88xx()

# センサーの初期化待ち
time.sleep(.1)

# 8x8ピクセルの画像とbicubic補間をした画像を並べて表示させる
#plt.subplots(figsize=(8, 4))
flg, ax = plt.subplots()

#ウィンドウサイズ設定
plt.figure(figsize=(4, 4), dpi=50)

# ループ開始
while True:
    # データ取得、numpy変換、1次元→2次元配列
    sens88 = np.array(sensor.readPixels()).reshape([8, 8])
    print(sens88)

#    # 8x8ピクセルのデータ
#    plt.subplot(1, 2, 1)
#    fig = plt.imshow(sensordata, cmap="inferno")
#    plt.colorbar()

    # bicubic補間データ
#    plt.subplot(1, 2, 2)
#    fig = plt.imshow(sens88, cmap="inferno", interpolation="bicubic")
#    plt.colorbar()

    im = ax.imshow(sens88, cmap="inferno", interpolation="bicubic")
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.1)
    plt.colorbar(im, cax=cax)

    # plt.showだと止まってしまうので、pauseを使用
    # plt.clfしないとカラーバーが多数表示される
#    plt.show()
    plt.pause(.1)
    plt.clf()
    