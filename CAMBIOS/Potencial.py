import matplotlib
from Funciones import *
import pylab


def raw_data(potenciales):
    fig = pylab.figure(figsize=[8, 6],dpi=100)
    ax = fig.gca()
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('off')
    xx = np.linspace(0, 800,25)
    yy = np.linspace(0, 600,25)
    X, Y = np.meshgrid(xx, yy)

    if len(potenciales)>0:
        Z=carga.potencial(potenciales[0],(X,Y))
        for i in potenciales:
            if i!=potenciales[0]:
                Z = Z+carga.potencial(i,(X,Y))
            
        
        
        ax.contourf(X, Y, Z, 30)
        ax.contour(X,Y,Z,10,colors='k')

    return fig
def imagen(potenciales):
    raw_data(potenciales).savefig('potencial.png')



       
        


