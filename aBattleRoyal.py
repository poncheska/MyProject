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
pygame.mixer.music.load("music1.mp3")
pygame.mixer.music.play(10)
winw=640
winh=640
clock=pygame.time.Clock()

run=True

win=pygame.display.set_mode((winw,winh))
pygame.display.set_caption("Doka 2")
pygame.display.set_icon(pygame.image.load('icon.jpg'))
bg=pygame.image.load('background.jpg')
dblock=pygame.image.load('deathblock.png')
dcount= -200
dcount1= -1
dcount2= 0
dblocks=[]
dblim=0
dbnumber=-1
#egg
theend = pygame.image.load('theend.jpg')
arthasliveimage = [pygame.image.load('arthaslive1.png'),
                   pygame.image.load('arthaslive2.png'),
                   pygame.image.load('arthaslive3.png'),
                   pygame.image.load('arthaslive4.png'),
                   pygame.image.load('arthaslive5.png'),
                   pygame.image.load('arthaslive6.png')]
arthaskillcd = 400
arthaslive = 5
eggruncnt = 0
egg = False
eggactive = False
eastereggimage = pygame.image.load('easter_egg.png')
eggcounter = 0
eggspritecnt = 0
eggbg = pygame.image.load('egg_bg.jpg')
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
              pygame.image.load('intro_last.jpg')]
intro_fr = 7
intro = True
intro_counter = 0
intro_end = False
# bulletff
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
players = []
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
armageddons=[]
armageddoncd=200

class bullet:
    def __init__(self, xbullet, ybullet):
        self.spritecondition = 0
        self.bulletsprite = [pygame.image.load('bullet1.png'),
                             pygame.image.load('bullet2.png'),
                             pygame.image.load('bullet3.png')]
        self.xbullet = xbullet
        self.ybullet = ybullet
    def setposition(self, arg1, arg2):
        self.xbullet=arg1
        self.ybullet=arg2
    def draw(self):
        self.spritecondition+=1
        if self.spritecondition==3:
            self.spritecondition=0
        win.blit(self.bulletsprite[self.spritecondition], (self.xbullet, self.ybullet))
        for plyr in players:
            if plyr.palive and((plyr.xplayer>=self.xbullet <= plyr.xplayer<=self.xbullet+20 and self.ybullet <= plyr.yplayer<=self.ybullet+20)
                    or (self.xbullet <= plyr.xplayer+playerw<=self.xbullet+20 and plyr.yplayer>=self.ybullet <= plyr.yplayer<=self.ybullet+20)
                    or (self.xbullet <= plyr.xplayer + playerw <= self.xbullet + 20 and self.ybullet <= plyr.yplayer+playerh <= self.ybullet + 20)
                    or (self.xbullet <= plyr.xplayer <= self.xbullet + 20 and self.ybullet <= plyr.yplayer+playerh <= self.ybullet + 20)
                    or (self.xbullet <= plyr.xplayer + playerw//2 <= self.xbullet + 20 and self.ybullet <= plyr.yplayer + playerh <= self.ybullet + 20)
                    or (self.xbullet <= plyr.xplayer + playerw <= self.xbullet + 20 and self.ybullet <= plyr.yplayer + playerh//2  <= self.ybullet + 20)
                    or (self.xbullet <= plyr.xplayer <= self.xbullet + 20 and self.ybullet <= plyr.yplayer + playerh//2 <= self.ybullet + 20)
                    or (self.xbullet <= plyr.xplayer +playerw//2 <= self.xbullet + 20 and self.ybullet <= plyr.yplayer <= self.ybullet + 20)):
                plyr.palive = False


class armageddon:
    def __init__(self, argx, argy):
        self.armageddonimage = pygame.image.load('armageddon.png')
        self.argx = argx
        self.argy = argy
        self.excicting = True
        self.doing = False
        self.upper_bullet_list=[]
        self.right_bullet_list=[]
        self.lower_bullet_list=[]
        self.left_bullet_list=[]
        self.bullet_count=0
        self.type_of_bullet=None
        self.bullet_spawn_cd=0

    def draw(self):
        global armageddoncd
        if self.excicting and not self.doing:
            win.blit(self.armageddonimage, (self.argx, self.argy))
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
                    self.upper_bullet_list.append(bullet(random.randint(0,15)*40+10, -30))
                elif self.type_of_bullet==2:
                    self.right_bullet_list.append(bullet(670, random.randint(0,15)*40+10))
                elif self.type_of_bullet==3:
                    self.lower_bullet_list.append(bullet(random.randint(0,15)*40+10, 670))
                elif self.type_of_bullet==4:
                    self.left_bullet_list.append(bullet(-30, random.randint(0,15)*40+10))
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
        for plyr in players:
            if plyr.palive and((
                    plyr.xplayer >= self.argx and plyr.xplayer <= self.argx + 40 and plyr.yplayer >= self.argy and plyr.yplayer <= self.argy + 40)
                    or (
                    plyr.xplayer + playerw >= self.argx and plyr.xplayer + playerw <= self.argx + 40 and plyr.yplayer >= self.argy and plyr.yplayer <= self.argy + 40)
                    or (
                    plyr.xplayer + playerw >= self.argx and plyr.xplayer + playerw <= self.argx + 40 and plyr.yplayer + playerh >= self.argy and plyr.yplayer + playerh <= self.argy + 40)
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
                        self.snake1.append(bullet(self.argx+20-80,self.argy+20-80))
                        self.snake2.append(bullet(self.argx+20+120, self.argy+20-80))
                        self.snake3.append(bullet(self.argx+20-80, self.argy+20+100))
                        self.snake4.append(bullet(self.argx+20+100, self.argy+20+100))
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
    def __init__(self, argx, argy):
        self.chain = [bullet(-30, -30), bullet(-30, -30),
                      bullet(-30, -30), bullet(-30, -30),
                      bullet(-30, -30), bullet(-30, -30)]
        self.chainsawupgrade = False
        self.palive = True
        self.spritecondition=int()
        self.cone=0
        self.chinsawcount=400
        self.orbitup=True
        self.orbitdown=False
        self.orbitcount=0
        self.destroycount=0
        self.is_destroyed=False
        self.xplayer=argx
        self.yplayer=argy
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
                self.chain[1].setposition(self.xplayer + 10 + (45+self.orbitcount) * math.cos(math.radians(self.cone)),
                                          self.yplayer + 10 + (45+self.orbitcount) * math.sin(math.radians(self.cone)))
                self.chain[2].setposition(
                    self.xplayer + 10 + (115-self.orbitcount) * math.cos(math.radians(360 - ((5 * self.cone)//3 + 120))),
                    self.yplayer + 10 + (115-self.orbitcount) * math.sin(math.radians(360 - ((5 * self.cone)//3 + 120))))
                self.chain[3].setposition(self.xplayer + 10 + (45+self.orbitcount) * math.cos(math.radians(self.cone + 120)),
                                          self.yplayer + 10 + (45+self.orbitcount) * math.sin(math.radians(self.cone + 120)))
                self.chain[4].setposition(
                    self.xplayer + 10 + (115-self.orbitcount) * math.cos(math.radians(360 - ((5 * self.cone)//3  + 240))),
                    self.yplayer + 10 + (115-self.orbitcount) * math.sin(math.radians(360 - ((5 * self.cone)//3 + 240))))
                self.chain[5].setposition(self.xplayer + 10 + (45+self.orbitcount) * math.cos(math.radians(self.cone + 240)),
                                          self.yplayer + 10 + (45+self.orbitcount) * math.sin(math.radians(self.cone + 240)))
                for i in self.chain:
                    i.draw()
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




myplayer=player(0, 0)
myplayer1=player(600,600)
players.append(myplayer)
players.append(myplayer1)


class deathblock:
    def __init__(self, argx, argy):
        self.argx = argx
        self.argy = argy
        self.args = True
    def get_arg(self , arg1, arg2):
        self.argx=arg1
        self.argy=arg2
        self.args=True
    def draw(self):
        win.blit(dblock, (self.argx, self.argy))
        for plyr in players:
            if plyr.palive and((plyr.xplayer>=self.argx and plyr.xplayer<=self.argx+40 and plyr.yplayer>=self.argy and plyr.yplayer<=self.argy+40) \
                    or (plyr.xplayer+playerw>=self.argx and plyr.xplayer+playerw<=self.argx+40 and plyr.yplayer>=self.argy and plyr.yplayer<=self.argy+40) \
                    or (plyr.xplayer + playerw >= self.argx and plyr.xplayer + playerw <= self.argx + 40 and plyr.yplayer+playerh >= self.argy and plyr.yplayer+playerh <= self.argy + 40) \
                    or (plyr.xplayer >= self.argx and plyr.xplayer <= self.argx + 40 and plyr.yplayer+playerh >= self.argy and plyr.yplayer+playerh <= self.argy + 40)):
                plyr.palive = False


class ArtasDestroyer:
    def __init__(self, x, y):
        self.argx = x
        self.argy = y
        self.sprite = [pygame.image.load('artkill1.png'),
                       pygame.image.load('artkill2.png'),
                       pygame.image.load('artkill3.png'),
                       pygame.image.load('artkill4.png')]
        self.spritecount = 0
        self.exciting = True

    def draw(self):
        win.blit(self.sprite[self.spritecount//5], (self.argx, self.argy))
        self.spritecount += 1
        if self.spritecount == 20:
            self.spritecount = 0
        self.argx -= 5
        if self.argx < -80:
            self.exciting = False
        if eggplayer.palive and((eggplayer.xplayer>=self.argx and eggplayer.xplayer<=self.argx+80 and eggplayer.yplayer>=self.argy and eggplayer.yplayer<=self.argy+80)
                           or (eggplayer.xplayer+playerw>=self.argx and eggplayer.xplayer+playerw<=self.argx+80 and eggplayer.yplayer>=self.argy and eggplayer.yplayer<=self.argy+80)
                           or (eggplayer.xplayer + playerw >= self.argx and eggplayer.xplayer + playerw <= self.argx + 80 and eggplayer.yplayer+playerh >= self.argy and eggplayer.yplayer+playerh <= self.argy + 80)
                           or (eggplayer.xplayer >= self.argx and eggplayer.xplayer <= self.argx + 80 and eggplayer.yplayer+playerh >= self.argy and eggplayer.yplayer+playerh <= self.argy + 80)):
            global arthaslive
            arthaslive -= 1
            self.exciting = False

class Arthas:
    def __init__(self):
        self.sprite = [pygame.image.load('eggboss1.png'),
                       pygame.image.load('eggboss2.png'),
                       pygame.image.load('eggboss3.png'),
                       pygame.image.load('eggboss4.png'),
                       pygame.image.load('eggboss5.png'),
                       pygame.image.load('eggboss6.png')]

        self.deathimage = [pygame.image.load('artdeath1.png'),
                           pygame.image.load('artdeath2.png'),
                           pygame.image.load('artdeath3.png'),
                           pygame.image.load('artdeath4.png'),
                           pygame.image.load('artdeath5.png'),
                           pygame.image.load('artdeath6.png'),
                           pygame.image.load('artdeath7.png'),
                           pygame.image.load('artdeath8.png'),
                           pygame.image.load('artdeath9.png'),
                           pygame.image.load('artdeath10.png')]

        self.animcount = 0
        self.x = 480
        self.y = 240
        self.bulletlist = []
        self.aimy = None
        self.aim = False
        self.ulti = False
        self.ulticd = 100
        self.walllist = []
        self.wallcd = 150
        self.exciting = True
        self.exciting2 = True

    def draw(self):
        if self.exciting:
            self.ulticd -= 1
            self.wallcd -= 1
            global arthaslive

            if self.ulticd == 0:
                self.ultimate()
                self.ulticd = 100 - (5 - arthaslive) * 15
                self.wallcd += 20 + (5 - arthaslive) * 5

            if self.wallcd == 0:
                self.wall()
                self.wallcd = 150
                self.ulticd += 100 - (5 - arthaslive) * 20

            self.move()

            if not self.ulti:
                win.blit(self.sprite[0], (self.x, self.y))
            else:
                win.blit(self.sprite[self.animcount//5], (self.x, self.y))
                self.animcount += 1
                if self.animcount == 30:
                    self.animcount = 0
                    self. ulti = False

            for i in self.bulletlist:
                i.setposition(i.xbullet - 4, i.ybullet)
                i.draw()
                if i.xbullet < -20:
                    del i

            for i in self.walllist:
                i.get_arg(i.argx - 2, i.argy)
                i.draw()
                if i.argx < -40:
                    del i
        else:
            if self.x != 240 or self.x != 240:
                if self.x < 240:
                    self.x = (self.x + 4)
                elif self.x > 240:
                    self.x = (self.x - 4)
                if self.y < 240:
                    self.y = (self.y + 4)
                elif self.y > 240:
                    self.y = (self.y - 4)
                win.blit(self.sprite[self.animcount//5], (self.x, self.y))
                self.animcount += 1
                if self.animcount == 30:
                    self.animcount = 0
            else:
                win.blit(self.deathimage[self.animcount//5], (0, 0))
                self.animcount += 1
                if self.animcount == 49:
                    self.animcount = 0
                    self.exciting2 = False

    def move(self):
        if not self.aim:
            self.aimy = random.randint(10, 110) * 4
            self.aim = True
        if self.y > self.aimy:
            self.y -= 4
        elif self.y < self.aimy:
            self.y += 4
        if self.y == self.aimy:
            self.aim = False

    def ultimate(self):
        self.ulti = True
        self.bulletlist.append(bullet(self.x - 20, self.y + 40))
        self.bulletlist.append(bullet(self.x - 40, self.y + 60))
        self.bulletlist.append(bullet(self.x - 40, self.y + 80))
        self.bulletlist.append(bullet(self.x - 20, self.y + 100))

    def wall(self):
        count=40
        global eggruncnt
        while count < self.y - 40:
            self.walllist.append(deathblock(self.x - eggruncnt*2 + 4, count))
            count += 40
        count=560
        while count > self.y + 160 + 40:
            self.walllist.append(deathblock(self.x - eggruncnt*2 + 4, count))
            count -= 40




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
            egg = False
    win.blit(introsprite[intro_counter//intro_fr], (0, 0))
    pygame.display.update()
    if intro_end:
        eggcounter += 1
        keys = pygame.key.get_pressed()
        if eggcounter == 100:
            intro = False
            egg = True
            pygame.mixer.music.load("egg1.mp3")
            pygame.mixer.music.play(1)
        if keys[pygame.K_f]:
            intro = False
            pygame.mixer.music.load("music.mp3")
            pygame.mixer.music.play(1)
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

eggplayer = player(10, 280)
players.append(eggplayer)
evil = Arthas()
arthaskills = []

while egg:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            egg = False
    if not eggactive:
        win.blit(introsprite[11], (0, 0))
        win.blit(eastereggimage, (-640 + eggspritecnt*5, 320))
        pygame.display.update()
        if eggspritecnt<128:
            eggspritecnt += 1
        keys = pygame.key.get_pressed()
        if keys[pygame.K_F5]:
            eggactive = True
            pygame.mixer.music.load("arthasfight.mp3")
            pygame.mixer.music.play(1)
    elif evil.exciting2 and eggplayer.palive:
        win.blit(eggbg, (eggruncnt*2, 0))
        eggplayer.draw()
        eggruncnt -= 1

        if evil.exciting:
            arthaskillcd -= 1
            if arthaskillcd == 0:
                arthaskills.append(ArtasDestroyer(640, random.randint(40, 520)))
                arthaskillcd = 400
            if len(arthaskills) != 0:
                arthaskills[0].draw()
                if not arthaskills[0].exciting:
                    del arthaskills[0]

        if eggruncnt == -20:
            eggruncnt = 0

        keys=pygame.key.get_pressed()

        if keys[pygame.K_q] and eggplayer.yplayer > 40:
            eggplayer.gety(eggplayer.yplayer - 10)

        if keys[pygame.K_a] and eggplayer.yplayer < 560:
            eggplayer.gety(eggplayer.yplayer + 10)

        if keys[pygame.K_w] and eggplayer.yplayer > 40:
            eggplayer.gety(eggplayer.yplayer - 5)

        if keys[pygame.K_s] and eggplayer.yplayer < 560:
            eggplayer.gety(eggplayer.yplayer + 5)

        if keys[pygame.K_e] and eggplayer.yplayer > 40:
            eggplayer.gety(eggplayer.yplayer - 1)

        if keys[pygame.K_d] and eggplayer.yplayer < 560:
            eggplayer.gety(eggplayer.yplayer + 1)

        evil.draw()
        win.blit(arthasliveimage[(5-arthaslive) % 6], (200, 5))
        if arthaslive == 0 and evil.exciting:
            evil.exciting = False
            pygame.mixer.music.load("artlose.mp3")
            pygame.mixer.music.play(1)
        pygame.display.update()
    else:
        win.blit(theend, (0, 0))
        pygame.display.update()



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
            dblocks.append(deathblock((dblim + dcount1) * 40, dcount2 * 40))
            dbnumber += 1
            dblocks.append(deathblock(600 - (dblim + dcount1) * 40, 600 - dcount2 * 40))
            dbnumber += 1
            dblocks.append(deathblock(600 - dcount2 * 40, (dblim + dcount1) * 40))
            dbnumber += 1
            dblocks.append(deathblock(dcount2 * 40, 600 - (dblim + dcount1) * 40))
        else:
            dbnumber += 1
            dblocks.append(deathblock((dblim+dcount1)*40, dcount2*40))
            dbnumber += 1
            dblocks.append(deathblock(600-(dblim+dcount1)*40, 600-dcount2*40))
            dbnumber += 1
            dblocks.append(deathblock(600-dcount2*40, (dblim+dcount1)*40))
            dbnumber += 1
            dblocks.append(deathblock(dcount2*40, 600-(dblim+dcount1)*40))

    chainupcd-=1
    if chainupcd==0:
        chainupgraders.append(chainsawupgrader())
        chainupgraders[len(chainupgraders)-1].get_arg(random.randint(0,15)*40,random.randint(0,15)*40)
        chainupcd = 600

    snakebuttoncd -= 1
    if snakebuttoncd == 0:
        if len(snakebuttons) > 0:
            snakebuttons = []
        snakebuttons.append(snakebuttonclass())
        snakebuttons[len(snakebuttons)-1].get_arg(random.randint(0,15)*40,random.randint(0,15)*40)
        snakebuttoncd = 400

    armageddoncd -=1
    if armageddoncd==0:
        armageddons.append(armageddon(random.randint(0,15)*40,random.randint(0,15)*40))
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
                upbullets.append(bullet(myplayer.xplayer+(playerw-bulleta)//2, myplayer.yplayer-bulleta-1))
                upbulletsx.append(myplayer.xplayer+(playerw-bulleta)//2)
                upbulletsy.append(myplayer.yplayer-bulleta-1)
            elif keys[pygame.K_g]:
                downbullets.append(bullet(myplayer.xplayer+(playerw-bulleta)//2, myplayer.yplayer+playerh+1))
                downbulletsx.append(myplayer.xplayer+(playerw-bulleta)//2)
                downbulletsy.append(myplayer.yplayer+playerh+1)
            elif keys[pygame.K_h]:
                rightbullets.append(bullet(myplayer.xplayer+playerw+1, myplayer.yplayer+(playerh-bulleta)//2))
                rightbulletsx.append(myplayer.xplayer+playerw+1)
                rightbulletsy.append(myplayer.yplayer+(playerh-bulleta)//2)
            elif keys[pygame.K_f]:
                leftbullets.append(bullet(myplayer.xplayer-bulleta-1, myplayer.yplayer+(playerh-bulleta)//2))
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
                upbullets.append(bullet(myplayer1.xplayer+(playerw-bulleta)//2, myplayer1.yplayer-bulleta-1))
                upbulletsx.append(myplayer1.xplayer+(playerw-bulleta)//2)
                upbulletsy.append(myplayer1.yplayer-bulleta-1)
            elif keys[pygame.K_KP5]:
                downbullets.append(bullet(myplayer1.xplayer+(playerw-bulleta)//2, myplayer1.yplayer+playerh+1))
                downbulletsx.append(myplayer1.xplayer+(playerw-bulleta)//2)
                downbulletsy.append(myplayer1.yplayer+playerh+1)
            elif keys[pygame.K_KP6]:
                rightbullets.append(bullet(myplayer1.xplayer+playerw+1, myplayer1.yplayer+(playerh-bulleta)//2))
                rightbulletsx.append(myplayer1.xplayer+playerw+1)
                rightbulletsy.append(myplayer1.yplayer+(playerh-bulleta)//2)
            elif keys[pygame.K_KP4]:
                leftbullets.append(bullet(myplayer1.xplayer-bulleta-1, myplayer1.yplayer+(playerh-bulleta)//2))
                leftbulletsx.append(myplayer1.xplayer-bulleta-1)
                leftbulletsy.append(myplayer1.yplayer+(playerh-bulleta)//2)
    pygame.time.delay(15)
    DrawWindow()

pygame.quit()

