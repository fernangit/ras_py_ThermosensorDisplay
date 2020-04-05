# coding: utf-8
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

#ウィンドウサイズ設定
#plt.figure(figsize=(19.2, 10.8)) #FullHD
plt.figure()
#フルサイズで表示
mng = plt.get_current_fig_manager()
mng.resize(*mng.window.maxsize())

#係数
coefficient = 1.0

# ループ開始
while True:
    # データ取得、numpy変換、1次元→2次元配列
    sens88 = np.array(sensor.readPixels()).reshape([8, 8])*coefficient
#    print(sens88)

    #最大温度表示
#    temp = sensor.readThermistor()
    temp = sens88.max()
#    print(temp)
    plt.text(0.4, 0.6, str(round(temp, 1))+'℃', color='black', fontsize=40)

#    # 8x8ピクセルのデータ
#    plt.subplot(1, 2, 1)
#    fig = plt.imshow(sensordata, cmap="inferno")
#    plt.colorbar()

    # bicubic補間データ
#    plt.subplot(1, 2, 2)
#    fig = plt.imshow(sens88, cmap="inferno", interpolation="bicubic")
    fig = plt.imshow(sens88, cmap="coolwarm", interpolation="bicubic", vmin=25, vmax=38)
    plt.colorbar()

    # plt.showだと止まってしまうので、pauseを使用
    # plt.clfしないとカラーバーが多数表示される
#    plt.show()
    plt.pause(0.01)
    plt.clf()
