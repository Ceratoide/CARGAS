import pygame,sys
from pygame.locals import *
import numpy as np
from Funciones import *
from Menu import *

class world:
    def __init__(self,ball,cargas):
        
        pygame.init()
        pygame.display.set_caption("Simulador Campo Electrico")
        self.clock=pygame.time.Clock()
        self.ball=ball
        self.cargas=cargas

        self.BLANCO = (255, 255, 255)

        self.screen = pygame.display.set_mode((800, 600))
        bg_image = pygame.image.load("fondo-pared-ladrillos.jpg")
        self.bg_image = bg_image.convert()
        self.screen.blit(self.bg_image,(0,0))
        self.tablero=pygame.image.load("Tab.png")
    def dibujar_botones(self,lista_botones):
        panel = pygame.transform.scale(self.tablero, [800, 600])
        self.screen.blit(panel, [0, 0])
        for boton in lista_botones:
            if boton['on_click']:
                self.screen.blit(boton['imagen_pressed'], boton['rect'])
            else:
                self.screen.blit(boton['imagen'], boton['rect'])
    def update(self,lista_botones):
        self.clock.tick(10)   
        for o in self.ball :
            self.screen.blit(self.bg_image,o.pos,o.pos)
        for i in range(len(self.ball)):
            for j in range(len(self.cargas)):
                self.ball[i].col(self.cargas[j])
        for k in self.cargas:
            self.screen.blit(k.image,k.pos)
            for o in self.ball:
                
                o.acel=o.fuerza(k)
                o.move(k)
                self.screen.blit(o.image,o.pos)
        self.dibujar_botones(lista_botones)
        pygame.display.flip()
    def visual():
        ELECTRON = pygame.image.load("prueba.png")
        ELECTRON_PULSO = pygame.image.load("PRUEBA_OPRIMIDO.png")
        CARGA = pygame.image.load("CARGA.png")
        CARGA_PULSO = pygame.image.load("CARGA_OPRIMIDO.png")
        c=ball((500,100),(1,0),20)
        g=ball((0,200),(10,2),-20)
        h=ball((0,250),(1.5,0),-5)
        k=ball((300,400),(0,0),10)
        e=carga((350,250),-20)
        f=carga((600,250),-20)
        l=carga((550,500),50)
        n=carga((550,100),20)
        p=[]
        b=[]
        for i in range(-200,1000,20):
            p=p+[carga((i,500),10)]
            p=p+[carga((i,0),-10)]
            b=b+[ball((i,400),(0,0),15)]
            b=b+[ball((i,200),(0,0),-15)]
        #w=world([v],p)
        #w=world([g,k,c,v],[e])
        #w=world(b,[e])
        cargas=[e,f,l,n]
        
        #PRUEBA VELOCIDAD ORBITAL
        PO=ball((0,500),(1.5,0),-5)
        CO=carga((400,300),40)
        #w=world([PO],[CO])
        v=[]
        u=[]
        botones = []
        r_boton_1_1 = ELECTRON.get_rect()
        r_boton_1_1.topleft = [40, 135]
        botones.append({ 'imagen': ELECTRON, 'imagen_pressed': ELECTRON_PULSO, 'rect': r_boton_1_1, 'on_click': False})
        r_boton_2_2 = ELECTRON.get_rect()
        r_boton_2_2.topleft = [130, 135]
        botones.append({ 'imagen': CARGA, 'imagen_pressed': CARGA_PULSO, 'rect': r_boton_2_2, 'on_click': False})
        
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


         
                

            world(v,u).update(botones)



