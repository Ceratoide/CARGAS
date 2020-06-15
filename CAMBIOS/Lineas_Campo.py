import numpy as np
import matplotlib
from Funciones import *
import pylab
matplotlib.rcParams.update({'figure.max_open_warning': 0})
import gc
def raw_field(charges):
    fig = pylab.figure(figsize=[8, 6],dpi=100)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('off')
    x = np.linspace(0, 800, 64)
    y = np.linspace(0, 600, 64)
    X, Y = np.meshgrid(x, y)


    if len(charges)>0:
        Ex=carga.campo(charges[0],(X,Y))[0]
        Ey=carga.campo(charges[0],(X,Y))[1]
        for charge in charges:
            ex,ey=carga.campo(charge,(X,Y))
            Ex += ex
            Ey += ey
            
    
        ax.streamplot(x, y, Ex, Ey,color=(0,0,0), linewidth=1, cmap=matplotlib.cm.inferno, density=1, arrowstyle='->', arrowsize=1.5)
    
    return fig

def imagencampo(charges):
    raw_field(charges).savefig('campo.png')
    raw_field(charges).clf
    gc.collect()