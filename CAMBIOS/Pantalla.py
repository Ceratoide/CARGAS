import pygame,sys
from pygame.locals import *
import numpy as np
from Funciones import *
from Menu import *
from textos import *
from Potencial import *
from Lineas_Campo import *
from os import remove
pote=False
campe=False
class world:
    def __init__(self,ball,cargas):
        global pote
        pygame.init()
        pygame.display.set_caption("Simulador Campo Electrico")
        programIcon = pygame.image.load('proton.png')
        pygame.display.set_icon(programIcon)
        self.clock=pygame.time.Clock()
        self.ball=ball
        self.cargas=cargas
        self.screen = pygame.display.set_mode((800, 600))
        self.tablero=pygame.image.load("Tab.png")
        self.fuente= pygame.font.Font('DS-DIGIB.TTF', 30)
        self.window = pygame.display.get_surface()
        if pote==True:
            self.surf = pygame.transform.flip(pygame.image.load("potencial.png"),False,True)
        elif campe==True:
            self.surf = pygame.transform.flip(pygame.image.load("campo.png"),False,True)
        elif pote==False and campe==False:
            self.surf =pygame.image.load('fondo.png')
        self.surf=self.surf.convert()
        self.window.blit(self.surf, (0,0))
    def dibujar_botones(self,lista_botones):
        panel = pygame.transform.scale(self.tablero, [800, 600])
        self.screen.blit(panel, [0, 0])
        for boton in lista_botones:
            if boton['on_click']:
                self.screen.blit(boton['imagen_pressed'], boton['rect'])
            else:
                self.screen.blit(boton['imagen'], boton['rect'])
    def update(self,lista_botones,input_boxes,POT,update_potencial,CAMP,update_campo):
        self.clock.tick(10)   
        global pote
        global campe
        for o in self.ball :
            self.screen.blit(self.surf,(o.pos[0],o.pos[1]),o.pos)
        for i in range(len(self.ball)):
            for j in range(len(self.cargas)):
                self.ball[i].col(self.cargas[j])
        
        if update_potencial==True:
            imagen(self.cargas)
        if update_campo==True:
            imagencampo(self.cargas)
        if POT==True:
            pote=True
        else:
            pote=False
        if CAMP==True:
            campe=True
        else:
            campe=False

        campo_total=0
        potencial_total=0
        for k in self.cargas:
            self.screen.blit(k.image,k.pos)
            for o in self.ball:
                
                o.acel=o.fuerza(k)
                o.move(k)
                self.screen.blit(o.image,o.pos)
            campo_total=campo_total+carga.magnitud_campo(k,pygame.mouse.get_pos())
            potencial_total=potencial_total+carga.potencial(k,pygame.mouse.get_pos())
        texto=self.fuente.render("{:.5f}".format(campo_total), 0, (0, 0, 0))
        texto2=self.fuente.render("{:.5f}".format(potencial_total), 0, (0, 0, 0))
        self.dibujar_botones(lista_botones)
        self.screen.blit(texto, (20,243))
        self.screen.blit(texto2, (20,315))

        for box in input_boxes:
            box.pintar(self.screen)
        pygame.display.flip()
        
    def visual():
        mag = cajas_texto(13, 391, 195, 32)
        velx = cajas_texto(13, 460, 100, 32)
        vely = cajas_texto(112, 460, 95, 32)
        input_boxes = [mag, velx,vely]
        ELECTRON = pygame.image.load("prueba.png")
        ELECTRON_PULSO = pygame.image.load("PRUEBA_OPRIMIDO.png")
        CARGA = pygame.image.load("CARGA.png")
        CARGA_PULSO = pygame.image.load("CARGA_OPRIMIDO.png")
        NEW=pygame.image.load("LIMPIAR.png")
        NEW_PULSO=pygame.image.load("LIMPIAR_OPRIMIDO.png")
        ULTIMO=pygame.image.load("return.png")
        ULTIMO_PULSO=pygame.image.load("return_press.png")
        COZZETTI=pygame.image.load("POT.png")
        MAXIMO_COZZETTI=pygame.image.load("POT_PRESS.png")
        CAMP=pygame.image.load("CAMP.png")
        CAMP_PRESS=pygame.image.load("CAMP_PRESS.png")
        v=[]
        u=[carga((100,100),0)]
        botones = []
        r_boton_1_1 = ELECTRON.get_rect()
        r_boton_1_1.topleft = [40, 135]
        botones.append({ 'imagen': ELECTRON, 'imagen_pressed': ELECTRON_PULSO, 'rect': r_boton_1_1, 'on_click': False})
        r_boton_2_2 = CARGA.get_rect()
        r_boton_2_2.topleft = [130, 135]
        botones.append({ 'imagen': CARGA, 'imagen_pressed': CARGA_PULSO, 'rect': r_boton_2_2, 'on_click': False})
        r_boton_3_3 = NEW.get_rect()
        r_boton_3_3.topleft = [25, 510]
        botones.append({ 'imagen': NEW, 'imagen_pressed': NEW_PULSO, 'rect': r_boton_3_3, 'on_click': False})
        r_boton_4_4 = ULTIMO.get_rect()
        r_boton_4_4.topleft = [155, 505]
        botones.append({ 'imagen': ULTIMO, 'imagen_pressed': ULTIMO_PULSO, 'rect': r_boton_4_4, 'on_click': False})
        r_boton_5_5 = CAMP.get_rect()
        r_boton_5_5.topleft = [40, 35]
        botones.append({ 'imagen': COZZETTI, 'imagen_pressed': MAXIMO_COZZETTI, 'rect': r_boton_5_5, 'on_click': False})
        r_boton_6_6 = COZZETTI.get_rect()
        r_boton_6_6.topleft = [40, 75]
        botones.append({ 'imagen': CAMP, 'imagen_pressed': CAMP_PRESS, 'rect': r_boton_6_6, 'on_click': False})
        b=None
        VelX=0
        VelY=0
        Mag=0
        pot=False
        camp=False
        n=0
        l=0
        paso=True
        while True:
            update_potencial=False
            update_campo=False
            
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
                    mouse=pygame.mouse.get_pos()
                    if b==True:
                        if pygame.mouse.get_pos()[0]>225:
                            v=v+[ball((mouse[0]-10,mouse[1]-10),(VelX,-VelY),Mag)]
                    else:
                        if pygame.mouse.get_pos()[0]>225:
                            u=u+[carga((mouse[0]-20,mouse[1]-20),Mag)]
                            if botones[4]['on_click'] and click or pot==True:
                                update_potencial=True
                                update_campo=False
                            elif botones[5]['on_click'] and click or camp==True:
                                update_campo=True
                                update_potencial=False
                                
                            
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        MENU().otra_pantalla()
                        

                if event.type==QUIT:
                    try:
                        remove('potencial.png')
                    except FileNotFoundError:
                        pass
                    try:
                        remove('campo.png')
                    except FileNotFoundError:
                        pass
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONUP:
                    for boton in botones:
                        boton['on_click'] = False
                try:
                    Mag=float(mag.text)
                except ValueError:
                    Mag=float(0)
                    
                input_boxes[0].eventos(event)
                try:
                    VelY=float(vely.text)
                except ValueError:
                    VelY=float(0)
                    
                input_boxes[1].eventos(event)
                try:
                    VelX=float(velx.text)
                except ValueError:
                    VelX=float(0)
                    
                input_boxes[2].eventos(event)

            if botones[2]['on_click'] and click:

                if len(u)>1:
                    u=[carga((100,100),0)]
                    v=[]
                    if pot==True:
                        update_potencial=True
                    if camp==True:
                        update_campo=True

            if botones[3]['on_click'] and click:
                if len(u)>1:
                    if pot==True:
                        update_potencial=True
                    if camp==True:
                        update_campo=True
                    u.pop(-1)
            if botones[4]['on_click'] and click and paso:
                if n==0:
                    pot=True
                    update_potencial=True
                    update_campo=False
                    n=1
                elif n==1:
                    pot=False
                    update_potencial=False
                    n=0
            elif botones[5]['on_click'] and click:
                if l==0:
                    camp=True
                    update_campo=True
                    update_potencial=False
                    paso=False
                    l=1
                elif l==1:
                    camp=False
                    update_campo=False
                    paso=True
                    l=0
            world(v,u).update(botones,input_boxes,pot,update_potencial,camp,update_campo)
