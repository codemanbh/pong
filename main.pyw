import pygame , random
from components.screen import screen , text , close , w, h , clock , background  , text_1 , text_2 , text_3
from components.ball import ball , Ball
from components.player import  p1 , p2
from components.line import line1

running = True
firstStart = True
score = 0

while True:
    clock.tick(120)
    screen.blit(background , (0,0))
    screen.blit(ball.surf , ball.rect ) 
    screen.blit(p1.surf, p1.rect) 
    screen.blit(p2.surf, p2.rect) 
    score_text = text( score , 30 ,h/5, w- w/7)
    screen.blit(score_text.surf , score_text.rect  )
    close()

    keys = pygame.key.get_pressed()
    if firstStart:
        screen.blit(text_3.surf , text_3.rect)
        if keys[pygame.K_RETURN]:
            firstStart = False

    if not firstStart:
        if running:
            p1.playerMovement()
            ball.ballMovement()

            if p1.rect.colliderect(ball.rect):
                ball.direction = 'l'
                ball.changeAngle()
                score += 1

            if p2.rect.colliderect(ball.rect) :
                ball.direction = 'r'
                ball.changeAngle()

            if ball.rect.x > w:
                running = False
            p2.rect.centery = ball.rect.centery
        else:
            screen.blit(text_1.surf , text_1.rect)
            screen.blit(text_2.surf ,text_2.rect)

            if keys[pygame.K_RETURN]:
                score = 0
                p1.rect.centery = h/2 
                ball = Ball()
                running = True

    pygame.display.flip()