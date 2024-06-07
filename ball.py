import pygame , random 
from math import cos , sin
from screen import w ,h

class Ball:
    def __init__(self):
        self.ball =  pygame.Surface((10,10))
        self.ball.fill('Red')
        self.rect = self.ball.get_rect()
        self.surf = self.ball
        self.rect.x = w/2
        self.rect.y = h/2
        self.direction = random.choice(['r','l'])
        self.angle = 0
        self.speed = 7
        self.range = range(2,5)

    def ballMovement(self):
        if self.rect.y < 0 or self.rect.y > h-10 :
            self.angle = self.angle * -1

        self.rect.y += self.angle
        if self.direction == 'r':
            self.rect.x += self.speed*cos(0)

        elif self.direction == 'l':
            self.rect.x -= self.speed
        
        if self.rect.x > w:
            print('lose')

    def changeAngle(self):
        self.angle = random.choice(self.range) * random.choice([1,-1])
        

ball = Ball()