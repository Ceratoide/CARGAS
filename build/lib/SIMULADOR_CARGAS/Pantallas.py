import pygame,sys
from pygame.locals import *
import numpy as np
from SIMULADOR_CARGAS.Pantalla import *
from pkg_resources import resource_stream, resource_string, resource_filename

class PANTALLAS:
    def __init__(self):
        
        pygame.init()
        pygame.display.set_caption("Simulador Campo Electrico ")
        programIcon = pygame.image.load(resource_filename("SIMULADOR_CARGAS",'sprites/proton.png'))
        pygame.display.set_icon(programIcon)
        self.imagen_boton = pygame.image.load(resource_filename("SIMULADOR_CARGAS","sprites/flecha.png"))
        self.imagen_boton_pressed = pygame.image.load(resource_filename("SIMULADOR_CARGAS","sprites/flecha2.png"))
        self.imagen_boton_2= pygame.transform.flip(self.imagen_boton, True, False)
        self.imagen_boton_pressed_2= pygame.transform.flip(self.imagen_boton_pressed, True, False)
        self.imagen_panel = pygame.image.load(resource_filename("SIMULADOR_CARGAS",'pantallas/pantallass.jpg'))
        self.clock=pygame.time.Clock()
        self.screen = pygame.display.set_mode((800, 600))
        self.fuente = pygame.font.SysFont('Courier', 20)
        self.anillo = pygame.image.load(resource_filename("SIMULADOR_CARGAS","sprites/carga_en_anillo.png"))
        self.constante=pygame.image.load(resource_filename("SIMULADOR_CARGAS","sprites/constante.png"))
        self.dipolo=pygame.image.load(resource_filename("SIMULADOR_CARGAS",'sprites/dipolo.png'))
        self.text_anillo=pygame.image.load(resource_filename("SIMULADOR_CARGAS",'sprites/ANILLO.png'))
        self.text_constante=pygame.image.load(resource_filename("SIMULADOR_CARGAS",'sprites/CONS.png'))
        self.text_dipolo=pygame.image.load(resource_filename("SIMULADOR_CARGAS",'sprites/DIPOL.png'))
        self.selector=pygame.image.load(resource_filename("SIMULADOR_CARGAS",'sprites/selector.png'))
        self.start=pygame.image.load(resource_filename("SIMULADOR_CARGAS",'sprites/INICIARP.png'))
        self.pantalla=self.text_anillo
        
    def dibujar_botones_iniciales(self,otra_lista,b):
        panel = pygame.transform.scale(self.imagen_panel, [800, 600])
        self.screen.blit(panel, [0, 0])
        self.screen.blit(self.anillo,(51,72))
        self.screen.blit(self.constante,(303,72))
        self.screen.blit(self.dipolo,(555,72))
        self.screen.blit(self.pantalla,(120,330))
        self.screen.blit(self.selector,(b,72))
        
        for boton in otra_lista:
            
            if boton['on_click']:
                self.screen.blit(boton['imagen_pressed'], boton['rect'])
            else:
                self.screen.blit(boton['imagen'], boton['rect'])

                
    def otra_pantalla(self):
        self.clock.tick(10)    
        botones = []
        otra_pantalla=True
        r_boton_1_1 = self.imagen_boton.get_rect()
        r_boton_1_1.topleft = [270, 540]
        botones.append({ 'imagen': self.imagen_boton, 'imagen_pressed': self.imagen_boton_pressed, 'rect': r_boton_1_1, 'on_click': False})
        r_boton_2_2 = self.imagen_boton_2.get_rect()
        r_boton_2_2.topleft = [150, 540]
        botones.append({ 'imagen': self.imagen_boton_2, 'imagen_pressed': self.imagen_boton_pressed_2, 'rect': r_boton_2_2, 'on_click': False})
        r_boton_3_3 = self.start.get_rect()
        r_boton_3_3.topleft = [200, 480]
        botones.append({ 'imagen': self.start, 'imagen_pressed': self.start, 'rect': r_boton_3_3, 'on_click': False})
        
        b=51
        segundo=False
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
                if segundo==False:
                    self.pantalla=self.text_constante
                    b=303
                    segundo=True
                    click = False
                else:
                    self.pantalla=self.text_dipolo
                    b=555
                    click = False
                
            if botones[1]['on_click'] and click:
                if segundo==False:
                    self.pantalla=self.text_anillo
                    b=51
                    click = False
                else:
                    self.pantalla=self.text_constante
                    b=303
                    segundo=False
                    click = False
            if botones[2]['on_click'] and click:
                if self.pantalla==self.text_anillo:
                    world.visual(pantalla1=True)
                elif self.pantalla==self.text_constante:
                    world.visual(pantalla2=True)
                elif self.pantalla==self.text_dipolo:
                    world.visual(pantalla3=True)
                click = False
                    
                
                    


            
            self.dibujar_botones_iniciales(botones,b)

            
            
            

            pygame.display.update()


