import pygame,sys
from pygame.locals import *
import numpy as np

class MENU:
    def __init__(self):
        
        pygame.init()
        pygame.display.set_caption("Simulador Campo Electrico ")
        programIcon = pygame.image.load('proton.png')
        pygame.display.set_icon(programIcon)
        self.imagen_boton = pygame.image.load("flecha.png")
        self.imagen_boton_pressed = pygame.image.load("flecha2.png")
        self.imagen_boton_2= pygame.transform.flip(self.imagen_boton, True, False)
        self.imagen_boton_pressed_2= pygame.transform.flip(self.imagen_boton_pressed, True, False)
        self.volti=pygame.image.load("volti.png")
        self.volti_otro=pygame.transform.flip(self.volti,True,False)
        self.imagen_panel = pygame.image.load('MENU.jpg')
        self.clock=pygame.time.Clock()
        self.screen = pygame.display.set_mode((800, 600))
        self.fuente = pygame.font.SysFont('Courier', 20)
        
        
    def dibujar_botones_iniciales(self,otra_lista,lista_botones):
        panel = pygame.transform.scale(self.imagen_panel, [800, 600])
        self.screen.blit(panel, [0, 0])
        for boton in otra_lista:
            
            if boton['on_click']:
                self.screen.blit(boton['imagen_pressed'], boton['rect'])
            else:
                self.screen.blit(boton['imagen'], boton['rect'])
        for boton in lista_botones:
            self.screen.blit(boton['imagen'], boton['rect'])
            if boton['on_click']:
                self.screen.blit(boton['imagen_pressed'], boton['rect'])
                

       
                
    def otra_pantalla(self):
        self.clock.tick(10)    
        otra_pantalla = True
        botones = []
        r_boton_1_1 = self.imagen_boton.get_rect()
        r_boton_1_1.topleft = [670, 540]
        botones.append({ 'imagen': self.imagen_boton, 'imagen_pressed': self.imagen_boton_pressed, 'rect': r_boton_1_1, 'on_click': False})
        r_boton_2_2 = self.imagen_boton.get_rect()
        r_boton_2_2.topleft = [550, 540]
        botones.append({ 'imagen': self.imagen_boton_2, 'imagen_pressed': self.imagen_boton_pressed_2, 'rect': r_boton_2_2, 'on_click': False})
        otros_botones=[]
        r_boton_3_3 = self.volti.get_rect()
        r_boton_3_3.topleft = [325, 320]
        otros_botones.append({ 'imagen': self.volti, 'imagen_pressed': self.volti_otro, 'rect': r_boton_3_3, 'on_click': False})
        
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
                    for boton in otros_botones:
                        boton['on_click'] = boton['rect'].colliderect([mouse[0], mouse[1], 1, 1])
                    click = True          
                if event.type == MOUSEBUTTONUP:
                    for boton in botones:
                        boton['on_click'] = False
                    for boton in otros_botones:
                        boton['on_click'] = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        otra_pantalla = False
            if botones[0]['on_click'] and click:
                self.imagen_panel = pygame.image.load('fondo-pared-ladrillos.jpg')
                otros_botones=[]
                click = False
                
            if botones[1]['on_click'] and click:
                self.imagen_panel = pygame.image.load('MENU.jpg')
                otros_botones.append({ 'imagen': self.volti, 'imagen_pressed': self.volti_otro, 'rect': r_boton_3_3, 'on_click': False})
                click = False

            
            self.dibujar_botones_iniciales(otros_botones,botones)

            
            
            

            pygame.display.update()
