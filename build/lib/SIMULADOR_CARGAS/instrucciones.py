import pygame,sys
from pygame.locals import *
import numpy as np
from pkg_resources import resource_stream, resource_string, resource_filename
class INSTRUCCIONES:
    def __init__(self):
        
        pygame.init()
        pygame.display.set_caption(resource_filename("SIMULADOR_CARGAS","Simulador Campo Electrico "))
        programIcon = pygame.image.load(resource_filename("SIMULADOR_CARGAS",'sprites\\proton.png'))
        pygame.display.set_icon(programIcon)
        self.imagen_boton = pygame.image.load(resource_filename("SIMULADOR_CARGAS","sprites\\flecha.png"))
        self.imagen_boton_pressed = pygame.image.load(resource_filename("SIMULADOR_CARGAS","sprites\\flecha2.png"))
        self.imagen_boton_2= pygame.transform.flip(self.imagen_boton, True, False)
        self.imagen_boton_pressed_2= pygame.transform.flip(self.imagen_boton_pressed, True, False)
        self.MC=pygame.image.load(resource_filename("SIMULADOR_CARGAS",'pantallas\\MenuCargas.png'))
        self.PC=pygame.image.load(resource_filename("SIMULADOR_CARGAS",'pantallas\\MenuCP.png'))
        self.FIELD=pygame.image.load(resource_filename("SIMULADOR_CARGAS",'pantallas\\MenuCampo.png'))
        self.ROJO=pygame.image.load(resource_filename("SIMULADOR_CARGAS",'pantallas\\MenuRojo.png'))
        self.FINAL=pygame.image.load(resource_filename("SIMULADOR_CARGAS",'pantallas\\Menultimo.png'))
        self.imagen_panel = self.MC
        
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
        r_boton_1_1 = self.imagen_boton.get_rect()
        r_boton_1_1.topleft = [670, 540]
        botones.append({ 'imagen': self.imagen_boton, 'imagen_pressed': self.imagen_boton_pressed, 'rect': r_boton_1_1, 'on_click': False})
        r_boton_2_2 = self.imagen_boton.get_rect()
        r_boton_2_2.topleft = [550, 540]
        botones.append({ 'imagen': self.imagen_boton_2, 'imagen_pressed': self.imagen_boton_pressed_2, 'rect': r_boton_2_2, 'on_click': False})

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

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        otra_pantalla = False
            if botones[0]['on_click'] and click:
                if self.imagen_panel == self.MC:
                    self.imagen_panel = self.PC
                elif self.imagen_panel == self.PC:
                    self.imagen_panel = self.FIELD
                elif self.imagen_panel == self.FIELD:
                    self.imagen_panel = self.ROJO
                elif self.imagen_panel == self.ROJO:
                    self.imagen_panel= self.FINAL
                    
                click = False
                
            if botones[1]['on_click'] and click:
                if self.imagen_panel == self.FINAL:
                    self.imagen_panel = self.ROJO
                elif self.imagen_panel == self.ROJO:
                    self.imagen_panel = self.FIELD
                elif self.imagen_panel == self.FIELD:
                    self.imagen_panel = self.PC
                elif self.imagen_panel == self.PC:
                    self.imagen_panel= self.MC             
                click = False

            
            self.dibujar_botones_iniciales(botones)

            
            
            

            pygame.display.update()


