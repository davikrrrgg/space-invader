import pygame
import time
import os
import random
import random

sfondo=pygame.image.load("assets/background-black.png")
pg=pygame.image.load("assets/pixel_ship_yellow.png")
pg_laser=pygame.image.load("assets/pixel_laser_yellow.png")
bot1=pygame.image.load("assets/pixel_ship_red_small.png")
bot_laser=pygame.image.load("assets/pixel_laser_red.png")


pygame.init()

music= pygame.mixer.Sound(("sounds/space-invaders-classic-arcade-game-116826.mp3"))
shot= pygame.mixer.Sound(("sounds/shot.mp3"))
level_up= pygame.mixer.Sound(("sounds/level_up.mp3"))


screen=pygame.display.set_mode((400,400))

def start():

    pygame.mixer.Sound.play(music)

    t=0

    m=[
        [20,20,999,-30,True,True,bot1,t,bot_laser,False]
    ]
    
    lvl=1
    ricarica=True
    laser=False
    i=0
    ys=0
    ys2=-400
    x=160
    y=300
    xl=999
    yl=999


    FONT = pygame.font.SysFont('arial', 25, bold=True)
    livello_txt=FONT.render("Livello: ", True, (255,255,255))

    def disegna(i):
        lvl_txt=FONT.render(str(lvl), True, (255,255,255))
    
        screen.blit(sfondo,(0,ys+i))
        screen.blit(sfondo,(0,ys2+i))
        screen.blit(livello_txt, (0,0))
        screen.blit(lvl_txt, (110,0))
        screen.blit(pg,(x,y))
        screen.blit(pg_laser, (xl,yl))
                                        #disegno bot
        u=0
        while u<(lvl):
            flag_bot=False
            if (m[u][4]==True):
                xb=m[u][0]
                yb=m[u][1]
                xbl=m[u][2]
                xbl=m[u][3]
                screen.blit(bot_laser, (m[u][2],m[u][3]))
                screen.blit((m[u][6]), (xb,yb))
                if m[u][5]==True:
                    m[u][0]=m[u][0]+1
                    if m[u][0]>340:
                        m[u][5]=False
                else:
                    m[u][0]=m[u][0]-1
                    if m[u][0]<-10:
                        m[u][5]=True


            u=u+1

    def aggiorna():
        pygame.display.update()
        pygame.time.Clock().tick(250)



    def pausa():
        FONT = pygame.font.SysFont('arial', 40, bold=True)
        pausa_txt=FONT.render("Pausa", True, (0,255,0))
        screen.blit(pausa_txt, (130,150))
        aggiorna()
        a=True
        while a==True:
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    a=False
                if event.type== pygame.QUIT:
                    pygame.quit()
                    os.sys.exit()
            pygame.time.delay(100)


    while True:
        for event in pygame.event.get():
                                                #esci/pausa
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    pausa()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_w:
                    if ricarica==True:
                        xl=x+30
                        yl=y
                        pygame.mixer.Sound.play(shot)

                        laser=True
            if event.type== pygame.QUIT:
                pygame.quit()
                os.sys.exit()
                                    #comandi

        key=pygame.key.get_pressed()
        if key[pygame.K_a]:
            if x>-5:
                x=x-3
        if key[pygame.K_d]:
            if x<338:
                x=x+3
                                    #laser pg

        if laser==True:
            yl=yl-5
            ricarica=False
            if yl<0:
                laser =False
                ricarica=True
                yl=999


                                #collisioni
        r=0
        while r!=lvl:
            if xl>m[r][0] and xl< m[r][0]+50 and yl>m[r][1] and yl<m[r][1]+50:
                m[r][4]=False
                
            r=r+1


        r=0                        #incremento livello e controllo di livello in corso
        while r<lvl:
            if m[r][4]==True:
                break
            else:
                if r==lvl-1:
                    if(lvl>3 and lvl<6):                    #divisioni nelle linee in y
                        v=[20,60,999,-30,True,True,bot1,0.1,False]
                    else:
                        v=[20,20,999,-30,True,True,bot1,0.1,bot_laser,False]
                    if(lvl>6):
                        v=[20,100,999,-30,True,True,bot1,0.1,bot_laser,False]

                    m.append(v)
                    z=0
                    while z!=lvl:
                        m[z][4]=True
                        z=z+1
                    xl=999
                    pygame.mixer.Sound.play(level_up)
                    lvl=lvl+1

                    z=1                         #controllo e reset delle posizioni in x
                    while (z != lvl-1):
                        m[z][0]=m[z-1][0]+50
                        z=z+1

                    break

            r=r+1


        r=0                                    #laser bot
        while(r<lvl):
    
            if(m[r][7]<10):
                m[r][7]=m[r][7]+0.1
            
            if m[r][7]>9.8:
                m[r][7]=0.0
            if m[r][7]>8:
                m[r][9]=True
                m[r][2]=m[r][0]-14
                m[r][3]=m[r][1]+10
                break
                

            r=r+1
        r=0
        while(r<lvl):
            if(m[r][9]==True):
                m[r][3]=m[r][3]+10
            if(m[r][3]>390):
                m[r][3]=-1000
                m[r][9]=False
            r=r+1
        


                #cicl sfondo

        if i>400:
            i=0
        i=i+1


        disegna(i)
        aggiorna()

start()