import pygame 



class cajas_texto:
    def __init__(self, x, y, w, h, text='0'):
        pygame.init()
        self.COLOR_INACTIVE = pygame.Color('black')
        self.COLOR_ACTIVE = pygame.Color('blue')
        self.FONT = pygame.font.Font('DS-DIGIB.TTF', 25)
        self.rect = pygame.Rect(x, y, w, h)
        self.color = self.COLOR_INACTIVE
        self.text = text
        self.txt_surface = self.FONT.render(text, True, self.color)
        self.active = False
    
    def eventos(self, event):
    
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
                self.text=''
                
            else:
                self.active = False
            self.color = self.COLOR_ACTIVE if self.active else self.COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.text = '0'
                    

                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                elif len(self.text)<6:
                    self.text = self.text+ event.unicode
                self.txt_surface = self.FONT.render(self.text, True, self.color)
       




    def pintar(self, screen):
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(screen, self.color, self.rect, 2)
  





