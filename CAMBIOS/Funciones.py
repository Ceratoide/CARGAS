import pygame,sys
from pygame.locals import *
import numpy as np

class carga(pygame.sprite.Sprite):
    def __init__(self,pos,magnitud):
        if magnitud<0:
            self.image=pygame.image.load("electron.png")
        if magnitud>0:
            self.image=pygame.image.load("proton.png") 
        if magnitud==0:
            self.image=pygame.image.load("Neutro.png")
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
            self.image=pygame.image.load("electronchikito.png")
        if magnitud>0:
            self.image=pygame.image.load("protonchikito.png") 
        if magnitud==0:
            self.image=pygame.image.load("Neutrochikito.png")
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
        
            

    def move(self,CARGA):
        if CARGA.pos[0]==self.pos[0] and CARGA.pos[1]==self.pos[1]:
            self.vel=self.vel-self.vel
        vx,vy=self.vel[0]*(self.pix)*10,self.vel[1]*(self.pix)*10
        ax,ay=self.acel
        self.vel=self.vel+self.acel
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
