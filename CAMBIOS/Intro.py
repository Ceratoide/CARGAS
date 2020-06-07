import pygame,sys
from pygame.locals import *
import numpy as np
from Funciones import *
from Pantalla import *
from Menu import *

def Iniciar():
        pygame.init()
        pygame.display.set_caption("Simulador Campo Electrico ")
        clock=pygame.time.Clock()
        
        screen = pygame.display.set_mode((800, 600))
        bg_image = pygame.image.load("INICIO.png")
        bg_image = bg_image.convert()
        screen.blit(bg_image,(0,0))
        clock.tick(10)    
        otra_pantalla = True
        while otra_pantalla:
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        otra_pantalla = False
                        world.visual()
                        
            pygame.display.update() 

