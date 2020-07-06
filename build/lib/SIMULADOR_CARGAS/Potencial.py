import matplotlib
import matplotlib.pyplot as plt
from SIMULADOR_CARGAS.Funciones import *
import pylab
import gc
from pathlib import Path
import os 
from os.path import join
def raw_data(potenciales):
    fig = pylab.figure(figsize=[8, 6],dpi=100)
    ax = fig.gca()
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('off')
    xx = np.linspace(0, 800,40)
    yy = np.linspace(0, 600,40)
    X, Y = np.meshgrid(xx, yy)
    if len(potenciales)>0:
        Z=carga.potencial(potenciales[0],(X,Y))
        for i in potenciales:
            if i!=potenciales[0]:
                Z = Z+carga.potencial(i,(X,Y))
        
        ax.contourf(X, Y, Z, 90,cmap=matplotlib.cm.inferno)
        ax.contour(X,Y,Z,90,colors='k')
    
    return fig
def barra(potenciales):
    plt.style.use('dark_background')
    xx = np.linspace(0, 800,50)
    yy = np.linspace(0, 600,50)
    X, Y = np.meshgrid(xx, yy)
    if len(potenciales)>0:
        Z=carga.potencial(potenciales[0],(X,Y))
        for i in potenciales:
            if i!=potenciales[0]:
                Z = Z+carga.potencial(i,(X,Y))


    fig,ax = plt.subplots()

    mpb=plt.contourf(X, Y, Z, 50,cmap=matplotlib.cm.inferno)
    plt.colorbar(mpb,ax=ax,fraction=0.20,orientation="horizontal",shrink=0.7,aspect=8)
    ax.remove()
        
    return fig

def imagen(potenciales):
    home = str(Path.home())
    raw_data(potenciales).savefig(join(home,'Simulador de Cargas\Temporal','Potencial.png'))
    barra(potenciales).savefig(join(home,'Simulador de Cargas\Temporal','Barra.png'),bbox_inches='tight')
    plt.close(raw_data(potenciales))
    raw_data(potenciales).clf()
    gc.collect()
    
    



       
        


