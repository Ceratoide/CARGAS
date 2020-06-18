import pygame,sys
from pygame.locals import *
import numpy as np
from Funciones import *
from Pantalla import *
from Menu import *

class main:
    def __init__(self):
        
        pygame.init()
        pygame.display.set_caption("Simulador Campo Electrico ")
        programIcon = pygame.image.load('proton.png')
        pygame.display.set_icon(programIcon)
        self.imagen_boton = pygame.image.load("iniciar.png")
        self.imagen_boton_pressed = pygame.image.load("iniciar_oprimido.png")
        self.imagen_panel = pygame.image.load('INICIO.jpg')
        self.clock=pygame.time.Clock()
        self.screen = pygame.display.set_mode((800, 600))
        self.screen.blit(self.imagen_panel,(0,0))

    def dibujar_botones_iniciales(self,lista_botones):
        panel = pygame.transform.scale(self.imagen_panel, [800, 600])
        self.screen.blit(panel, [0, 0])
        for boton in lista_botones:
            if boton['on_click']:
                self.screen.blit(boton['imagen_pressed'], boton['rect'])
            else:
                self.screen.blit(boton['imagen'], boton['rect'])

    def inicio(self):
        self.clock.tick(10)    
        otra_pantalla = True
        botones = []
        r_boton_1_1 = self.imagen_boton.get_rect()
        r_boton_1_1.topleft = [400, 270]
        botones.append({ 'imagen': self.imagen_boton, 'imagen_pressed': self.imagen_boton_pressed, 'rect': r_boton_1_1, 'on_click': False})
       
        while otra_pantalla:
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    sys.exit()
                click=False
                mouse=pygame.mouse.get_pos()
                for boton in botones:
                    boton['on_click'] = boton['rect'].colliderect([mouse[0], mouse[1], 1, 1])
                if event.type == MOUSEBUTTONDOWN:
                    click = True


            if botones[0]['on_click'] and click:
                MENU().otra_pantalla()
                click = False
                
                
            
            self.dibujar_botones_iniciales(botones)
            

            pygame.display.update()
main().inicio()