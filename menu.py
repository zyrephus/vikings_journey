import pygame, sys
pygame.init()
size = (1000, 650)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Viking's Journey")

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

xText1 = 160
pxText1 = xText1+15
nxText1 = xText1-15
xText2 = xText1+425
xShield = xText1 + 265
#logo
def logo():
    font = pygame.font.SysFont('Times New Roman',75, True, False)
    startText = font.render("Viking's", True, lightBlue)
    screen.blit(startText, [xText1,65])
    font = pygame.font.SysFont('Times New Roman',75, True, False)
    startText = font.render("Journey", True, lightBlue)
    screen.blit(startText, [xText2,65])
    
    shieldImg = pygame.image.load('shield.png')
    shieldImg = pygame.transform.scale(shieldImg, [150,110])
    screen.blit(shieldImg, [xShield,50])

#hover color
hoverColor = WHITE
hoverColor2 = WHITE
hoverColor3 = WHITE
#buttons
def options():
    #start
    pygame.draw.line(screen, hoverColor, [410,177],[590,177],5)
    pygame.draw.line(screen, hoverColor, [410,252],[590,252],5)
    pygame.draw.circle(screen, hoverColor, [410,215],40,5)
    pygame.draw.circle(screen, hoverColor, [590,215],40,5)
    pygame.draw.rect(screen, oColor, [410,180,180,70])
    pygame.draw.circle(screen, oColor, [410,215],35)
    pygame.draw.circle(screen, oColor, [590,215],35)
    #text
    font = pygame.font.SysFont('Calibri',50, True, False)
    startText = font.render("Start", True, WHITE)
    screen.blit(startText, [445,192])

    #credits
    pygame.draw.line(screen, hoverColor2, [410,272],[590,272],5)
    pygame.draw.line(screen, hoverColor2, [410,347],[590,347],5)
    pygame.draw.circle(screen, hoverColor2, [410,310],40,5)
    pygame.draw.circle(screen, hoverColor2, [590,310],40,5)
    pygame.draw.rect(screen, oColor2, [410,275,180,70])
    pygame.draw.circle(screen, oColor2, [410,310],35)
    pygame.draw.circle(screen, oColor2, [590,310],35)
    #text
    font = pygame.font.SysFont('Calibri',50, True, False)
    startText = font.render("Credits", True, WHITE)
    screen.blit(startText, [430,287])
    
    #quit
    pygame.draw.line(screen, hoverColor3, [410,367],[590,367],5)
    pygame.draw.line(screen, hoverColor3, [410,442],[590,442],5)
    pygame.draw.circle(screen, hoverColor3, [410,405],40,5)
    pygame.draw.circle(screen, hoverColor3, [590,405],40,5)
    pygame.draw.rect(screen, oColor3, [410,370,180,70])
    pygame.draw.circle(screen, oColor3, [410,405],35)
    pygame.draw.circle(screen, oColor3, [590,405],35)
    #text
    font = pygame.font.SysFont('Calibri',50, True, False)
    startText = font.render("Quit", True, WHITE)
    screen.blit(startText, [452,382])

def menu():
    screen.fill(mainCOLOR)
    background()
    logo()
    options()

def game():
    running = True
    while running:
        screen.fill(mainCOLOR)
    
        background()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        pygame.display.update()
 
def credit():
    rollPos = 800
    rollMove = 1
    
    running = True
    while running:
        screen.fill(mainCOLOR)

        #credits
        background()
        creditImg = pygame.image.load('credits.png')
        screen.blit(creditImg, [100,rollPos])

        rollPos-=rollMove
        if rollPos == 25:
            rollMove = 0
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        
        pygame.display.update()
    
move = 0.25

#main 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    menu()
    xText1 += move
    if xText1 == pxText1:
        move = -0.25
    if xText1 == nxText1:
        move = 0.25
    xText2 += move
    if xText2 == xText2+15:
        move = -0.25
    if xText2 == xText2-15:
        move = 0.25
    xShield += move
    if xShield == xShield+15:
        move = -0.25
    if xShield == xShield-15:
        move = 0.25
    #mouse hovering
    pos = pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]
    #start hover
    if x >= 365 and x <= 630 and y >=170 and y<=260:
        hoverColor = GOLD
    else:
        hoverColor = WHITE
    #credits hover
    if x >= 365 and x <= 630 and y >=265 and y<=355:
        hoverColor2 = GOLD
    else:
        hoverColor2 = WHITE
    #quit hover
    if x >= 365 and x <= 630 and y >=360 and y<=450:
        hoverColor3 = GOLD
    else:
        hoverColor3 = WHITE
    #start
    if event.type == pygame.MOUSEBUTTONDOWN and x >= 365 and x <= 630 and y >=170 and y<=260:
        buttons = pygame.mouse.get_pressed()
        if buttons[0] == True:
            oColor = optionCOLORL
    else:
        oColor = optionCOLOR
    if event.type == pygame.MOUSEBUTTONUP and x >= 365 and x <= 630 and y >=170 and y<=260:
        if buttons[0] == True:
            game()
    #credits
    if event.type == pygame.MOUSEBUTTONDOWN and x >= 365 and x <= 630 and y >=265 and y<=355:
        buttons = pygame.mouse.get_pressed()
        if buttons[0] == True:
            oColor2 = optionCOLORL
    else:
        oColor2 = optionCOLOR
    if event.type == pygame.MOUSEBUTTONUP and x >= 365 and x <= 630 and y >=265 and y<=355:
        if buttons[0] == True:
            credit()
    #quit
    if event.type == pygame.MOUSEBUTTONDOWN and x >= 365 and x <= 630 and y >=360 and y<=450:
        buttons = pygame.mouse.get_pressed()
        if buttons[0] == True:
            oColor3 = optionCOLORL
    else:
        oColor3 = optionCOLOR
    if event.type == pygame.MOUSEBUTTONUP and x >= 365 and x <= 630 and y >=360 and y<=450:
            pygame.quit()
            sys.exit()
    pygame.display.update()
