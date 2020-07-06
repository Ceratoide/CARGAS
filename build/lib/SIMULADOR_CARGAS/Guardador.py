import matplotlib
import matplotlib.pyplot as plt
from SIMULADOR_CARGAS.Funciones import *
import pylab
from mpl_toolkits.mplot3d import axes3d
from matplotlib import style
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from pathlib import Path
import os 
from os.path import join
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
    plt.title('Campo y potencial eléctrico N.{:}'.format(numero))
    return fig

def peroen3d(CARGAS,numero):
    fig = plt.figure()
    ax1 = fig.add_subplot(111,projection='3d')
    xx = np.linspace(0, 800,50)
    yy = np.linspace(0, 600,50)
    X, Y = np.meshgrid(xx, yy)
    if len(CARGAS)>0:
        Z=carga.potencial(CARGAS[0],(X,Y))
        for i in CARGAS:
            if i!=CARGAS[0]:
                Z = Z+carga.potencial(i,(X,Y))
    surf = ax1.plot_surface(X, Y, Z, cmap=matplotlib.cm.inferno, linewidth=0, antialiased=False)
    ax1.zaxis.set_major_locator(LinearLocator(10))
    ax1.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    fig.colorbar(surf, shrink=0.5, aspect=5)
    plt.title('Potencial eléctrico N.{:}'.format(numero))
    return fig
def imagen_toda(CARGAS,numero):
    home = str(Path.home())
    try:
        os.mkdir(join(home,'Simulador de Cargas\Creaciones'))
    except FileExistsError:
        pass
    
    raw_todo(CARGAS,numero).savefig(join(home,'Simulador de cargas\Creaciones','Campo_y_Potencial_{:}.png'.format(numero)))
    peroen3d(CARGAS,numero).savefig(join(home,'Simulador de cargas\Creaciones','Potencial_3d_{:}.png'.format(numero)))

