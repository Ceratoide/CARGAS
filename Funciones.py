import pygame,sys
from pygame.locals import *
import numpy as np

class carga(pygame.sprite.Sprite):
    def __init__(self,pos,magnitud):
        if magnitud<0:
            self.image=pygame.image.load("sprites\\electron.png")
        if magnitud>0:
            self.image=pygame.image.load("sprites\\proton.png") 
        if magnitud==0:
            self.image=pygame.image.load("sprites\\neutro.png")
        px,py=pos
        self.pos=self.image.get_rect().move(px,py)
        self.magnitud=magnitud
        self.mask=pygame.mask.from_surface(self.image)
        self.rect=self.pos
        self.pix=1/80
        self.k=8.9#Para dejar las cargas en nuC
    def campo(self, punto):
        k=self.k
        campo=[0,0]

        dist=np.sqrt(((punto[0]-self.pos[0]-20)*self.pix)**(2)+((punto[1]-self.pos[1]-20)*self.pix)**(2))**3
        if dist.all()!=0:
            campo[0]=(self.magnitud*k*(punto[0]-self.pos[0]-20)*self.pix)/dist
            campo[1]=(self.magnitud*k*(punto[1]-self.pos[1]-20)*self.pix)/dist
            return (campo[0],campo[1])
        else:
            return(0,0)
    def magnitud_campo(self,punto):
        k=self.k
        distancia=np.sqrt(((punto[0]-self.pos[0]-20)*self.pix)**(2)+((punto[1]-self.pos[1]-20)*self.pix)**(2))
        if distancia.all()!=0:
            norma=(self.magnitud*k)/distancia**2
            return norma
        else:
            return 0
    def potencial(self,punto):
        k=self.k
        distancia=np.sqrt(((punto[0]-self.pos[0]-20)*self.pix)**(2)+((punto[1]-self.pos[1]-20)*self.pix)**(2))
        if distancia.all()!=0:
            potencial=(self.magnitud*k)/distancia
            return potencial
        else:
            return 0
   
class ball(pygame.sprite.Sprite):
    
    def __init__(self,pos, vel,magnitud,acel=(0,0)):
        if magnitud<0:
            self.image=pygame.image.load("sprites\\electronchikito.png")
        if magnitud>0:
            self.image=pygame.image.load("sprites\\protonchikito.png") 
        if magnitud==0:
            self.image=pygame.image.load("sprites\\neutrochikito.png")
        px,py=pos
        self.pos=self.image.get_rect().move(px,py)
        self.vel=np.array(vel)
        self.acel=np.array(acel)
        self.magnitud=magnitud
        self.mask=pygame.mask.from_surface(self.image)
        self.rect=self.pos
        self.pix=1/80
    def fuerza(self,CARGA):
        fuerza=[0,0]
        if carga.campo(CARGA,self.pos)==False:
            return (0,0)
        fuerza[0]=self.magnitud*carga.campo(CARGA,self.pos)[0]
        fuerza[1]=self.magnitud*carga.campo(CARGA,self.pos)[1]
        if self.col(CARGA)==True:
            return (0,0)
        return (fuerza[0]*(self.pix/100),fuerza[1]*(self.pix/100))
        
            

    def move(self,o):
        FUERZA=[0,0]
        for i in o:
            FUERZA[0]=FUERZA[0]+self.fuerza(i)[0]
            FUERZA[1]=FUERZA[1]+self.fuerza(i)[1]            
        vx,vy=self.vel[0]*(self.pix)*10,self.vel[1]*(self.pix)*10
        
        ax,ay=self.acel
        self.vel=self.vel+(FUERZA[0],FUERZA[1])
        self.pos = self.pos.move(vx,vy)
        


        self.rect=self.pos

        
    def col(self, o):
        
        if pygame.sprite.collide_mask(self,o) is None:
            return
            
        npspos=np.array((self.pos.x,self.pos.y))
        npopos=np.array((o.pos.x,o.pos.y))
            
        colision = (npspos-npopos)
        dist=np.sqrt(np.dot(colision, colision))
        if dist!=0:
            colision=colision/dist
        if o.magnitud>=0 and self.magnitud<=0 :
            self.vel = self.vel - self.vel
            return True
        elif o.magnitud<=0 and self.magnitud>=0:
            self.vel = self.vel - self.vel
            return True
        
        return 
    
class detector(pygame.sprite.Sprite):
    def __init__(self,pos):
        self.image=pygame.image.load('sprites\\detector.png')
        self.image_pos=pygame.image.load('sprites\\detector_pos.png')
        self.image_neg=pygame.image.load('sprites\detector_neg.png')
        self.imagen=self.image
        px,py=pos
        self.pos=self.imagen.get_rect().move(px,py)
        self.mask=pygame.mask.from_surface(self.imagen)
        self.rect=self.pos
        self.campototal=0
        self.potencialtotal=0
    def detectar(self,CARGA):
        
        for i in CARGA:
            self.campototal=self.campototal+i.magnitud_campo(self.pos)
            self.potencialtotal=self.potencialtotal+i.potencial(self.pos)
        if self.campototal>0:
            self.imagen=self.image_pos
        elif self.campototal<0:
            self.imagen=self.image_neg
        else:
            self.imagen=self.image
    def campo_TOTAL(self,CARGA):
        CAMPO=0
        for i in CARGA:
            CAMPO=CAMPO+i.magnitud_campo((self.pos[0]+17.5,self.pos[1]+17.5)) 
        return CAMPO
    def potencial_TOTAL(self,CARGA):
        POT=0
        for i in CARGA:
            POT=POT+i.potencial((self.pos[0]+17.5,self.pos[1]+17.5)) 
        return POT
        
            
        

        
