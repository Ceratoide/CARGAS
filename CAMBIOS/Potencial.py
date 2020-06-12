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
ax = fig.add_axes([0, 0, 1, 1])
ax.axis('off')
xx = np.linspace(0, 800,20)
yy = np.linspace(0, 600,20)
X, Y = np.meshgrid(xx, yy)
canv = agg.FigureCanvasAgg(fig)
renderer = canv.get_renderer()
def raw_data(CARGA):
    Z = carga.potencial(CARGA,(X,Y))
    ax.contourf(X, Y, Z, 5)

    global canv
    canv.draw()
    global renderer
    raw_data = renderer.tostring_rgb()
    return raw_data


