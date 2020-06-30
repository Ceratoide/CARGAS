import matplotlib
import matplotlib.pyplot as plt
from Funciones import *
import pylab
def raw_todo(CARGAS,numero):
    plt.style.use('dark_background')
    fig = pylab.figure(figsize=[8, 6],dpi=100)
    ax = fig.gca()
    xx = np.linspace(0, 800,30)
    yy = np.linspace(0, 600,30)
    x = np.linspace(0, 800, 100)
    y = np.linspace(0, 600, 100)
    X, Y = np.meshgrid(xx, yy)
    Xf,Yf=np.meshgrid(x, y)
    if len(CARGAS)>0:
        Z=carga.potencial(CARGAS[0],(X,Y))
        for i in CARGAS:
            if i!=CARGAS[0]:
                Z = Z+carga.potencial(i,(X,Y))
        
        s=ax.contourf(X, Y, Z, 50,cmap=matplotlib.cm.inferno)
        
        Ex=carga.campo(CARGAS[0],(Xf,Yf))[0]
        Ey=carga.campo(CARGAS[0],(Xf,Yf))[1]
        for charge in CARGAS:
            ex,ey=carga.campo(charge,(Xf,Yf))
            Ex += ex
            Ey += ey
        
    
        ax.streamplot(x, y, Ex, Ey,color=(1,1,1), linewidth=1.5, density=1.5, arrowstyle='->', arrowsize=1.3)
    plt.colorbar(s,ax=ax)
    plt.title('CAMPO Y POTENCIAL ELECTRICO #{:}'.format(numero))
    return fig
def imagen_toda(CARGAS,numero):
    raw_todo(CARGAS,numero).savefig('Creaciones\Campo_y_Potencial_{:}.png'.format(numero))