import pygame

background_colour = (0, 0, 128)
(width, height) = (800, 800)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Stratego")
board = pygame.image.load("strategoBoard.jpg")
logo = pygame.image.load("strategoLogo.png")
screen.fill(background_colour)

allUnits = pygame.sprite.Group()
blueUnits = pygame.sprite.Group()
redUnits = pygame.sprite.Group()




class Unit(pygame.sprite.Sprite):

    def __init__(self, x, y):

        pygame.sprite.Sprite.__init__(self)


        self.image = pygame.image.load("Units/BlueUnits/blueRank6.jpg")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def getPos(self):
        return self.rect.x, self.rect.y

    



blue6 = Unit(60, 60)
allUnits.add(blue6)
blueUnits.add(blue6)
#print(blue6.getPos())

allsprites = pygame.sprite.RenderPlain((blue6))

screen.blit(logo, (0,0))
screen.blit(board, (150, 150))
#allsprites.draw(screen)
pygame.display.flip()



running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()



