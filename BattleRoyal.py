import pygame
pygame.init()




# Main Peremennie
winw=640
winh=640
clock=pygame.time.Clock()

run=True

win=pygame.display.set_mode((winw,winh))
pygame.display.set_caption("Tiny Battle Royale")

bg=pygame.image.load('background.jpg')
dblock=pygame.image.load('deathblock.png')
dcount=-100
dcount1=-1
dcount2=0
dblocks=[]
dblim=0
dbnumber=-1
#bullet
bulletsprite=[pygame.image.load('bullet1.png'),pygame.image.load('bullet2.png'),pygame.image.load('bullet3.png')]
bulletlistsq=0
bulleta=20
bulletspeed=15
shootcd=0
shootcdb=False
leftbullets=[]
leftbulletsx=[]
leftbulletsy=[]
rightbullets=[]
rightbulletsx=[]
rightbulletsy=[]
upbullets=[]
upbulletsx=[]
upbulletsy=[]
downbullets=[]
downbulletsx=[]
downbulletsy=[]
# player var-s
spritecondition = 0
playersprites=[pygame.image.load('player_unit1.png'),pygame.image.load('player_unit2.png'),pygame.image.load('player_unit3.png'),pygame.image.load('player_unit4.png'),pygame.image.load('player_unit5.png'),pygame.image.load('player_unit6.png')]
playerh=40
playerw=40
pspeed=10
movup=False
movdown=False
movright=False
movleft=False



class player:
    palive = True
    spritecondition=int()
    def getx(self,argx):
        self.xplayer=argx
    def gety(self,argy):
        self.yplayer=argy
    def draw(self):
        if self.palive:
            self.spritecondition += 1
            win.blit(playersprites[self.spritecondition // 5], (self.xplayer, self.yplayer))
            if self.spritecondition == 29:
                self.spritecondition = 0


myplayer=player()
myplayer.gety(0)
myplayer.getx(0)

class deathblock:
    argx = int()
    argy = int()
    def get_arg(self , arg1, arg2):
        self.argx=arg1
        self.argy=arg2
        self.args=True
    def draw(self):
        win.blit(dblock, (self.argx, self.argy))
        for plyr in [myplayer]:
            if (plyr.xplayer>=self.argx and plyr.xplayer<=self.argx+40 and plyr.yplayer>=self.argy and plyr.yplayer<=self.argy+40) \
                    or (plyr.xplayer+playerw>=self.argx and plyr.xplayer+playerw<=self.argx+40 and plyr.yplayer>=self.argy and plyr.yplayer<=self.argy+40) \
                    or (plyr.xplayer + playerw >= self.argx and plyr.xplayer + playerw <= self.argx + 40 and plyr.yplayer+playerh >= self.argy and plyr.yplayer+playerh <= self.argy + 40) \
                    or (plyr.xplayer >= self.argx and plyr.xplayer <= self.argx + 40 and plyr.yplayer+playerh >= self.argy and plyr.yplayer+playerh <= self.argy + 40):
                plyr.palive = False
class bullet:
    spritecondition=0
    def setposition(self, arg1, arg2):
        self.xbullet=arg1
        self.ybullet=arg2
    def draw(self):
        self.spritecondition+=1
        if self.spritecondition==3:
            self.spritecondition=0
        win.blit(bulletsprite[self.spritecondition], (self.xbullet, self.ybullet))
        for plyr in [myplayer]:
            if (plyr.xplayer>=self.xbullet and plyr.xplayer<=self.xbullet+20 and plyr.yplayer>=self.ybullet and plyr.yplayer<=self.ybullet+20) \
                    or (plyr.xplayer+playerw>=self.xbullet and plyr.xplayer+playerw<=self.xbullet+20 and plyr.yplayer>=self.ybullet and plyr.yplayer<=self.ybullet+20) \
                    or (plyr.xplayer + playerw >= self.xbullet and plyr.xplayer + playerw <= self.xbullet + 20 and plyr.yplayer+playerh >= self.ybullet and plyr.yplayer+playerh <= self.ybullet + 20) \
                    or (plyr.xplayer >= self.xbullet and plyr.xplayer <= self.xbullet + 20 and plyr.yplayer+playerh >= self.ybullet and plyr.yplayer+playerh <= self.ybullet + 20) \
                    or (plyr.xplayer + playerw//2 >= self.xbullet and plyr.xplayer + playerw//2 <= self.xbullet + 20 and plyr.yplayer + playerh >= self.ybullet and plyr.yplayer + playerh <= self.ybullet + 20) \
                    or (plyr.xplayer + playerw >= self.xbullet and plyr.xplayer + playerw <= self.xbullet + 20 and plyr.yplayer + playerh//2  >= self.ybullet and plyr.yplayer + playerh//2  <= self.ybullet + 20) \
                    or (plyr.xplayer >= self.xbullet and plyr.xplayer <= self.xbullet + 20 and plyr.yplayer + playerh//2 >= self.ybullet and plyr.yplayer + playerh//2 <= self.ybullet + 20) \
                    or (plyr.xplayer +playerw//2 >= self.xbullet and plyr.xplayer +playerw//2 <= self.xbullet + 20 and plyr.yplayer >= self.ybullet and plyr.yplayer <= self.ybullet + 20):
                plyr.palive = False




#Risovanie deistviy na ekrane
def DrawWindow():
    win.blit(bg, (0, 0))
    global bulletlistsq

    myplayer.draw()
    bulletlistsq = 0
    for i in range(len(leftbullets)):
        leftbullets[i-bulletlistsq].setposition(leftbulletsx[i-bulletlistsq],leftbulletsy[i-bulletlistsq])
        leftbulletsx[i-bulletlistsq]-=bulletspeed
        leftbullets[i-bulletlistsq].draw()
        if  leftbulletsx[i-bulletlistsq]<-40:
            del leftbulletsx[i-bulletlistsq]
            del leftbulletsy[i-bulletlistsq]
            del leftbullets[i-bulletlistsq]
            bulletlistsq += 1
    bulletlistsq = 0
    for i in range(len(rightbullets)):
        rightbullets[i-bulletlistsq].setposition(rightbulletsx[i-bulletlistsq],rightbulletsy[i-bulletlistsq])
        rightbulletsx[i-bulletlistsq]+=bulletspeed
        rightbullets[i-bulletlistsq].draw()
        if  rightbulletsx[i-bulletlistsq]>640:
            del rightbulletsx[i-bulletlistsq]
            del rightbulletsy[i-bulletlistsq]
            del rightbullets[i-bulletlistsq]
            bulletlistsq += 1
    bulletlistsq = 0
    for i in range(len(upbullets)):
        upbullets[i-bulletlistsq].setposition(upbulletsx[i-bulletlistsq],upbulletsy[i-bulletlistsq])
        upbulletsy[i-bulletlistsq]-=bulletspeed
        upbullets[i-bulletlistsq].draw()
        if  upbulletsy[i-bulletlistsq]<-40:
            del upbulletsx[i-bulletlistsq]
            del upbulletsy[i-bulletlistsq]
            del upbullets[i-bulletlistsq]
            bulletlistsq += 1
    bulletlistsq = 0
    for i in range(len(downbullets)):
        downbullets[i-bulletlistsq].setposition(downbulletsx[i-bulletlistsq],downbulletsy[i-bulletlistsq])
        downbulletsy[i-bulletlistsq]+=bulletspeed
        downbullets[i-bulletlistsq].draw()
        if  downbulletsx[i-bulletlistsq]<-40:
            del downbulletsx[i-bulletlistsq]
            del downbulletsy[i-bulletlistsq]
            del downbullets[i-bulletlistsq]
            bulletlistsq += 1
    for dd in range(0,dbnumber):
        dblocks[dd].draw()
    pygame.display.update()







#main cycle
while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False


    dcount+=1
    if dcount==5 and dcount2<16 and dbnumber<256:
        dcount=0
        dcount1+=1
        if dcount1==15-2*dblim:
            dblim+=1
            dcount2+=1
            dcount1=0
            dbnumber += 1
            dblocks.append(deathblock())
            dblocks[dbnumber].get_arg((dblim + dcount1) * 40, dcount2 * 40)
            dbnumber += 1
            dblocks.append(deathblock())
            dblocks[dbnumber].get_arg(600 - (dblim + dcount1) * 40, 600 - dcount2 * 40)
            dbnumber += 1
            dblocks.append(deathblock())
            dblocks[dbnumber].get_arg(600 - dcount2 * 40, (dblim + dcount1) * 40)
            dbnumber += 1
            dblocks.append(deathblock())
            dblocks[dbnumber].get_arg(dcount2 * 40, 600 - (dblim + dcount1) * 40)
        else:
            dbnumber += 1
            dblocks.append(deathblock())
            dblocks[dbnumber].get_arg((dblim+dcount1)*40, dcount2*40)
            dbnumber += 1
            dblocks.append(deathblock())
            dblocks[dbnumber].get_arg(600-(dblim+dcount1)*40, 600-dcount2*40)
            dbnumber += 1
            dblocks.append(deathblock())
            dblocks[dbnumber].get_arg(600-dcount2*40, (dblim+dcount1)*40)
            dbnumber += 1
            dblocks.append(deathblock())
            dblocks[dbnumber].get_arg(dcount2*40, 600-(dblim+dcount1)*40)

    if myplayer.palive:
        keys=pygame.key.get_pressed()

        if keys[pygame.K_w] and myplayer.yplayer>0:
            myplayer.gety(myplayer.yplayer-pspeed)

        if keys[pygame.K_s] and myplayer.yplayer<winh-playerh:
            myplayer.gety(myplayer.yplayer + pspeed)

        if keys[pygame.K_d] and myplayer.xplayer<winw-playerw:
            myplayer.getx(myplayer.xplayer + pspeed)

        if keys[pygame.K_a] and myplayer.xplayer>0:
            myplayer.getx(myplayer.xplayer - pspeed)




        shootcd+=1
        if shootcd==10:
            shootcdb=True
            shootcd=0
        if shootcdb:
            shootcd=0
            shootcdb=False
            if keys[pygame.K_i]:
                upbullets.append(bullet())
                upbulletsx.append(myplayer.xplayer+(playerw-bulleta)//2)
                upbulletsy.append(myplayer.yplayer-bulleta-1)
            elif keys[pygame.K_k]:
                downbullets.append(bullet())
                downbulletsx.append(myplayer.xplayer+(playerw-bulleta)//2)
                downbulletsy.append(myplayer.yplayer+playerh+1)
            elif keys[pygame.K_l]:
                rightbullets.append(bullet())
                rightbulletsx.append(myplayer.xplayer+playerw+1)
                rightbulletsy.append(myplayer.yplayer+(playerh-bulleta)//2)
            elif keys[pygame.K_j]:
                leftbullets.append(bullet())
                leftbulletsx.append(myplayer.xplayer-bulleta-1)
                leftbulletsy.append(myplayer.yplayer+(playerh-bulleta)//2)
    pygame.time.delay(10)
    DrawWindow()

pygame.quit()

