import pygame
import math
import random
pygame.init()

# UPRAVLENIE
# 1 player
# dvijenie-WASD
# strelba-TFGH
# 2 player
# dvijenie-OKL;
# strelba-NUM8NUM4NUM5NUM6


# Main Peremennie
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(1)
winw=640
winh=640
clock=pygame.time.Clock()

run=True

win=pygame.display.set_mode((winw,winh))
pygame.display.set_caption("Doka 2")
pygame.display.set_icon(pygame.image.load('icon.jpg'))
bg=pygame.image.load('background.jpg')
dblock=pygame.image.load('deathblock.png')
dcount=-200
dcount1=-1
dcount2=0
dblocks=[]
dblim=0
dbnumber=-1
# intro
introsprite=[pygame.image.load('intro1.jpg'),
              pygame.image.load('intro2.jpg'),
              pygame.image.load('intro3.jpg'),
              pygame.image.load('intro4.jpg'),
              pygame.image.load('intro5.jpg'),
              pygame.image.load('intro6.jpg'),
              pygame.image.load('intro7.jpg'),
              pygame.image.load('intro8.jpg'),
              pygame.image.load('intro9.jpg'),
              pygame.image.load('intro10.jpg'),
              pygame.image.load('intro11.jpg'),
              pygame.image.load('intro12.jpg'),
              pygame.image.load('intro_last.jpg'),]
intro_fr = 3
intro = True
intro_counter = 0
intro_end = False
# bullet
bulletsprite=[pygame.image.load('bullet1.png'),
              pygame.image.load('bullet2.png'),
              pygame.image.load('bullet3.png')]
bulletlistsq=0
bulleta=20
bulletspeed=15
shootcd=0
shootcdb=False
shootcd1=0
shootcdb1=False
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
playersprites=[pygame.image.load('player_unit1.png'),
               pygame.image.load('player_unit2.png'),
               pygame.image.load('player_unit3.png'),
               pygame.image.load('player_unit4.png'),
               pygame.image.load('player_unit5.png'),
               pygame.image.load('player_unit6.png')]
playerh=40
playerw=40
pspeed=10
player_destroing=[pygame.image.load('player_destroy2.png'),
                  pygame.image.load('player_destroy3.png'),
                  pygame.image.load('player_destroy4.png'),
                  pygame.image.load('player_destroy5.png')]
#upgrade
chainupgraders=[]
chainupcd=200
chainsawupimage=pygame.image.load('chainsawupgrade.png')
snakebuttonimage=pygame.image.load('snakebutton.png')
snakebuttons=[]
snakebuttoncd=100
armageddonimage=pygame.image.load('armageddon.png')
armageddons=[]
armageddoncd=200

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
        for plyr in [myplayer,myplayer1]:
            if plyr.palive and((plyr.xplayer>=self.xbullet and plyr.xplayer<=self.xbullet+20 and plyr.yplayer>=self.ybullet and plyr.yplayer<=self.ybullet+20) \
                    or (plyr.xplayer+playerw>=self.xbullet and plyr.xplayer+playerw<=self.xbullet+20 and plyr.yplayer>=self.ybullet and plyr.yplayer<=self.ybullet+20) \
                    or (plyr.xplayer + playerw >= self.xbullet and plyr.xplayer + playerw <= self.xbullet + 20 and plyr.yplayer+playerh >= self.ybullet and plyr.yplayer+playerh <= self.ybullet + 20) \
                    or (plyr.xplayer >= self.xbullet and plyr.xplayer <= self.xbullet + 20 and plyr.yplayer+playerh >= self.ybullet and plyr.yplayer+playerh <= self.ybullet + 20) \
                    or (plyr.xplayer + playerw//2 >= self.xbullet and plyr.xplayer + playerw//2 <= self.xbullet + 20 and plyr.yplayer + playerh >= self.ybullet and plyr.yplayer + playerh <= self.ybullet + 20) \
                    or (plyr.xplayer + playerw >= self.xbullet and plyr.xplayer + playerw <= self.xbullet + 20 and plyr.yplayer + playerh//2  >= self.ybullet and plyr.yplayer + playerh//2  <= self.ybullet + 20) \
                    or (plyr.xplayer >= self.xbullet and plyr.xplayer <= self.xbullet + 20 and plyr.yplayer + playerh//2 >= self.ybullet and plyr.yplayer + playerh//2 <= self.ybullet + 20) \
                    or (plyr.xplayer +playerw//2 >= self.xbullet and plyr.xplayer +playerw//2 <= self.xbullet + 20 and plyr.yplayer >= self.ybullet and plyr.yplayer <= self.ybullet + 20)):
                plyr.palive = False


class armageddon:
    argx = int()
    argy = int()
    excicting=True
    doing=False
    upper_bullet_list=[]
    right_bullet_list=[]
    lower_bullet_list=[]
    left_bullet_list=[]
    bullet_count=0
    type_of_bullet=None
    bullet_spawn_cd=0

    def get_arg(self, arg1, arg2):
        self.argx = arg1
        self.argy = arg2

    def draw(self):
        global armageddoncd
        if self.excicting and not self.doing:
            win.blit(armageddonimage, (self.argx, self.argy))
            for plyr in [myplayer, myplayer1]:
                if plyr.palive and((
                                           plyr.xplayer >= self.argx and plyr.xplayer <= self.argx + 40 and plyr.yplayer >= self.argy and plyr.yplayer <= self.argy + 40) \
                                   or (
                                           plyr.xplayer + playerw >= self.argx and plyr.xplayer + playerw <= self.argx + 40 and plyr.yplayer >= self.argy and plyr.yplayer <= self.argy + 40) \
                                   or (
                                           plyr.xplayer + playerw >= self.argx and plyr.xplayer + playerw <= self.argx + 40 and plyr.yplayer + playerh >= self.argy and plyr.yplayer + playerh <= self.argy + 40) \
                                   or (
                                           plyr.xplayer >= self.argx and plyr.xplayer <= self.argx + 40 and plyr.yplayer + playerh >= self.argy and plyr.yplayer + playerh <= self.argy + 40)):
                    self.doing = True
                    armageddoncd=600
        elif self.doing:
            if self.bullet_spawn_cd == 0:
                self.type_of_bullet=random.randint(1,4)
                if self.type_of_bullet==1:
                    self.upper_bullet_list.append(bullet())
                    self.upper_bullet_list[len(self.upper_bullet_list) - 1].setposition(random.randint(0,15)*40+10, -30)
                elif self.type_of_bullet==2:
                    self.right_bullet_list.append(bullet())
                    self.right_bullet_list[len(self.right_bullet_list) - 1].setposition(670, random.randint(0,15)*40+10)
                elif self.type_of_bullet==3:
                    self.lower_bullet_list.append(bullet())
                    self.lower_bullet_list[len(self.lower_bullet_list) - 1].setposition(random.randint(0,15)*40+10, 670)
                elif self.type_of_bullet==4:
                    self.left_bullet_list.append(bullet())
                    self.left_bullet_list[len(self.left_bullet_list) - 1].setposition(-30, random.randint(0,15)*40+10)
                self.bullet_spawn_cd=random.randint(1,40)
            self.bullet_spawn_cd -=1

            i_len=len(self.upper_bullet_list)
            for i in range(i_len):
                j=i_len - 1 - i
                self.upper_bullet_list[j].draw()
                if self.upper_bullet_list[j].ybullet > 640:
                    del self.upper_bullet_list[j]
                else:
                    self.upper_bullet_list[j].setposition(self.upper_bullet_list[j].xbullet, self.upper_bullet_list[j].ybullet + 10)

            i_len=len(self.right_bullet_list)
            for i in range(i_len):
                j=i_len - 1 - i
                self.right_bullet_list[j].draw()
                if self.right_bullet_list[j].xbullet < -40:
                    del self.right_bullet_list[j]
                else:
                    self.right_bullet_list[j].setposition(self.right_bullet_list[j].xbullet-10, self.right_bullet_list[j].ybullet)

            i_len=len(self.lower_bullet_list)
            for i in range(i_len):
                j=i_len - 1 - i
                self.lower_bullet_list[j].draw()
                if self.lower_bullet_list[j].ybullet < -40:
                    del self.lower_bullet_list[j]
                else:
                    self.lower_bullet_list[j].setposition(self.lower_bullet_list[j].xbullet, self.lower_bullet_list[j].ybullet - 10)

            i_len=len(self.left_bullet_list)
            for i in range(i_len):
                j=i_len - 1 - i
                self.left_bullet_list[j].draw()
                if self.left_bullet_list[j].ybullet > 640:
                    del self.left_bullet_list[j]
                else:
                    self.left_bullet_list[j].setposition(self.left_bullet_list[j].xbullet+10, self.left_bullet_list[j].ybullet)
    def clear(self):
        i_len=len(self.upper_bullet_list)
        for i in range(i_len):
            j=i_len - 1 - i
            del self.upper_bullet_list[j]

        i_len=len(self.right_bullet_list)
        for i in range(i_len):
            j=i_len - 1 - i
            del self.right_bullet_list[j]

        i_len=len(self.lower_bullet_list)
        for i in range(i_len):
            j=i_len - 1 - i
            del self.lower_bullet_list[j]


        i_len=len(self.left_bullet_list)
        for i in range(i_len):
            j=i_len - 1 - i
            del self.left_bullet_list[j]



class chainsawupgrader:
    argx = int()
    argy = int()
    excicting=True

    def get_arg(self, arg1, arg2):
        self.argx = arg1
        self.argy = arg2

    def draw(self):
        win.blit(chainsawupimage, (self.argx, self.argy))
        for plyr in [myplayer, myplayer1]:
            if plyr.palive and((
                    plyr.xplayer >= self.argx and plyr.xplayer <= self.argx + 40 and plyr.yplayer >= self.argy and plyr.yplayer <= self.argy + 40) \
                    or (
                    plyr.xplayer + playerw >= self.argx and plyr.xplayer + playerw <= self.argx + 40 and plyr.yplayer >= self.argy and plyr.yplayer <= self.argy + 40) \
                    or (
                    plyr.xplayer + playerw >= self.argx and plyr.xplayer + playerw <= self.argx + 40 and plyr.yplayer + playerh >= self.argy and plyr.yplayer + playerh <= self.argy + 40) \
                    or (
                    plyr.xplayer >= self.argx and plyr.xplayer <= self.argx + 40 and plyr.yplayer + playerh >= self.argy and plyr.yplayer + playerh <= self.argy + 40)):
                if plyr.chainsawupgrade:
                    plyr.chinsawcount+=200
                else:
                    plyr.chainsawupgrade = True
                self.excicting=False


class snakebuttonclass:
    argx = int()
    argy = int()
    snake1 = []
    snake2 = []
    snake3 = []
    snake4 = []
    snakecounter=0
    buttonexcicting = True
    snaking = False
    excicting = True
    def get_arg(self, arg1, arg2):
        self.argx = arg1
        self.argy = arg2

    def draw(self):
        if self.buttonexcicting:
            win.blit(snakebuttonimage, (self.argx, self.argy))
            for plyr in [myplayer, myplayer1]:
                if plyr.palive and((
                        plyr.xplayer >= self.argx and plyr.xplayer <= self.argx + 40 and plyr.yplayer >= self.argy and plyr.yplayer <= self.argy + 40) \
                        or (
                        plyr.xplayer + playerw >= self.argx and plyr.xplayer + playerw <= self.argx + 40 and plyr.yplayer >= self.argy and plyr.yplayer <= self.argy + 40) \
                        or (
                        plyr.xplayer + playerw >= self.argx and plyr.xplayer + playerw <= self.argx + 40 and plyr.yplayer + playerh >= self.argy and plyr.yplayer + playerh <= self.argy + 40) \
                        or (
                        plyr.xplayer >= self.argx and plyr.xplayer <= self.argx + 40 and plyr.yplayer + playerh >= self.argy and plyr.yplayer + playerh <= self.argy + 40)):
                    self.buttonexcicting=False
                    self.snaking=True
                    for i in range(0, 6):
                        self.snake1.append(bullet())
                        self.snake2.append(bullet())
                        self.snake3.append(bullet())
                        self.snake4.append(bullet())
                        self.snake1[i].setposition(self.argx+20-80,self.argy+20-80)
                        self.snake2[i].setposition(self.argx+20+120, self.argy+20-80)
                        self.snake3[i].setposition(self.argx+20-80, self.argy+20+100)
                        self.snake4[i].setposition(self.argx+20+100, self.argy+20+100)
        elif self.snaking:
            for i in range(0,5):
                num=5-i
                self.snake1[num].setposition(self.snake1[num-1].xbullet, self.snake1[num-1].ybullet)
                self.snake2[num].setposition(self.snake2[num-1].xbullet, self.snake2[num-1].ybullet)
                self.snake3[num].setposition(self.snake3[num-1].xbullet, self.snake3[num-1].ybullet)
                self.snake4[num].setposition(self.snake4[num-1].xbullet, self.snake4[num-1].ybullet)
                self.snake1[num].draw()
                self.snake2[num].draw()
                self.snake3[num].draw()
                self.snake4[num].draw()
            rand1 = random.randint(0, 1)
            self.snake1[0].setposition(self.snake1[0].xbullet-20*rand1, self.snake1[0].ybullet-20*(1-rand1))
            rand2 =random.randint(0,1)
            self.snake2[0].setposition(self.snake2[0].xbullet+20*rand2, self.snake2[0].ybullet-20*(1-rand2))
            rand3= random.randint(0, 1)
            self.snake3[0].setposition(self.snake3[0].xbullet-20*rand3, self.snake3[0].ybullet+20*(1-rand3))
            rand4 = random.randint(0, 1)
            self.snake4[0].setposition(self.snake4[0].xbullet+20*rand4, self.snake4[0].ybullet+20*(1-rand4))
            self.snake1[0].draw()
            self.snake2[0].draw()
            self.snake3[0].draw()
            self.snake4[0].draw()
            self.snakecounter += 1
            if self.snakecounter==50:
                self.excicting=False
    def clear(self):
        del self


class player:
    chainsawupgrade = False
    palive = True
    spritecondition=int()
    cone=0
    chain = [bullet(), bullet(), bullet(), bullet(), bullet(), bullet()]
    chinsawcount=400
    orbitup=True
    orbitdown=False
    orbitcount=0
    destroycount=0
    is_destroyed=False
    def setposition(self, argx, argy):
        self.xplayer=argx
        self.yplayer=argy
    def getx(self, argx):
        self.xplayer=argx

    def gety(self,argy):
        self.yplayer=argy
    def draw(self):
        if self.palive:
            self.spritecondition += 1
            win.blit(playersprites[self.spritecondition // 3], (self.xplayer, self.yplayer))
            if self.spritecondition == 17:
                self.spritecondition = 0
            if self.chainsawupgrade:
                if self.orbitup:
                    self.orbitcount+=1
                    if self.orbitcount==70:
                        self.orbitup=False
                        self.orbitdown=True
                if self.orbitdown:
                    self.orbitcount-=1
                    if self.orbitcount==0:
                        self.orbitup=True
                        self.orbitdown=False
                self.chain[0].setposition(self.xplayer + 10 + (115-self.orbitcount) * math.cos(math.radians(360 - (5 * self.cone)//3)),
                                          self.yplayer + 10 + (115-self.orbitcount) * math.sin(math.radians(360 - (5 * self.cone)//3)))
                self.chain[0].draw()
                self.chain[1].setposition(self.xplayer + 10 + (45+self.orbitcount) * math.cos(math.radians(self.cone)),
                                          self.yplayer + 10 + (45+self.orbitcount) * math.sin(math.radians(self.cone)))
                self.chain[1].draw()
                self.chain[2].setposition(
                    self.xplayer + 10 + (115-self.orbitcount) * math.cos(math.radians(360 - ((5 * self.cone)//3 + 120))),
                    self.yplayer + 10 + (115-self.orbitcount) * math.sin(math.radians(360 - ((5 * self.cone)//3 + 120))))
                self.chain[2].draw()
                self.chain[3].setposition(self.xplayer + 10 + (45+self.orbitcount) * math.cos(math.radians(self.cone + 120)),
                                          self.yplayer + 10 + (45+self.orbitcount) * math.sin(math.radians(self.cone + 120)))
                self.chain[3].draw()
                self.chain[4].setposition(
                    self.xplayer + 10 + (115-self.orbitcount) * math.cos(math.radians(360 - ((5 * self.cone)//3  + 240))),
                    self.yplayer + 10 + (115-self.orbitcount) * math.sin(math.radians(360 - ((5 * self.cone)//3 + 240))))
                self.chain[4].draw()
                self.chain[5].setposition(self.xplayer + 10 + (45+self.orbitcount) * math.cos(math.radians(self.cone + 240)),
                                          self.yplayer + 10 + (45+self.orbitcount) * math.sin(math.radians(self.cone + 240)))
                self.chain[5].draw()
                self.cone+=4
                if self.cone == 360:
                    self.cone=0
                self.chinsawcount-=1
                if self.chinsawcount==0:
                    self.chainsawupgrade=False
                    self.chinsawcount=400
    def drawdestroying(self):
        win.blit(player_destroing[self.destroycount//6],(self.xplayer-20, self.yplayer-20))
        self.destroycount+=1
        if self.destroycount==24:
            self.is_destroyed=True




myplayer=player()
myplayer.setposition(0, 0)
myplayer1=player()
myplayer1.setposition(600,600)



class deathblock:
    argx = int()
    argy = int()
    def get_arg(self , arg1, arg2):
        self.argx=arg1
        self.argy=arg2
        self.args=True
    def draw(self):
        win.blit(dblock, (self.argx, self.argy))
        for plyr in [myplayer,myplayer1]:
            if plyr.palive and((plyr.xplayer>=self.argx and plyr.xplayer<=self.argx+40 and plyr.yplayer>=self.argy and plyr.yplayer<=self.argy+40) \
                    or (plyr.xplayer+playerw>=self.argx and plyr.xplayer+playerw<=self.argx+40 and plyr.yplayer>=self.argy and plyr.yplayer<=self.argy+40) \
                    or (plyr.xplayer + playerw >= self.argx and plyr.xplayer + playerw <= self.argx + 40 and plyr.yplayer+playerh >= self.argy and plyr.yplayer+playerh <= self.argy + 40) \
                    or (plyr.xplayer >= self.argx and plyr.xplayer <= self.argx + 40 and plyr.yplayer+playerh >= self.argy and plyr.yplayer+playerh <= self.argy + 40)):
                plyr.palive = False





#Risovanie deistviy na ekrane
def DrawWindow():
    win.blit(bg, (0, 0))
    global bulletlistsq
    global snakebuttons

    myplayer.draw()
    myplayer1.draw()
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

    for plyr in [myplayer, myplayer1]:
        if not plyr.palive and not plyr.is_destroyed:
            plyr.drawdestroying()

    chainupsq = 0
    for chupgr in range(len(chainupgraders)):
        chainupgraders[chupgr-chainupsq].draw()
        if not chainupgraders[chupgr-chainupsq].excicting:
            del chainupgraders[chupgr-chainupsq]
            chainupsq += 1

    snkbuttsq = 0
    for snkbutt in range(len(snakebuttons)):
        snakebuttons[snkbutt-snkbuttsq].draw()
        if not snakebuttons[snkbutt-snkbuttsq].excicting:
            for i in range(snkbutt-snkbuttsq,len(snakebuttons)-1):
                snakebuttons[i].clear()
                snakebuttons[i]=snakebuttons[i+1]
            snakebuttons[len(snakebuttons)-1].clear()
            del snakebuttons[len(snakebuttons)-1]
            snkbuttsq += 1

    if len(armageddons) == 1:
        armageddons[0].draw()



    for dd in range(0,dbnumber):
        dblocks[dd].draw()

    pygame.display.update()

# intro cycle

while intro:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            intro = False
    win.blit(introsprite[intro_counter//intro_fr], (0, 0))
    pygame.display.update()
    if intro_end:
        keys=pygame.key.get_pressed()
        if keys[pygame.K_f]:
            intro = False
    else:
        if intro_counter > 12*intro_fr:
            win.blit(introsprite[12], (0, 0))
            pygame.display.update()
            intro_end = True

        else:
            win.blit(introsprite[intro_counter//intro_fr], (0, 0))
            pygame.display.update()
            intro_counter += 1
    pygame.time.delay(15)

#main cycle

while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False

    dcount+=1
    if dcount==20 and dcount2<16 and dbnumber<256:
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

    chainupcd-=1
    if chainupcd==0:
        chainupgraders.append(chainsawupgrader())
        chainupgraders[len(chainupgraders)-1].get_arg(random.randint(0,15)*40,random.randint(0,15)*40)
        chainupcd = 600

    snakebuttoncd -=1
    if snakebuttoncd==0:
        if len(snakebuttons) > 0:
            snakebuttons = []
        snakebuttons.append(snakebuttonclass())
        snakebuttons[len(snakebuttons)-1].get_arg(random.randint(0,15)*40,random.randint(0,15)*40)
        snakebuttoncd = 400

    armageddoncd -=1
    if armageddoncd==0:
        armageddons.append(armageddon())
        armageddons[0].get_arg(random.randint(0,15)*40,random.randint(0,15)*40)
        armageddoncd=500
    elif armageddoncd==100 and len(armageddons)!=0:
        armageddons[0].clear()
        del armageddons[0]







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
            if keys[pygame.K_t]:
                upbullets.append(bullet())
                upbulletsx.append(myplayer.xplayer+(playerw-bulleta)//2)
                upbulletsy.append(myplayer.yplayer-bulleta-1)
            elif keys[pygame.K_g]:
                downbullets.append(bullet())
                downbulletsx.append(myplayer.xplayer+(playerw-bulleta)//2)
                downbulletsy.append(myplayer.yplayer+playerh+1)
            elif keys[pygame.K_h]:
                rightbullets.append(bullet())
                rightbulletsx.append(myplayer.xplayer+playerw+1)
                rightbulletsy.append(myplayer.yplayer+(playerh-bulleta)//2)
            elif keys[pygame.K_f]:
                leftbullets.append(bullet())
                leftbulletsx.append(myplayer.xplayer-bulleta-1)
                leftbulletsy.append(myplayer.yplayer+(playerh-bulleta)//2)





    if myplayer1.palive:
        keys=pygame.key.get_pressed()

        if keys[pygame.K_o] and myplayer1.yplayer>0:
            myplayer1.gety(myplayer1.yplayer-pspeed)

        if keys[pygame.K_l] and myplayer1.yplayer<winh-playerh:
            myplayer1.gety(myplayer1.yplayer + pspeed)

        if keys[pygame.K_SEMICOLON] and myplayer1.xplayer<winw-playerw:
            myplayer1.getx(myplayer1.xplayer + pspeed)

        if keys[pygame.K_k] and myplayer1.xplayer>0:
            myplayer1.getx(myplayer1.xplayer - pspeed)




        shootcd1+=1
        if shootcd1==10:
            shootcdb1=True
            shootcd1=0
        if shootcdb1:
            shootcd1=0
            shootcdb1=False
            if keys[pygame.K_KP8]:
                upbullets.append(bullet())
                upbulletsx.append(myplayer1.xplayer+(playerw-bulleta)//2)
                upbulletsy.append(myplayer1.yplayer-bulleta-1)
            elif keys[pygame.K_KP5]:
                downbullets.append(bullet())
                downbulletsx.append(myplayer1.xplayer+(playerw-bulleta)//2)
                downbulletsy.append(myplayer1.yplayer+playerh+1)
            elif keys[pygame.K_KP6]:
                rightbullets.append(bullet())
                rightbulletsx.append(myplayer1.xplayer+playerw+1)
                rightbulletsy.append(myplayer1.yplayer+(playerh-bulleta)//2)
            elif keys[pygame.K_KP4]:
                leftbullets.append(bullet())
                leftbulletsx.append(myplayer1.xplayer-bulleta-1)
                leftbulletsy.append(myplayer1.yplayer+(playerh-bulleta)//2)
    pygame.time.delay(15)
    DrawWindow()

pygame.quit()

