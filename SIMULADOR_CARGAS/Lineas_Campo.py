import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from SIMULADOR_CARGAS.Funciones import *
import pylab
from pathlib import Path
import os 
from os.path import join
import gc
def raw_field(charges):
    plt.style.use('dark_background')
    fig = pylab.figure(figsize=[8, 6],dpi=100)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('off')
    x = np.linspace(0, 800, 60)
    y = np.linspace(0, 600, 60)
    X, Y = np.meshgrid(x, y)

    if len(charges)>0:
        Ex=carga.campo(charges[0],(X,Y))[0]
        Ey=carga.campo(charges[0],(X,Y))[1]
        for charge in charges:
            ex,ey=carga.campo(charge,(X,Y))
            Ex += ex
            Ey += ey
        
    
        ax.streamplot(x, y, Ex, Ey,color=(1,1,1), linewidth=1.5, density=0.7, arrowstyle='->', arrowsize=1.3)
    
    return fig

def imagencampo(charges):
    home = str(Path.home())
    raw_field(charges).savefig(join(home,'Simulador de Cargas/Temporal','Campo.png'))
    raw_field(charges).clf()
    plt.close(raw_field(charges))
    gc.collect()