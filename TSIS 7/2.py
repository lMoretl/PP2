import pygame
import os
import time
pygame.mixer.init(44100, -16,1, 4096)
sound=pygame.mixer.Channel(1)


listofmusic=list(os.walk("C:/Users/User/Desktop/python/music"))
allpathes=list()
for path,dirs,files in listofmusic:
    for file in files:
        pathed=os.path.join("C:/Users/User/Desktop/python/music",file)
        allpathes.append(pathed)


screen=pygame.display.set_mode((500,500))
image=pygame.image.load("C:/Users/User/Desktop/python/images/playerinterface.jpg")
reimage=pygame.transform.scale(image,(500,500))
runned,i,playing,lefted=True,0,1,False
clock=pygame.time.Clock()

while runned:
    screen.blit(reimage,(0,0))
    
    buttonnext=pygame.key.get_pressed()
    try:
        if buttonnext[pygame.K_SPACE] and not pygame.mixer.music.get_busy() and playing:
            a=pygame.mixer.music.load(allpathes[i])
            pygame.mixer.music.play()
            i+=1
            time.sleep(0.5)
        elif buttonnext[pygame.K_RIGHT]:
            if lefted:
                i+=1
                lefted=False
            a=pygame.mixer.music.load(allpathes[i])
            pygame.mixer.music.play()
            i+=1
            time.sleep(0.5)
        elif buttonnext[pygame.K_LEFT]:
            i-=1
            lefted=True
            a=pygame.mixer.music.load(allpathes[i])
            pygame.mixer.music.play()
            time.sleep(0.5)
        elif buttonnext[pygame.K_SPACE] and pygame.mixer.music.get_busy() and playing:
            pygame.mixer.music.pause()
            playing=False
            time.sleep(0.5)
        elif buttonnext[pygame.K_SPACE] and (not playing):
            pygame.mixer.music.unpause()
            playing=True
            time.sleep(0.5)
    except:
        i=0
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            runned=False
    pygame.display.flip()