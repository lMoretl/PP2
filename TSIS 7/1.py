import pygame
import math
import datetime
def hell(a,font):
    x,y=0,0
    if abs(a)>360:
        a+=360
    if abs(a)<=90:
        pass
    elif abs(a)>90 and abs(a)<=180:
        deg=(a-90)/57.2958
        x+=math.sin(deg)*font
    elif abs(a)<=270 and abs(a)>=180:
        deg=(a-180)/57.2958
        y-=math.sin(deg)*font
        x+=math.cos(deg)*font
    elif abs(a)<=360 and abs(a)>=270:
        deg=(a-270)/57.2958
        y-=math.cos(deg)*font
    return x,y
pygame.init()

clock=pygame.time.Clock()
height,width=500,500
font,font1,font2=220,220,125
screen=pygame.display.set_mode((height,width))
pygame.display.set_caption("mickey mouse clock")

image=pygame.image.load("C:/Users/User/Desktop/python/images/better.png")
reimage=pygame.transform.scale(image,(height+25,width))

hands=pygame.image.load("C:/Users/User/Desktop/python/images/hands.png")
resecondhands=pygame.transform.scale(hands,(font,10))
reminutehands=pygame.transform.scale(hands,(font1,20))
rehourhands=pygame.transform.scale(hands,(font2,30))

runned=True

while runned:
    hours=datetime.datetime.now().hour
    if hours>12:
        hours-=12

    a=-270+datetime.datetime.now().second*-6
    b=-270+datetime.datetime.now().minute*-6
    c=-270+hours*-30

    screen.fill((255,255,255))

    screen.blit(reimage,(0,0))

    rotatedimage=pygame.transform.rotate(resecondhands,a)
    screen.blit(rotatedimage,(height/2-hell(a,font)[0],width/2-hell(a,font)[1]-5))

    rotatedsecondhands=pygame.transform.rotate(reminutehands,b)
    screen.blit(rotatedsecondhands,(height/2-hell(b,font1)[0],width/2-hell(b,font1)[1]-10))

    rotatedminutehands=pygame.transform.rotate(rehourhands,c)
    screen.blit(rotatedminutehands,(height/2-hell(c,font2)[0],width/2-hell(c,font2)[1]-15))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            runned=False
    pygame.display.flip()
    clock.tick(20)