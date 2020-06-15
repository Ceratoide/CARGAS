import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from Funciones import *
import pylab
matplotlib.rcParams.update({'figure.max_open_warning': 0})
import gc
def raw_field(charges):
    plt.style.use('dark_background')
    fig = pylab.figure(figsize=[8, 6],dpi=100)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('off')
    x = np.linspace(0, 800, 100)
    y = np.linspace(0, 600, 100)
    X, Y = np.meshgrid(x, y)

    if len(charges)>0:
        Ex=carga.campo(charges[0],(X,Y))[0]
        Ey=carga.campo(charges[0],(X,Y))[1]
        for charge in charges:
            ex,ey=carga.campo(charge,(X,Y))
            Ex += ex
            Ey += ey
        
    
        ax.streamplot(x, y, Ex, Ey,color=(1,1,1), linewidth=1, density=0.8, arrowstyle='->', arrowsize=1.5)
    
    return fig

def imagencampo(charges):
    raw_field(charges).savefig('campo.png')
    raw_field(charges).clf()
    plt.close(raw_field(charges))
    gc.collect()