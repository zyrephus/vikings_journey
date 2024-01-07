import pygame, sys
from time import * #imports all the time functions
 
# Setup pygame/window
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((1000, 650),0,32) 
pygame.display.set_caption("Viking's Journey")
 
font = pygame.font.SysFont(None, 20)

#-------------------------------------------------------------------------------------------------

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
mainCOLORL = [31,33,41]
detailCOLOR = [21,74,49]
optionCOLOR = [65, 77, 125]
optionCOLORL = [91,101,130]
GOLD = [217,165,9]
lightBlue = [207,248,250]

oColor = optionCOLOR
oColor2 = optionCOLOR
oColor3 = optionCOLOR

#logo variables
xText1 = 160
pxText1 = xText1+15
nxText1 = xText1-15
xText2 = xText1+425
xShield = xText1 + 265

#hover color
hoverColor = WHITE
hoverColor2 = WHITE
hoverColor3 = WHITE

#-------------------------------------------------------------------------------------------------

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

#buttons
def buttons():
    #start
    pygame.draw.line(screen, hoverColor, [410,177],[590,177],5)
    pygame.draw.line(screen, hoverColor, [410,252],[590,252],5)
    pygame.draw.circle(screen, hoverColor, [410,215],40,5)
    pygame.draw.circle(screen, hoverColor, [590,215],40,5)
    pygame.draw.rect(screen, oColor, [410,180,180,70])
    pygame.draw.circle(screen, oColor, [410,215],35)
    pygame.draw.circle(screen, oColor, [590,215],35)
    #credits
    pygame.draw.line(screen, hoverColor2, [410,272],[590,272],5)
    pygame.draw.line(screen, hoverColor2, [410,347],[590,347],5)
    pygame.draw.circle(screen, hoverColor2, [410,310],40,5)
    pygame.draw.circle(screen, hoverColor2, [590,310],40,5)
    pygame.draw.rect(screen, oColor2, [410,275,180,70])
    pygame.draw.circle(screen, oColor2, [410,310],35)
    pygame.draw.circle(screen, oColor2, [590,310],35)
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
    startText = font.render("Start", True, WHITE)
    screen.blit(startText, [445,192])
    font = pygame.font.SysFont('Calibri',50, True, False)
    startText = font.render("Credits", True, WHITE)
    screen.blit(startText, [430,287])
    font = pygame.font.SysFont('Calibri',50, True, False)
    startText = font.render("Quit", True, WHITE)
    screen.blit(startText, [452,382])

#game border/screen
def gameBorder():
    #border
    pygame.draw.line(screen, WHITE, [100,35], [900,35], 18)
    pygame.draw.line(screen, WHITE, [100,535], [900,535], 18)
    pygame.draw.line(screen, WHITE, [100,35], [100,535], 18)
    pygame.draw.line(screen, WHITE, [900,35], [900,535], 18)

def gameScreen():
    pygame.draw.rect(screen, mainCOLORL, [100,35,800,500])

#storyline text
def text1():
    #text 1
    #heading
    font = pygame.font.SysFont('bahnschrift',14, True, False)
    heading1 = font.render("1016", True, WHITE)
    screen.blit(heading1, [120,50])
    #paragraph 1
    font = pygame.font.SysFont('bahnschrift',14, False, False)
    text1_line1 = font.render("The king of Danes in has hired you to take out the set of monsters on a local farm that supports the city. Your name", True, WHITE) 
    screen.blit(text1_line1, [140,75]) #every line is 15 apart and headings are 25 apart
    text1_line2 = font.render("is Birger, a renowned viking. If you fail the mission, the city and its ten thousand citizens will be doomed. Every battle", True, WHITE) 
    screen.blit(text1_line2, [120,90])
    text1_line3 = font.render("is rewarded with gold coins from the local villagers as an expression of gratitude. You can use the cash to attend the", True, WHITE) 
    screen.blit(text1_line3, [120,105])
    text1_line4 = font.render("local market to see the farmer for food and the blacksmith for new weapons and armor.", True, WHITE) 
    screen.blit(text1_line4, [120,120])
    #paragraph 2
    font = pygame.font.SysFont('bahnschrift',14, False, False)
    text1_line5 = font.render("The person behind the creation of the vicious monsters is Helheim. Odin sent her to the Underworld as punishment", True, WHITE)
    screen.blit(text1_line5, [140,135]) #new paragraphs are still 15 apart
    text1_line5 = font.render("and she has risen back to the Overworld to take vengeance on those who wronged her. Helheim will start in Danes, but", True, WHITE)
    screen.blit(text1_line5, [120,150])
    text1_line5 = font.render("she won't stop there; she will destroy the rest of humanity if you don't save the kingdom. You have been blessed by", True, WHITE)
    screen.blit(text1_line5, [120,165])
    text1_line5 = font.render("by Odin to defeat the creatures of Hel. He has granted you immense powers, but you still need to find some tools.", True, WHITE)
    screen.blit(text1_line5, [120,180])
    
def text2():
    #text 2
    #chapter 1:
    font = pygame.font.SysFont('bahnschrift',14, True, False)
    heading1 = font.render("Chapter 1: The Beginning", True, WHITE)
    screen.blit(heading1, [120,50])
    #paragraph 1
    font = pygame.font.SysFont('bahnschrift',14, False, False)
    text1_line1 = font.render("The mysterious lad later told you that his name was Odin, a spirit who chose you in order to save the world. You ", True, WHITE) 
    screen.blit(text1_line1, [140,75]) #every line is 15 apart and headings are 25 apart
    text1_line2 = font.render("then head outside to the town square. His Majesty is already there, along with a crowd of onlookers. He seemed to be", True, WHITE) 
    screen.blit(text1_line2, [120,90])
    text1_line3 = font.render("looking for someone, and you knew that King Canute was trying to find you. ", True, WHITE) 
    screen.blit(text1_line3, [120,105])
    text1_line4 = font.render("local market to see the farmer for food and the blacksmith for new weapons and armor.", True, WHITE) 
    screen.blit(text1_line4, [120,120])

#starting setting
def home():
      homeImg = pygame.image.load('home.png')
      screen.blit(homeImg, [100,35])

# M A I N    M E N U
#-------------------------------------------------------------------------------------------------

click = False
 
def main_menu():
    while True:
        #mouse positions
        mx, my = pygame.mouse.get_pos()

        #option click
        start_1 = pygame.draw.rect(screen, oColor, [410,180,180,70])
        start_2 = pygame.draw.circle(screen, oColor, [410,215],35)
        start_3 = pygame.draw.circle(screen, oColor, [590,215],35)
        credit_1 = pygame.draw.rect(screen, oColor2, [410,275,180,70])
        credit_2 = pygame.draw.circle(screen, oColor2, [410,310],35)
        credit_3 = pygame.draw.circle(screen, oColor2, [590,310],35)
        quit_1 = pygame.draw.rect(screen, oColor3, [410,370,180,70])
        quit_2 = pygame.draw.circle(screen, oColor3, [410,405],35)
        quit_3 = pygame.draw.circle(screen, oColor3, [590,405],35)
        if start_1.collidepoint((mx, my)) or start_2.collidepoint((mx, my)) or start_3.collidepoint((mx, my)):
            if click:
                game()
        if credit_1.collidepoint((mx, my)) or credit_2.collidepoint((mx, my)) or credit_3.collidepoint((mx, my)):
            if click:
                credit()
        if quit_1.collidepoint((mx, my)) or quit_2.collidepoint((mx, my)) or quit_3.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()

        screen.fill(mainCOLOR)
        background()
        logo()
        buttons()

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)

#-------------------------------------------------------------------------------------------------

#variables for button positions
a = 50
b = 560 
c = a+180 
d = b+75 
e = b+38 
f = b+3

# G A M E
#-------------------------------------------------------------------------------------------------

#C H A R A C T E R S
'''
    birgerImg = pygame.image.load('C_birger.png')
    screen.blit(birgerImg, [250,270])
def birgerL():
    birgerImg = pygame.image.load('C_birger.png')
    birgerImg = pygame.transform.flip(birgerImg, True, False)
    screen.blit(birgerImg, [250,270])

def odinR():
    odinImg = pygame.image.load('C_odin.png')
    screen.blit(odinImg, [250,270])

odinImg = pygame.image.load('C_odin.png')
odinImg = pygame.transform.flip(odinImg, True, False)
screen.blit(odinImg, [ox,oy]) 
'''

#text bubble
def textB():
    t1 = pygame.image.load('textBox.png')
    t1 = pygame.transform.scale(t1, [480,180])
    screen.blit(t1, [310,150])

def textBI():
    t1 = pygame.image.load('textBox.png')
    t1 = pygame.transform.scale(t1, [480,180])
    t1 = pygame.transform.flip(t1, True, False)
    screen.blit(t1, [255,130])

#dialogue 1
def d1():
    font = pygame.font.SysFont('bahnschrift',18, True, False)
    oName = font.render("ODIN", True, BLACK)
    screen.blit(oName, [355,180])
    font = pygame.font.SysFont('bahnschrift',11, False, False)
    oName = font.render("Are you ready? Awake! The rumors regarding the destruction of Sir Crosby's", True, BLACK)
    screen.blit(oName, [355,205])
    oName = font.render("fields at the farm were tampered with. King Canute sent four men to scout", True, BLACK)
    screen.blit(oName, [355,220])
    oName = font.render("the area and they returned with appalled faces on each of them.", True, BLACK)
    screen.blit(oName, [355,235])
    font = pygame.font.SysFont('bahnschrift',8, True, False)
    oName = font.render("left click to continue", True, BLACK)
    screen.blit(oName, [660,255])
#dialogue 2
def d2():
    font = pygame.font.SysFont('bahnschrift',18, True, False)
    oName = font.render("ODIN", True, BLACK)
    screen.blit(oName, [355,180])
    font = pygame.font.SysFont('bahnschrift',11, False, False)
    oName = font.render("King Canute is already on his way here. Get ready! This could be your chance!", True, BLACK)
    screen.blit(oName, [355,205])
    font = pygame.font.SysFont('bahnschrift',8, True, False)
    oName = font.render("left click to continue", True, BLACK)
    screen.blit(oName, [660,255])

tx = 310
ty = 160
ty2 = ty+25
tx2 = tx+305
ty3 = ty2+50

#dialogue 3
def d3():
    font = pygame.font.SysFont('bahnschrift',18, True, False)
    oName = font.render("BIRGER", True, BLACK)
    screen.blit(oName, [tx,ty])
    font = pygame.font.SysFont('bahnschrift',11, False, False)
    oName = font.render("WHAT???", True, BLACK)
    screen.blit(oName, [tx,ty2])
    font = pygame.font.SysFont('bahnschrift',8, True, False)
    oName = font.render("press space to continue", True, BLACK)
    screen.blit(oName, [tx2,ty3])

#GAME3
def game3():
    click = False
    running = True
    while running:
        #mouse position
        mx, my = pygame.mouse.get_pos()

        #go back button
        pygame.draw.line(screen, hoverColor3, [a,b],[c,b],5)
        pygame.draw.line(screen, hoverColor3, [a,d],[c,d],5)
        pygame.draw.circle(screen, hoverColor3, [a,e],40,5)
        pygame.draw.circle(screen, hoverColor3, [c,e],40,5)
        quit_1 = pygame.draw.rect(screen, oColor3, [a,f,180,70])
        quit_2 = pygame.draw.circle(screen, oColor3, [a,e],35)
        quit_3 = pygame.draw.circle(screen, oColor3, [c,e],35)
        font = pygame.font.SysFont('Calibri',50, True, False)
        startText = font.render("Go Back", True, WHITE)
        screen.blit(startText, [55,575])
        
        if quit_1.collidepoint((mx, my)) or quit_2.collidepoint((mx, my)) or quit_3.collidepoint((mx, my)):
            if click:
                main_menu()

        #game border/scree
        gameBorder()
        gameScreen()

        text2()

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    click = True
                            
        pygame.display.update()
        mainClock.tick(60) 

#GAME2
def game2():
        
    ox = 740
    oy = 270
    vel = 3
    x = 0
    show = False
    show2 = False
    show3 = False
    click = False
    space = False
    done = False
    
    running = True
    while running:
        #mouse position
        mx, my = pygame.mouse.get_pos()  
            
        screen.fill(mainCOLOR)
        
        background()

        #go back button
        pygame.draw.line(screen, hoverColor3, [a,b],[c,b],5)
        pygame.draw.line(screen, hoverColor3, [a,d],[c,d],5)
        pygame.draw.circle(screen, hoverColor3, [a,e],40,5)
        pygame.draw.circle(screen, hoverColor3, [c,e],40,5)
        quit_1 = pygame.draw.rect(screen, oColor3, [a,f,180,70])
        quit_2 = pygame.draw.circle(screen, oColor3, [a,e],35)
        quit_3 = pygame.draw.circle(screen, oColor3, [c,e],35)
        font = pygame.font.SysFont('Calibri',50, True, False)
        startText = font.render("Go Back", True, WHITE)
        screen.blit(startText, [55,575])
        if quit_1.collidepoint((mx, my)) or quit_2.collidepoint((mx, my)) or quit_3.collidepoint((mx, my)):
            if click:
                main_menu()
                
        #starting setting
        home()
        #game border
        gameBorder()

        #birger and odin
        birgerImg = pygame.image.load('C_birger.png')
        screen.blit(birgerImg, [250,270])
        #odin
        odinImg = pygame.image.load('C_odin.png')
        odinImg = pygame.transform.flip(odinImg, True, False)
        screen.blit(odinImg, [ox,oy])
        ox-=vel

        #DIALOGUE
        if ox <= 626:
            vel = 0
            #dialogue 1
            textB(), d1()
            #dialogue 2
            if click:
                show = True
            if show:
                textB(), d2()
                click = False
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONUP:
                        if event.button == 1:
                            click = True
            #dialogue 3
            if click:
                show2 = True
            if show2:
                home(), gameBorder(), screen.blit(birgerImg, [250,270]), screen.blit(odinImg, [626,270])
                textBI(), d3()
                done = True

        if space:
            if done:
                game3()
                    
        click = False 
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    click = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    space = True
                    
        pygame.display.update()
        mainClock.tick(60)
                    

#GAME
click = False

def game():    
    running = True
    while running:
        #mouse position
        mx, my = pygame.mouse.get_pos()
            
        screen.fill(mainCOLOR)
        
        background()

        #go back button
        pygame.draw.line(screen, hoverColor3, [a,b],[c,b],5)
        pygame.draw.line(screen, hoverColor3, [a,d],[c,d],5)
        pygame.draw.circle(screen, hoverColor3, [a,e],40,5)
        pygame.draw.circle(screen, hoverColor3, [c,e],40,5)
        quit_1 = pygame.draw.rect(screen, oColor3, [a,f,180,70])
        quit_2 = pygame.draw.circle(screen, oColor3, [a,e],35)
        quit_3 = pygame.draw.circle(screen, oColor3, [c,e],35)
        font = pygame.font.SysFont('Calibri',50, True, False)
        startText = font.render("Go Back", True, WHITE)
        screen.blit(startText, [55,575])
        if quit_1.collidepoint((mx, my)) or quit_2.collidepoint((mx, my)) or quit_3.collidepoint((mx, my)):
            if click:
                running = False

        #game border/scree
        gameBorder()
        gameScreen()

        #text
        text1()
        #space to continue
        font = pygame.font.SysFont('Calibri',18, True, False)
        startText = font.render("Press space to continue...", True, WHITE)
        screen.blit(startText, [675,500])   

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    click = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    game2()
                            
        pygame.display.update()
        mainClock.tick(60)
    

# C R E D I T S
#-------------------------------------------------------------------------------------------------

click  = False

def credit():
    rollPos = 800
    rollMove = 1
    
    running = True
    while running:
        try:
            #mouse position
            mx, my = pygame.mouse.get_pos()
            
            screen.fill(mainCOLOR)

            background()

            #go back button
            pygame.draw.line(screen, hoverColor3, [a,b],[c,b],5)
            pygame.draw.line(screen, hoverColor3, [a,d],[c,d],5)
            pygame.draw.circle(screen, hoverColor3, [a,e],40,5)
            pygame.draw.circle(screen, hoverColor3, [c,e],40,5)
            quit_1 = pygame.draw.rect(screen, oColor3, [a,f,180,70])
            quit_2 = pygame.draw.circle(screen, oColor3, [a,e],35)
            quit_3 = pygame.draw.circle(screen, oColor3, [c,e],35)
            font = pygame.font.SysFont('Calibri',50, True, False)
            startText = font.render("Go Back", True, WHITE)
            screen.blit(startText, [55,575])
            if quit_1.collidepoint((mx, my)) or quit_2.collidepoint((mx, my)) or quit_3.collidepoint((mx, my)):
                if click:
                    running = False
            
            #credits
            creditImg = pygame.image.load('credits.png')
            screen.blit(creditImg, [100,rollPos])

            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONUP:
                    if event.button == 1:
                        click = True
            rollPos-=rollMove
            if rollPos == 25:
                rollMove = 0
            
            pygame.display.update()

        except UnboundLocalError:
            print("Restart the program!")
            break
 
main_menu()
