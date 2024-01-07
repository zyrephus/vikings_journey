import pygame
pygame.init()
size = (1000, 650)
screen = pygame.display.set_mode(size)

#colors
BLACK = [0,0,0]
WHITE = [255,255,255]
GREEN = [0,255,0]
RED = [255,0,0]
BLUE = [0,0,255]
MAGENTA = [255,0,255]
YELLOW = [255,255,0]
ORANGE = [255,165,0]
mainCOLOR = [39,44,59]
detailCOLOR = [21,74,49]
optionCOLOR = [65, 77, 125]
optionCOLORL = [91,101,130]
GOLD = [217,165,9]
lightBlue = [207,248,250]

oColor = optionCOLOR
oColor2 = optionCOLOR
oColor3 = optionCOLOR

#details
def background():
    #top left
    pygame.draw.circle(screen, detailCOLOR, [0,50],100)
    pygame.draw.circle(screen, detailCOLOR, [80,40],80)
    pygame.draw.circle(screen, detailCOLOR, [170,20],50)
    pygame.draw.circle(screen, detailCOLOR, [5,150],30)
    #top right
    pygame.draw.circle(screen, detailCOLOR, [950,40],150)
    pygame.draw.circle(screen, detailCOLOR, [750,25],70)
    pygame.draw.circle(screen, detailCOLOR, [975,150],110)
    pygame.draw.circle(screen, detailCOLOR, [990,275],50)
    pygame.draw.circle(screen, detailCOLOR, [820,130],35)
    #bottom left
    pygame.draw.circle(screen, detailCOLOR, [20,630],75)
    pygame.draw.circle(screen, detailCOLOR, [20,520],90)
    pygame.draw.circle(screen, detailCOLOR, [150,675],70)
    pygame.draw.circle(screen, detailCOLOR, [220,665],80)
    pygame.draw.circle(screen, detailCOLOR, [270,595],30)
    #bottom right
    pygame.draw.circle(screen, detailCOLOR, [1000,625],75)
    pygame.draw.circle(screen, detailCOLOR, [1000,525],30)
    pygame.draw.circle(screen, detailCOLOR, [900,675],60)
    #text
    font = pygame.font.SysFont('Arial',16, True, False)
    startText = font.render("- ICS3U1a, O'Gorman High School | Ver. Alpha Stage -", True, optionCOLORL)
    screen.blit(startText, [315,625])

def roll():
    rollPos = 800
    rollMove = 1
    running = True
    while running:
        background()
        creditImg = pygame.image.load('credits.png')
        screen.blit(creditImg, [100,rollPos])
        for event in pygame.event.get:
            rollPos-=rollMove
            if rollPos == 25:
                rollMove = 0
        pygame.display.update()

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    #background
    screen.fill(mainCOLOR)
    roll()
    pygame.display.flip()
pygame.quit()
