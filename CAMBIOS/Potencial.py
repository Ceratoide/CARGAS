import matplotlib
import numpy as np
from Funciones import *
matplotlib.use("Agg")

import matplotlib.backends.backend_agg as agg


import pylab

fig = pylab.figure(figsize=[8, 6], # Inches
                   dpi=100,        # 100 dots per inch, so the resulting buffer is 400x400 pixels
                   )
ax = fig.gca()
t=np.arange(0,10,1)
xx = np.linspace(0, 600)
yy = xx.copy()
X, Y = np.meshgrid(xx, yy)
canv = agg.FigureCanvasAgg(fig)
renderer = canv.get_renderer()
def raw_data(CARGA):

    Z = carga.potencial(CARGA,(X,Y))
    ax.contourf(X, Y, Z, 3)

    global canv
    canv.draw()
    global renderer
    raw_data = renderer.tostring_rgb()
    return raw_data


