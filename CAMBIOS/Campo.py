import pygame,sys
from pygame.locals import *
import numpy as np
from Funciones import *
class world:
    def __init__(self,ball,cargas):
        
        pygame.init()
        pygame.display.set_caption("Simulador Campo Electrico")
        self.clock=pygame.time.Clock()
        self.ball=ball
        self.cargas=cargas
        self.screen = pygame.display.set_mode((800, 600))
        
    def update(self):
        self.clock.tick(10)    
        

        for i in range(len(self.ball)):
            for j in range(len(self.cargas)):
                self.ball[i].col(self.cargas[j])
        for k in self.cargas:
            self.screen.blit(k.image,k.pos)
            for o in self.ball:
                
                o.acel=o.fuerza(k)
                o.move(k)
                self.screen.blit(o.image,o.pos)
        
        pygame.display.flip()
def main():
    c=ball((500,100),(1,0),20)
    g=ball((0,200),(10,2),-20)
    v=ball((0,250),(1.5,0),-5)
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
    w=world(b,[e,f,l,n])




    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    MENU().otra_pantalla()

                    

            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        

        w.update()
main()