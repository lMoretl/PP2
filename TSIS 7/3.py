import pygame
import time
pygame.init()
runned=True
Height,Width=800,500
x,y=50,50
dx,dy=0,0
Delta=20
clock=pygame.time.Clock()
screen=pygame.display.set_mode((Height,Width))
pygame.display.set_caption("Katarinai,nemurinai,Toroimenoai,anatano")
while runned:
    screen.fill((255,255,255))
    pressed=pygame.key.get_pressed()
    if pressed[pygame.K_DOWN] and pressed[pygame.K_LEFT]:
        dx=-Delta
        dy=Delta
    elif pressed[pygame.K_LEFT] and pressed[pygame.K_UP]:
        dx=-Delta
        dy=-Delta
    elif pressed[pygame.K_RIGHT] and pressed[pygame.K_UP]:
        dx=Delta
        dy=-Delta
    elif pressed[pygame.K_RIGHT] and pressed[pygame.K_DOWN]:
        dx=Delta
        dy=Delta
    elif pressed[pygame.K_UP]:
        dx=0
        dy=-Delta
    elif pressed[pygame.K_DOWN]:
        dx=0
        dy=Delta
    elif pressed[pygame.K_LEFT]:
        dx=-Delta
        dy=0
    elif pressed[pygame.K_RIGHT]:
        dx=Delta
        dy=0
    else:
        dx=0
        dy=0
    x=x+dx
    y=y+dy
    if not ((Height/2+x-25>=0 and Height/2+x+25<=Height) and (Width/2+y-25>=0 and Width/2+y+25<=Width)):
        x=x-dx
        y=y-dy
    pygame.draw.circle(screen,(255,0,0),(Height/2+x,Width/2+y),25,0)
    time.sleep(0.07)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            runned=False
    pygame.display.flip()
    clock.tick(60)