import pygame,sys
from pygame.locals import *
import numpy as np
from Funciones import *
from textos import *
from Potencial import *
from Lineas_Campo import *
from Guardador import *
from os import remove
import os.path as path
pote=False
campe=False
class world:
    def __init__(self,ball,cargas,detector):
        global pote
        pygame.init()
        pygame.display.set_caption("Simulador Campo Electrico")
        programIcon = pygame.image.load('sprites\\proton.png')
        pygame.display.set_icon(programIcon)
        self.barra=False
        self.clock=pygame.time.Clock()
        self.ball=ball
        self.cargas=cargas
        self.detector=detector
        self.screen = pygame.display.set_mode((800, 600))
        self.tablero=pygame.image.load("pantallas\\Tab.png")
        self.line=pygame.image.load('sprites\\line.png')
        self.fuente= pygame.font.Font('fuentes\\DS-DIGIB.TTF', 30)
        self.window = pygame.display.get_surface()
        if pote==True:
            self.surf = pygame.transform.flip(pygame.image.load("potencial.png"),False,True)
            self.barra=True
        elif campe==True:
            self.surf = pygame.transform.flip(pygame.image.load("campo.png"),False,True)
            self.barra=False
        elif pote==False and campe==False:
            self.surf =pygame.image.load('pantallas\\fondo.png')
            self.barra=False
        self.surf=self.surf.convert()
        self.window.blit(self.surf, (0,0))

    def dibujar_botones(self,lista_botones):
        panel = pygame.transform.scale(self.tablero, [800, 600])
        line1=self.line
        line2=pygame.transform.rotate(self.line, 90)
        self.screen.blit(panel, [0, 0])
        if 15<pygame.mouse.get_pos()[1]<460 and 225<pygame.mouse.get_pos()[0]<775:
            self.screen.blit(line1, (225,pygame.mouse.get_pos()[1]))
            self.screen.blit(line2, (pygame.mouse.get_pos()[0],458))
        if self.barra:
            self.window.blit(pygame.image.load("barra.png"), (240,471))

        for boton in lista_botones:
            if boton['on_click']:
                self.screen.blit(boton['imagen_pressed'], boton['rect'])
            else:
                self.screen.blit(boton['imagen'], boton['rect'])
    def update(self,lista_botones,input_boxes,POT,update_potencial,CAMP,update_campo,GUARDAR):
        self.clock.tick(10)   
        global pote
        global campe


        for o in self.ball :
            self.screen.blit(self.surf,o.pos,o.pos)
            o.move(self.cargas)
        b=0
        if GUARDAR:
            while path.exists('Creaciones\Campo_y_Potencial_{:}.png'.format(b)):
                b=b+1
            imagen_toda(self.cargas,b)
            
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
                o.col(k)
                self.screen.blit(o.image,o.pos)
            
            campo_total=campo_total+carga.magnitud_campo(k,pygame.mouse.get_pos())
            potencial_total=potencial_total+carga.potencial(k,pygame.mouse.get_pos())
        for i in self.detector:
            if self.detector[0].campo_TOTAL(self.cargas)>0:
                i.detectar(self.cargas,op1=True)
            elif self.detector[0].campo_TOTAL(self.cargas)<0:
                i.detectar(self.cargas,op2=True)
            else:
                i.detectar(self.cargas,op3=True)
            self.screen.blit(i.imagen,i.pos)               

        if len(self.detector)==0:
            texto=self.fuente.render("{:.3f}".format(campo_total), 0, (0, 0, 0))
            texto2=self.fuente.render("{:.3f}".format(potencial_total), 0, (0, 0, 0))
            ejex=(pygame.mouse.get_pos()[0]/80)-2.91
            ejey=-(pygame.mouse.get_pos()[1]/80)+5.7
        else:
            texto=self.fuente.render("{:.3f}".format(self.detector[0].campo_TOTAL(self.cargas)), 0, (0, 0, 0))
            texto2=self.fuente.render("{:.3f}".format(self.detector[0].potencial_TOTAL(self.cargas)), 0, (0, 0, 0))
            ejex=((self.detector[0].pos[0]+17.5)/80)-2.91
            ejey=-((self.detector[0].pos[1]+17.5)/80)+5.7
        textposx=self.fuente.render("{:.2f}".format(ejex), 0, (255, 255, 255))
        textposy=self.fuente.render("{:.2f}".format(ejey), 0, (255, 255, 255))
        self.dibujar_botones(lista_botones)

        if 6.85>ejex>0 and 5.45>ejey>0 :
            self.screen.blit(texto, (20,243))
            self.screen.blit(texto2, (20,315))
            self.screen.blit(textposx, (650,499))
            self.screen.blit(textposy, (715,499))
        for box in input_boxes:
            box.pintar(self.screen)
        pygame.display.flip()
        
    def visual(pantalla1=False,pantalla2=False,pantalla3=False):
        mag = cajas_texto(13, 391, 195, 32)
        velx = cajas_texto(13, 460, 100, 32)
        vely = cajas_texto(112, 460, 95, 32)
        input_boxes = [mag, velx,vely]
        ELECTRON = pygame.image.load("sprites\\prueba.png")
        ELECTRON_PULSO = pygame.image.load("sprites\\PRUEBA_OPRIMIDO.png")
        CARGA = pygame.image.load("sprites\\CARGA.png")
        CARGA_PULSO = pygame.image.load("sprites\\CARGA_OPRIMIDO.png")
        NEW=pygame.image.load("sprites\\LIMPIAR.png")
        NEW_PULSO=pygame.image.load("sprites\\LIMPIAR_OPRIMIDO.png")
        ULTIMO=pygame.image.load("sprites\\return.png")
        ULTIMO_PULSO=pygame.image.load("sprites\\return_press.png")
        COZZETTI=pygame.image.load("sprites\\POT.png")
        MAXIMO_COZZETTI=pygame.image.load("sprites\\POT_PRESS.png")
        CAMP=pygame.image.load("sprites\\CAMP.png")
        CAMP_PRESS=pygame.image.load("sprites\\CAMP_PRESS.png")
        SAVE=pygame.image.load("sprites\\save.png")
        SAVE_PRESS=pygame.image.load("sprites\\save_press.png")
        DET=pygame.image.load("sprites\\detector.png")
        EQUIS=pygame.image.load("sprites\\equis.png")
        EQUISP=pygame.image.load("sprites\\equisp.png")
        v=[]
        u=[carga((100,100),0)]
        botones = []
        r_boton_1_1 = ELECTRON.get_rect()
        r_boton_1_1.topleft = [35, 135]
        botones.append({ 'imagen': ELECTRON, 'imagen_pressed': ELECTRON_PULSO, 'rect': r_boton_1_1, 'on_click': False})
        r_boton_2_2 = CARGA.get_rect()
        r_boton_2_2.topleft = [138, 135]
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
        r_boton_7_7 = SAVE.get_rect()
        r_boton_7_7.topleft = [642, 536]
        botones.append({ 'imagen': SAVE, 'imagen_pressed': SAVE_PRESS, 'rect': r_boton_7_7, 'on_click': False})
        r_boton_8_8 = DET.get_rect()
        r_boton_8_8.topleft = [97, 135]
        botones.append({ 'imagen': DET, 'imagen_pressed': DET, 'rect': r_boton_8_8, 'on_click': False})
        r_boton_9_9 = EQUIS.get_rect()
        r_boton_9_9.topleft = [97, 175]
        botones.append({ 'imagen': EQUIS, 'imagen_pressed': EQUISP, 'rect': r_boton_9_9, 'on_click': False})              
        
        b=None
        VelX=0
        VelY=0
        Mag=0
        pot=False
        camp=False
        n=0
        l=0
        paso=True
        Ejecucion=True
        
        if pantalla1:
            p=np.arange(0,2*np.pi,np.pi/10)
            for i in p:
                X=100*np.cos(i)+500
                Y=100*np.sin(i)+200
                u=u+[carga((X,Y),0)]
                x=50*np.cos(i)+510
                y=50*np.sin(i)+210
                v=v+[ball((x,y),(0,0),(10*(-1)**(i*(10/np.pi))))]
        
        elif pantalla2:
            p=np.arange(150,850,30)
            for i in p:
                u=u+[carga((i,300),15)]
                u=u+[carga((i,100),-15)]
        elif pantalla3:
            u=u+[carga((400,250),100),carga((450,300),-100)]
            
        det=[]

        
        while Ejecucion==True:
            update_potencial=False
            update_campo=False
            GUARDAR=False
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    
                    mouse = event.pos
                    for boton in botones:
                        boton['on_click'] = boton['rect'].colliderect([mouse[0], mouse[1], 1, 1])
                    click = True
                    if botones[0]['on_click'] and click:
                        b=1
                    if botones[1]['on_click'] and click:
                        b=0
                    if botones[7]['on_click'] and click:
                        b=2                     
                    mouse=pygame.mouse.get_pos()
                    if b==1:
                        if pygame.mouse.get_pos()[0]>225 and pygame.mouse.get_pos()[1]<460:
                            v=v+[ball((mouse[0]-10,mouse[1]-10),(VelX,-VelY),Mag)]
                    elif b==0:
                        if pygame.mouse.get_pos()[0]>225 and pygame.mouse.get_pos()[1]<460:
                            u=u+[carga((mouse[0]-20,mouse[1]-20),Mag)]
                            if botones[4]['on_click'] and click or pot==True:
                                update_potencial=True
                                update_campo=False
                            elif botones[5]['on_click'] and click or camp==True:
                                update_campo=True
                                update_potencial=False
                    elif b==2:
                        if pygame.mouse.get_pos()[0]>225 and pygame.mouse.get_pos()[1]<460:
                            det=[detector((mouse[0]-17,mouse[1]-17))]
                            
                 
                                
                            
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        Ejecucion=False
                        

                if event.type==QUIT:
                    try:
                        remove('potencial.png')
                    except FileNotFoundError:
                        pass
                    try:
                        remove('campo.png')
                    except FileNotFoundError:
                        pass
                    try:
                        remove('barra.png')
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
                v=[]
                det=[]
                if len(u)>1:
                    u=[carga((100,100),0)]
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
            if botones[6]['on_click'] and click:
                GUARDAR=True
            if botones[8]['on_click'] and click:
                det=[]
          
                
            


            world(v,u,det).update(botones,input_boxes,pot,update_potencial,camp,update_campo,GUARDAR)
