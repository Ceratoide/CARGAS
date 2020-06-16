import matplotlib
import matplotlib.pyplot as plt
from Funciones import *
import pylab
import gc

def raw_data(potenciales):
    fig = pylab.figure(figsize=[8, 6],dpi=100)
    ax = fig.gca()
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('off')
    xx = np.linspace(0, 800,50)
    yy = np.linspace(0, 600,50)
    X, Y = np.meshgrid(xx, yy)
    
    if len(potenciales)>0:
        Z=carga.potencial(potenciales[0],(X,Y))
        for i in potenciales:
            if i!=potenciales[0]:
                Z = Z+carga.potencial(i,(X,Y))

        ax.contourf(X, Y, Z, levels=100,cmap=matplotlib.cm.inferno)
        ax.contour(X,Y,Z,levels=80,colors='k')

    return fig
def imagen(potenciales):
    raw_data(potenciales).savefig('potencial.png')
    plt.close(raw_data(potenciales))
    raw_data(potenciales).clf()
    gc.collect()
    
    



       
        


