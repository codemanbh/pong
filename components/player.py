import pygame , random
from components.screen import w , h

class Player:
    def __init__(self , direction):
        self.player = pygame.Surface((20,150))
        self.player.fill('Green')
        self.surf = self.player
        self.rect = self.player.get_rect()
        self.rect.y = h/2
        self.rect.x = w/2
        self.rect.centery = h/2
        self.rect.x = w/2
        self.move_speed  = 6

        if direction == 'r':
            self.rect.x = w -30
        else:
            self.rect.x = 10

    def playerMovement(self):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                p1.rect.y -= self.move_speed
            if keys[pygame.K_DOWN]:
                p1.rect.y += self.move_speed




p1 = Player('r')
p2 = Player('l')