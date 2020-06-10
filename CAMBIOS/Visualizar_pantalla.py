import pygame,sys
from pygame.locals import *
import numpy as np
from Funciones import *
from Pantalla import *
from Menu import *

def visual():
        ELECTRON = pygame.image.load("prueba.png")
        ELECTRON_PULSO = pygame.image.load("PRUEBA_OPRIMIDO.png")
        CARGA = pygame.image.load("CARGA.png")
        CARGA_PULSO = pygame.image.load("CARGA_OPRIMIDO.png")
        NEW=pygame.image.load("LIMPIAR.png")
        NEW_PULSO=pygame.image.load("LIMPIAR_OPRIMIDO.png")
        v=[]
        u=[]
        botones = []
        r_boton_1_1 = ELECTRON.get_rect()
        r_boton_1_1.topleft = [40, 135]
        botones.append({ 'imagen': ELECTRON, 'imagen_pressed': ELECTRON_PULSO, 'rect': r_boton_1_1, 'on_click': False})
        r_boton_2_2 = CARGA.get_rect()
        r_boton_2_2.topleft = [130, 135]
        botones.append({ 'imagen': CARGA, 'imagen_pressed': CARGA_PULSO, 'rect': r_boton_2_2, 'on_click': False})
        r_boton_3_3 = NEW.get_rect()
        r_boton_3_3.topleft = [45, 510]
        botones.append({ 'imagen': NEW, 'imagen_pressed': NEW_PULSO, 'rect': r_boton_3_3, 'on_click': False})
        b=None
        while True:
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    
                    mouse = event.pos
                    for boton in botones:
                        boton['on_click'] = boton['rect'].colliderect([mouse[0], mouse[1], 1, 1])
                    click = True
                    if botones[0]['on_click'] and click:
                        b=True
                    if botones[1]['on_click'] and click:
                        b=False
                    if b==True:
                        if pygame.mouse.get_pos()[0]>225:
                            v=v+[ball(pygame.mouse.get_pos(),(0,0),10)]
                    else:
                        if pygame.mouse.get_pos()[0]>225:
                            u=u+[carga(pygame.mouse.get_pos(),-10)]
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        MENU().otra_pantalla()
                        #w.update()

                if event.type==QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONUP:
                    for boton in botones:
                        boton['on_click'] = False
            if botones[2]['on_click'] and click:
                u=[]
                v=[]


         
                

            world(v,u).update(botones)
