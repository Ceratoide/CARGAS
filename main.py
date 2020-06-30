import pygame,sys
from pygame.locals import *
import numpy as np
from Funciones import *
from Pantalla import *
from Pantallas import *
from instrucciones import *
class main:
    def __init__(self):
        
        pygame.init()
        pygame.display.set_caption("Simulador Campo Electrico ")
        programIcon = pygame.image.load('sprites\proton.png')
        pygame.display.set_icon(programIcon)
        self.imagen_boton = pygame.image.load("sprites\\iniciar.png")
        self.imagen_boton_pressed = pygame.image.load("sprites\\iniciar_oprimido.png")
        self.pantallas=pygame.image.load('sprites\\INSTRU.png')
        self.pantallas_press=pygame.image.load("sprites\\press.png")
        self.sortir=pygame.image.load('sprites\\SALIR.png')
        self.sortir_press=pygame.image.load('sprites\\SALIR_PRESS.png')
        self.instrucciones= pygame.image.load('sprites\\PANTA.png')
        self.imagen_panel = pygame.image.load('pantallas\\INICIO.jpg')
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
        r_boton_2_2 = self.pantallas.get_rect()
        r_boton_2_2.topleft = [475, 365]
        botones.append({ 'imagen': self.pantallas_press, 'imagen_pressed': self.pantallas, 'rect': r_boton_2_2, 'on_click': False})
        r_boton_3_3 = self.pantallas.get_rect()
        r_boton_3_3.topleft = [475, 440]
        botones.append({ 'imagen': self.pantallas_press, 'imagen_pressed': self.instrucciones, 'rect': r_boton_3_3, 'on_click': False})
        r_boton_4_4 = self.sortir.get_rect()
        r_boton_4_4.topleft = [360, 470]
        botones.append({ 'imagen': self.sortir, 'imagen_pressed': self.sortir_press, 'rect': r_boton_4_4, 'on_click': False})
        
        
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
                world.visual()
                click = False

            if botones[1]['on_click'] and click:
                INSTRUCCIONES().otra_pantalla()
                click = False

            if botones[2]['on_click'] and click:
                PANTALLAS().otra_pantalla()
                click = False

            if botones[3]['on_click'] and click:
                pygame.quit()
                sys.exit()
                
                
            
            self.dibujar_botones_iniciales(botones)
            

            pygame.display.update()
main().inicio()