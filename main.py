import pygame
import loops 


screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Rock Paper Scissors")

icon = pygame.image.load("rock-paper-scissors.png")
pygame.display.set_icon(icon)

clock = pygame.time.Clock()

t = 0
play = True
while play:
    
    clock.tick(60)
    
    loops.roundloop()
    
    loops.ppoints = 0
    loops.cpoints = 0

    nb = False
    cb = False

    for i in range(loops.rounds):
        if i+1 < loops.rounds:
            nb = True
            cb = True
        elif i+1 == loops.rounds:
            cb = True
            nb = False
        loops.choiceloop()
        loops.startloop()
        loops.resultsloop()
    
    loops.restartloop()
