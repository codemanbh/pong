import pygame , random
from screen import w , h

class Line:
    def __init__(self ):
        self.player = pygame.Surface((w,1))
        self.player.fill([30,30,30])
        self.surf = self.player
        self.rect = self.player.get_rect()
        self.rect.y = 0
        self.rect.x = 0
        self.rect.centery = 0
        self.rect.x = 0
        self.move_speed  = 6





line1 = Line()