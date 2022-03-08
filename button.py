import pygame


screen = pygame.display.set_mode((1280, 720))

class Button():
    def __init__(self, x, y, image, bg):
        self.x = x
        self.y = y
        self.image_width = image.get_width()
        self.image_height = image.get_height()
        self.image = image
        self.bg = bg
        self.clicked = False
        
    def button_show(self):
        mouse_pos = pygame.mouse.get_pos()
        self.rect = pygame.Rect(self.x - 12.5, self.y - 12.5, self.image_width + 25, self.image_height + 25)
        if self.rect.collidepoint(mouse_pos):
            self.bg = "light grey"
            self.rect = pygame.draw.rect(screen, self.bg, (self.x - 12.5, self.y - 12.5, self.image_width + 25, self.image_height + 25), 0, 25)
            screen.blit(self.image, (self.x, self.y))
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
        if self.rect.collidepoint(mouse_pos) == False:
            self.bg = "white"
            self.rect = pygame.draw.rect(screen, self.bg, (self.x - 12.5, self.y - 12.5, self.image_width + 25, self.image_height + 25), 0, 25)
            screen.blit(self.image, (self.x, self.y))
    
    def result_show(self):
        screen.blit(self.image, (self.x, self.y))
            

