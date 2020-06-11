import numpy as np
import matplotlib.pyplot as plt
from Funciones import *


class lineas_de_campo:
    def __init__(self):
        pygame.init()
        carga.init()
        nx, ny = 64, 64
        self.x=np.linspace(-2,2,nx)
        self.y=np.linspace(-2,2,ny)
        self.X, self.Y = np.meshgrid(self.x, self.y)
        count = 1
        

