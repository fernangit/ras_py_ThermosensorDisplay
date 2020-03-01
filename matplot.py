# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1 import make_axes_locatable

img = np.random.rand(10, 10)
print(img.shape)
print(img)

flg, ax = plt.subplots()
#ax.imshow(img)
im = ax.imshow(img, cmap="inferno", interpolation="bicubic")

divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.1)
plt.colorbar(im, cax=cax)

plt.show()
