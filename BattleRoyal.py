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
# player var-s
xplayer=0
yplayer=0
playerh=40
playerw=40
pspeed=10
movup=False
movdown=False
movright=False
movleft=False
palive= True

class deathblock:
    argx = int()
    argy = int()
    args=False
    def get_arg(self , arg1, arg2):
        self.argx=arg1
        self.argy=arg2
        self.args=True
    def draw(self):
        if self.args:
            global palive
            win.blit(dblock, (self.argx, self.argy))
            if (xplayer>=self.argx and xplayer<=self.argx+40 and yplayer>=self.argy and yplayer<=self.argy+40) \
                    or (xplayer+playerw>=self.argx and xplayer+playerw<=self.argx+40 and yplayer>=self.argy and yplayer<=self.argy+40) \
                    or (xplayer + playerw >= self.argx and xplayer + playerw <= self.argx + 40 and yplayer+playerh >= self.argy and yplayer+playerh <= self.argy + 40) \
                    or (xplayer >= self.argx and xplayer <= self.argx + 40 and yplayer+playerh >= self.argy and yplayer+playerh <= self.argy + 40):
                palive=False









#Risovanie deistviy na ekrane
def DrawWindow(dc):
    win.blit(bg, (0, 0))

    if palive:
        pygame.draw.rect(win,(0,0,0),(xplayer,yplayer,playerw,playerh))

    for dd in range(0,dbnumber):
        dblocks[dd].draw()
    pygame.display.update()







#main cycle
while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False



    pygame.time.delay(10)
    dcount+=1
    if dcount==2 and dcount2<16 and dbnumber<256:
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

    DrawWindow(dcount1+dcount2*16)

    keys=pygame.key.get_pressed()
    if keys[pygame.K_w] and yplayer>0:
        yplayer-=pspeed
    if keys[pygame.K_s] and yplayer<winh-playerh:
        yplayer+=pspeed
    if keys[pygame.K_d] and xplayer<winw-playerw:
        xplayer+=pspeed
    if keys[pygame.K_a] and xplayer>0:
        xplayer-=pspeed


pygame.quit()



