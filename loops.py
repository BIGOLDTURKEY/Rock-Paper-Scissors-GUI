import pygame
import button
import random
from svg.path import parse_path


pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((1280, 720))

one = pygame.image.load("number-1.png")
two = pygame.image.load("number-2.png")
three = pygame.image.load("number-3.png")
#four = pygame.image.load("number-4.png")
#five = pygame.image.load("number-5.png")

def roundloop():
        
    b1 = button.Button(128, 232, one, "white")
    b2 = button.Button(512, 232, two, "white")
    b3 = button.Button(896, 232, three, "white")
    
    rfont = pygame.font.Font("freesansbold.ttf", 64)
    rtext = rfont.render("How many rounds do you want to play? ", True, "black", "white")
    rtext_rect = rtext.get_rect()
    rtext_rect.center = (640, 100)
    
    run = True
    while run:
                
        clock.tick(60)
                
        screen.fill("white")
        
        screen.blit(rtext, rtext_rect)
        
        b1.button_show()
        b2.button_show()
        b3.button_show()
        
        mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b1.rect.collidepoint(mouse_pos):
                    global rounds 
                    rounds = 1
                    run = False
                if b2.rect.collidepoint(mouse_pos):
                    rounds = 2
                    run = False
                if b3.rect.collidepoint(mouse_pos):
                    rounds = 3
                    run = False
                
        pygame.display.update()

rock = pygame.image.load("rock.png")
paper = pygame.image.load("paper.png")
scissors = pygame.image.load("scissors.png")

rockb = button.Button(150, 280, rock, "white")
papb = button.Button(512, 280, paper, "white")
scib = button.Button(874, 280, scissors, "white")

font = pygame.font.Font("freesansbold.ttf", 64)
text = font.render("What will you play?", True, "black", "white")
text_rect = text.get_rect()
text_rect.center = (640, 100)

def choiceloop():
    run = True
    while run:
        
        clock.tick(60)
        
        screen.fill("white")

        screen.blit(text, text_rect)
        
        rockb.button_show()
        papb.button_show()
        scib.button_show()
        
        mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rockb.rect.collidepoint(mouse_pos):
                    global pc
                    pc = rock
                    run = False
                elif papb.rect.collidepoint(mouse_pos):
                    pc = paper
                    screen.fill((255, 255, 255))
                    run = False
                elif scib.rect.collidepoint(mouse_pos):
                    pc = scissors
                    screen.fill((255, 255, 255))
                    run = False
            
            
        pygame.display.update()
 
start_list = ["Rock...", "Paper...", "Scissors...", "Shoot!"]
        
def startloop():
    for i in range(4):
                
        screen.fill("white")
        
        font1 = pygame.font.Font("freesansbold.ttf", 128)
        text1 = font1.render(start_list[i], True, "black", "white")
        text_rect1 = text1.get_rect()
        text_rect1.center = (640, 360)
        screen.blit(text1, text_rect1)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        pygame.display.update()
        pygame.time.delay(1000)

next = pygame.image.load("right-arrow.png")
nextb = button.Button(1100, 570, next, "white")

close = pygame.image.load("close.png")
closeb = button.Button(50, 570, close, "white")

c_list = [rock, paper, scissors]

CsToIn = {
    rock: 1,
    paper: 2,
    scissors: 3
}

ppoints = 0
cpoints = 0

font2 = pygame.font.Font("freesansbold.ttf", 64)
text2 = font2.render("Your play", True, "black", "white")
text_rect2 = text2.get_rect()
text_rect2.center = (220, 100)

font3 = pygame.font.Font("freesansbold.ttf", 64)
text3 = font3.render("System's play", True, "black", "white")
text_rect3 = text3.get_rect()
text_rect3.center = (1000, 100)

font4 = pygame.font.Font("freesansbold.ttf", 64)
text4 = font4.render("You win!", True, "black", "white")
text_rect4 = text4.get_rect()
text_rect4.center = (625, 360)
    
font5 = pygame.font.Font("freesansbold.ttf", 64)
text5 = font5.render("You lose!", True, "black", "white")
text_rect5 = text5.get_rect()
text_rect5.center = (625, 360)
    
font6 = pygame.font.Font("freesansbold.ttf", 64)
text6 = font6.render("Draw!", True, "black", "white")
text_rect6 = text6.get_rect()
text_rect6.center = (625, 360)

def resultsloop():
    
    global ppoints
    global cpoints
        
    text2_width, text2_height = font2.size("text2")
        
    pr = button.Button((text_rect2.center[0] - (text2_width/2) - 50), 200, pc, "white")
        
    text3_width, text3_height = font2.size("text3")
    
    compc = random.choice(c_list)
    cr = button.Button((text_rect3.center[0] - (text3_width/2) - 50), 200, compc, "white")
    
    pin = CsToIn[pc]
    cin = CsToIn[compc]
    
    i = 0
    
    run = True
    while run:
        
        clock.tick(60)
        
        screen.fill("white")
        
        screen.blit(text2, text_rect2)
        screen.blit(text3, text_rect3)
        
        pr.result_show()
        cr.result_show()
        
        if pin == 1 and cin == 3:
            if i < 1:   
                ppoints = ppoints + 1
            screen.blit(text4, text_rect4)
        elif pin == 3 and cin == 1:
            if i < 1:
                cpoints = cpoints + 1
            screen.blit(text5, text_rect5)
        elif pin > cin:
            if i < 1:
                ppoints = ppoints + 1
            screen.blit(text4, text_rect4)
        elif pin == cin:
            screen.blit(text6, text_rect6)
        else:
            if i < 1:
                cpoints = cpoints + 1
            screen.blit(text5, text_rect5)   
        
        font7 = pygame.font.Font("freesansbold.ttf", 32)
        text7 = font7.render(f"Player: {str(ppoints)}", True, "black", "white")
        text_rect7 = text7.get_rect()
        text_rect7.center = (625, 500)
        screen.blit(text7, text_rect7)
        
        font8 = pygame.font.Font("freesansbold.ttf", 32)
        text8 = font8.render(f"System: {str(cpoints)}", True, "black", "white")
        text_rect8 = text8.get_rect()
        text_rect8.center = (625, 600)
        screen.blit(text8, text_rect8)
        
        nextb.button_show()
        closeb.button_show()
            
        mouse_pos = pygame.mouse.get_pos()
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if nextb.rect.collidepoint(mouse_pos):
                    run = False
                if closeb.rect.collidepoint(mouse_pos):
                    pygame.quit()

        pygame.display.update()     
        i = 1

font8 = pygame.font.Font("freesansbold.ttf", 64)
text8 = font8.render("Would you like to restart?", True, "black", "white")
text_rect8 = text8.get_rect()
text_rect8.center = (640, 175)

font4a = pygame.font.Font("freesansbold.ttf", 64)
text4a = font4a.render("You win!", True, "black", "white")
text_rect4a = text4a.get_rect()
text_rect4a.center = (640, 50)
    
font5a = pygame.font.Font("freesansbold.ttf", 64)
text5a = font5a.render("You lose!", True, "black", "white")
text_rect5a = text5a.get_rect()
text_rect5a.center = (640, 50)
    
font6a = pygame.font.Font("freesansbold.ttf", 64)
text6a = font6a.render("Draw!", True, "black", "white")
text_rect6a = text6a.get_rect()
text_rect6a.center = (640, 50)

restart = pygame.image.load("restart.png")
restartb = button.Button(182.86, 360, restart, "white")

close1 = pygame.image.load("close.png")
closeb1 = button.Button(969.14, 360, close1, "white")

def restartloop():
    run = True
    while run:
        
        clock.tick(60)
        
        screen.fill("white")
        
        screen.blit(text8, text_rect8)
        
        if ppoints == cpoints:
            screen.blit(text6a, text_rect6a)
        elif ppoints > cpoints:
            screen.blit(text4a, text_rect4a)
        elif ppoints < cpoints:
            screen.blit(text5a, text_rect5a)
        
        closeb1.button_show()
        restartb.button_show()
        
        mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if closeb1.rect.collidepoint(mouse_pos):
                    pygame.quit()
                elif restartb.rect.collidepoint(mouse_pos):
                    run = False
        
        pygame.display.update()
        
        
        