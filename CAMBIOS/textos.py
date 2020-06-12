import pygame 
pygame.init()
COLOR_INACTIVE = pygame.Color('black')
COLOR_ACTIVE = pygame.Color('blue')
FONT = pygame.font.Font('DS-DIGIB.TTF', 25)


class cajas_texto:

    def __init__(self, x, y, w, h, text='0'):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False
    
    def eventos(self, event):
    
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    if self.text!='':
                        self.text=float(self.text)
                    self.text = '0'

                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text = self.text+ event.unicode
                self.txt_surface = FONT.render(self.text, True, self.color)
       




    def pintar(self, screen):
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(screen, self.color, self.rect, 2)
  





