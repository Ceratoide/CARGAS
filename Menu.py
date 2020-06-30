import pygame,sys
from pygame.locals import *
import numpy as np
from Pantalla import *
from instrucciones import *
from Pantallas import *
class MENU:
    def __init__(self):
        
        pygame.init()
        pygame.display.set_caption("Simulador Campo Electrico ")
        programIcon = pygame.image.load('sprites\\proton.png')
        pygame.display.set_icon(programIcon)

        self.volti=pygame.image.load("volti.png")
        self.pantallas=pygame.image.load('PANTA.png')
        self.instrucciones= pygame.image.load('INSTRU.png')
        self.imagen_panel = pygame.image.load('MENU.jpg')

        self.clock=pygame.time.Clock()
        self.screen = pygame.display.set_mode((800, 600))
        self.fuente = pygame.font.SysFont('Courier', 20)
        
        
    def dibujar_botones_iniciales(self,otra_lista):
        panel = pygame.transform.scale(self.imagen_panel, [800, 600])
        self.screen.blit(panel, [0, 0])
        for boton in otra_lista:
            
            if boton['on_click']:
                self.screen.blit(boton['imagen_pressed'], boton['rect'])
            else:
                self.screen.blit(boton['imagen'], boton['rect'])


       
                
    def otra_pantalla(self):
        self.clock.tick(10)    
        otra_pantalla = True
        botones = []
        r_boton_1_1 = self.volti.get_rect()
        r_boton_1_1.topleft = [325, 320]
        botones.append({ 'imagen': self.volti, 'imagen_pressed': self.volti, 'rect': r_boton_1_1, 'on_click': False})
        r_boton_2_2 = self.pantallas.get_rect()
        r_boton_2_2.topleft = [283, 100]
        botones.append({ 'imagen': self.pantallas, 'imagen_pressed': self.pantallas, 'rect': r_boton_2_2, 'on_click': False})
        r_boton_3_3 = self.pantallas.get_rect()
        r_boton_3_3.topleft = [283, 170]
        botones.append({ 'imagen': self.instrucciones, 'imagen_pressed': self.instrucciones, 'rect': r_boton_3_3, 'on_click': False})
        
        
        
        
        
        
        while otra_pantalla:
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    mouse = event.pos
                    for boton in botones:
                        boton['on_click'] = boton['rect'].colliderect([mouse[0], mouse[1], 1, 1])
                    click = True
       
                if event.type == MOUSEBUTTONUP:
                    for boton in botones:
                        boton['on_click'] = False
                

                        
                if botones[0]['on_click'] and click:
                    world.visual()


            
            self.dibujar_botones_iniciales(botones)

            
            
            

            pygame.display.update()
