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
        self.argx=arg1*40
        self.argy=arg2*40
        self.args=True
    def draw(self):
        if self.args:
            global palive
            win.blit(dblock, (self.argx, self.argy))
            if xplayer>=self.argx and xplayer<=self.argx+40 and yplayer>=self.argy and yplayer<=self.argy+40:
                palive=False









#Risovanie deistviy na ekrane
def DrawWindow(dc):
    win.blit(bg, (0, 0))

    if palive:
        pygame.draw.rect(win,(0,0,0),(xplayer,yplayer,playerw,playerh))

    for dd in range(0,dc):
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
    if dcount==20 and dcount2<16:
        dcount=0
        dcount1+=1
        if dcount1==16:
            dcount1=0
            dcount2+=1
            dblocks.append(deathblock())
            dblocks[dcount1 + dcount2 * 16].get_arg(dcount1, dcount2)
        else:
            dblocks.append(deathblock())
            dblocks[dcount1+dcount2*16].get_arg(int(dcount1), int(dcount2))

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



