import matplotlib
import numpy as np
from Funciones import *
matplotlib.use("Agg")

import matplotlib.backends.backend_agg as agg
matplotlib.rcParams.update({'figure.max_open_warning': 0})

import pylab

fig = pylab.figure(figsize=[8, 6],dpi=100)
ax = fig.gca()
ax = fig.add_axes([0, 0, 1, 1])
ax.axis('off')
xx = np.linspace(0, 800,30)
yy = np.linspace(0, 600,30)
X, Y = np.meshgrid(xx, yy)
canv = agg.FigureCanvasAgg(fig)
renderer = canv.get_renderer()
def raw_data(potenciales):
    if len(potenciales)>0:
        Z=carga.potencial(potenciales[0],(X,Y))
        for i in potenciales:
            if i!=potenciales[0]:
                Z = Z+carga.potencial(i,(X,Y))
            
        ax.contourf(X, Y, Z, 20)
       
        
    global canv
    canv.draw()
    global renderer
    raw_data = renderer.tostring_rgb()
    return raw_data


