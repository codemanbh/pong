import pygame
# from screen import w , h
pygame.font.init()

w = 900
h = 500

screen = pygame.display.set_mode([w, h])
screen.fill("Black")
pygame.display.set_caption('Pong')
background = pygame.Surface((w,h))
background.fill("Black")

clock = pygame.time.Clock()
class text:
    def __init__(self , content , size , hight = h/4 , width =  w/2):
        decay_font = pygame.font.Font('Minecraft.ttf', size)
        self.surf = decay_font.render(str(content) , True , 'white')
        self.ruct = self.surf
        self.rect = self.surf.get_rect()
        self.rect.centerx = width
        self.rect.centery = hight



text_1 = text("game over !!" , 70)
text_2 = text("press enter to replay" , 30 , h/3)
text_3 = text("press enter to start" , 30)

def close():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()