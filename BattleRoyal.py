import pygame
pygame.init()
# Peremennie
winw=740
winh=740
clock=pygame.time.Clock()

run=True

win=pygame.display.set_mode((winw,winh))
pygame.display.set_caption("Tiny Battle Royale")

bg=pygame.image.load('background.jpg')

#Risovanie deistviy na ekrane
def DrawWindow():
    win.blit(bg, (0, 0))

#main cycle
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
    DrawWindow()
    clock.tick(100)
pygame.quit()



