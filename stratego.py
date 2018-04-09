import pygame

background_colour = (0, 0, 128)
(width, height) = (500, 500)
squareWidth = 50
squareHeight = 50
grid = []


screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Stratego")
board = pygame.image.load("Images/strategoBoard.jpg")
#logo = pygame.image.load("Images/strategoLogo.png")
screen.fill(background_colour)
screen.convert()

allUnits = pygame.sprite.Group()
blueUnits = pygame.sprite.Group()
redUnits = pygame.sprite.Group()



#Super Class
class Unit(pygame.sprite.Sprite):

    def __init__(self, row, col):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("Images/blueCover.png")
        self.rect = self.image.get_rect()
        self.rect.x = (row * squareWidth) + 3 #intialize with grid coords - convert to x, y
        self.rect.y = (col * squareHeight) + 3
        self.selected = False

    def getPos(self):
        return self.rect.x, self.rect.y

    
    def update(self):
        if self.selected == True:
            mx, my = pygame.mouse.get_pos()

            row = mx // (squareWidth)
            col = my // (squareHeight)

            self.rect.x = (row * squareWidth) + 3
            self.rect.y = (col * squareHeight) + 3

        else:
            return

    def selectUnit(self):
        mx, my = pygame.mouse.get_pos()
        x = self.rect.x
        y = self.rect.y
        #print("Coords:", x, y, mx, my)
        
        if x <= mx <= x + 40 and y <= my < y + 40:
            self.selected = True
        
        else:
            self.selected = False


#Sub Classes

class Rank2(Unit):

    def __init__(self, x, y, team):

        Unit.__init__(self, x, y)
        self.rank = 2
        self.team = team
        
        if self.team == "blue":
            self.image = pygame.image.load("Units/BlueUnits/blueRank2.jpg")
        elif self.team == "red":
            self.image = pygame.image.load("Units/RedUnits/redRank2.jpg")


class Rank3(Unit):

    def __init__(self, x, y, team):

        Unit.__init__(self, x, y)
        self.rank = 3
        self.team = team
        
        if self.team == "blue":
            self.image = pygame.image.load("Units/BlueUnits/blueRank3.jpg")
        elif self.team == "red":
            self.image = pygame.image.load("Units/RedUnits/redRank3.jpg")

class Rank4(Unit):

    def __init__(self, x, y, team):

        Unit.__init__(self, x, y)
        self.rank = 4
        self.team = team
        
        if self.team == "blue":
            self.image = pygame.image.load("Units/BlueUnits/blueRank4.jpg")
        elif self.team == "red":
            self.image = pygame.image.load("Units/RedUnits/redRank4.jpg")

class Rank5(Unit):

    def __init__(self, x, y, team):

        Unit.__init__(self, x, y)
        self.rank = 5
        self.team = team
        
        if self.team == "blue":
            self.image = pygame.image.load("Units/BlueUnits/blueRank5.jpg")
        elif self.team == "red":
            self.image = pygame.image.load("Units/RedUnits/redRank5.jpg")

class Rank6(Unit):

    def __init__(self, x, y, team):

        Unit.__init__(self, x, y)
        self.rank = 6
        self.team = team
        
        if self.team == "blue":
            self.image = pygame.image.load("Units/BlueUnits/blueRank6.jpg")
        elif self.team == "red":
            self.image = pygame.image.load("Units/RedUnits/redRank6.jpg")
        

class Rank7(Unit):

    def __init__(self, x, y, team):

        Unit.__init__(self, x, y)
        self.rank = 7
        self.team = team
        
        if self.team == "blue":
            self.image = pygame.image.load("Units/BlueUnits/blueRank7.jpg")
        elif self.team == "red":
            self.image = pygame.image.load("Units/RedUnits/redRank7.jpg")

class Rank8(Unit):
    
    def __init__(self, x, y, team):

        Unit.__init__(self, x, y)
        self.rank = 8
        self.team = team
        
        if self.team == "blue":
            self.image = pygame.image.load("Units/BlueUnits/blueRank8.jpg")
        elif self.team == "red":
            self.image = pygame.image.load("Units/RedUnits/redRank8.jpg")

class Rank9(Unit):

    def __init__(self, x, y, team):

        Unit.__init__(self, x, y)
        self.rank = 9
        self.team = team
        
        if self.team == "blue":
            self.image = pygame.image.load("Units/BlueUnits/blueRank9.jpg")
        elif self.team == "red":
            self.image = pygame.image.load("Units/RedUnits/redRank9.jpg")

class Rank10(Unit):
    
    def __init__(self, x, y, team):

        Unit.__init__(self, x, y)
        self.rank = 10
        self.team = team
        
        if self.team == "blue":
            self.image = pygame.image.load("Units/BlueUnits/blueRank10.jpg")
        elif self.team == "red":
            self.image = pygame.image.load("Units/RedUnits/redRank10.jpg")

class RankBomb(Unit):
    
    def __init__(self, x, y, team):

        Unit.__init__(self, x, y)
        self.rank = 11
        self.team = team
        
        if self.team == "blue":
            self.image = pygame.image.load("Units/BlueUnits/blueRankBomb.jpg")
        elif self.team == "red":
            self.image = pygame.image.load("Units/RedUnits/redRankBomb.jpg")


class RankSpy(Unit):
    
    def __init__(self, x, y, team):

        Unit.__init__(self, x, y)
        self.rank = 1
        self.team = team
        
        if self.team == "blue":
            self.image = pygame.image.load("Units/BlueUnits/blueRankSpy.jpg")
        elif self.team == "red":
            self.image = pygame.image.load("Units/RedUnits/redRankSpy.jpg")

class RankFlag(Unit):
    
    def __init__(self, x, y, team):

        Unit.__init__(self, x, y)
        self.rank = 0
        self.team = team

        if self.team == "blue":
            self.image = pygame.image.load("Units/BlueUnits/blueRankFlag.jpg")
        elif self.team == "red":
            self.image = pygame.image.load("Units/RedUnits/redRankFlag.jpg")
            

def setupUnits():

    #--Blue Units--#

    blueFlag = RankFlag(0, 0, "blue")
    allUnits.add(blueFlag)
    blueUnits.add(blueFlag)

    blueSpy = RankSpy(1, 0, "blue")
    allUnits.add(blueSpy)
    blueUnits.add(blueSpy)

    blueBomb = RankBomb(2, 0, "blue")
    allUnits.add(blueBomb)
    blueUnits.add(blueBomb)

    blue2 = Rank2(3, 0, "blue")
    allUnits.add(blue2)
    blueUnits.add(blue2)

    blue3 = Rank3(4, 0, "blue")
    allUnits.add(blue3)
    blueUnits.add(blue3)

    blue4 = Rank4(5, 0, "blue")
    allUnits.add(blue4)
    blueUnits.add(blue4)

    blue5 = Rank5(6, 0, "blue")
    allUnits.add(blue5)
    blueUnits.add(blue5)

    blue6 = Rank6(7, 0, "blue")
    allUnits.add(blue6)
    blueUnits.add(blue6)

    blue7 = Rank7(8, 0, "blue")
    allUnits.add(blue7)
    blueUnits.add(blue7)

    blue8 = Rank8(9, 0, "blue")
    allUnits.add(blue8)
    blueUnits.add(blue8)

    blue9 = Rank9(4, 1, "blue")
    allUnits.add(blue9)
    blueUnits.add(blue9)

    blue10 = Rank10(5, 1, "blue")
    allUnits.add(blue10)
    blueUnits.add(blue10)

    #--Red Units--#

    redFlag = RankFlag(0, 9, "red")
    allUnits.add(redFlag)
    redUnits.add(redFlag)

    redSpy = RankSpy(1, 9, "red")
    allUnits.add(redSpy)
    redUnits.add(redSpy)

    redBomb = RankBomb(2, 9, "red")
    allUnits.add(redBomb)
    redUnits.add(redBomb)

    red2 = Rank2(3, 9, "red")
    allUnits.add(red2)
    redUnits.add(red2)

    red3 = Rank3(4, 9, "red")
    allUnits.add(red3)
    redUnits.add(red3)

    red4 = Rank4(5, 9, "red")
    allUnits.add(red4)
    redUnits.add(red4)

    red5 = Rank5(6, 9, "red")
    allUnits.add(red5)
    redUnits.add(red5)

    red6 = Rank6(7, 9, "red")
    allUnits.add(red6)
    redUnits.add(red6)

    red7 = Rank7(8, 9, "red")
    allUnits.add(red7)
    redUnits.add(red7)

    red8 = Rank8(9, 9, "red")
    allUnits.add(red8)
    redUnits.add(red8)

    red9 = Rank9(4, 8, "red")
    allUnits.add(red9)
    redUnits.add(red9)

    red10 = Rank10(5, 8, "red")
    allUnits.add(red10)
    redUnits.add(red10)


    


#Create the grid -- 0 means no Unit occupies, 1 means one Unit occupies
for row in range(10):
    grid.append([])
    for col in range(10):
        grid[row].append(0)
print(grid)



setupUnits()


running = True
while running:

    #screen.blit(logo, (0,0))
    screen.blit(board, (0, 0))
    allUnits.draw(screen)
    pygame.display.flip()

    for event in pygame.event.get():
        for unit in allUnits:
    
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row = pos[0] // (squareWidth)
                column = pos[1] // (squareHeight)
                #print("row, col:", row, column)                
                
                
                unit.update()
                if unit.selected == False:
                    unit.selectUnit()
                
                #print(unit.selected)
