import pygame
import ranks

pygame.init()


#Define screen size
(width, height) = (750, 750)
myFont = pygame.font.SysFont("Algerian", 50)
myFont1 = pygame.font.SysFont("Algerian", 30)
myFont2 = pygame.font.SysFont("Times New Roman", 20)
startLabel = myFont.render("Start", 1, (255, 215, 0))
howToLabel = myFont1.render("How To Play", 1, (255, 215, 0))
backLabel = myFont1.render("Back to Start", 1, (255, 215, 0))
rulesText = myFont2.render("Stratego is a game in which you need to capture the flag of your", 1, (255, 215, 0))
rulesText2 = myFont2.render("opponent while defending your own flag. To capture the flag you", 1, (255, 215, 0))
rulesText3 = myFont2.render("use your army of 20 pieces. Pieces have a rank and represent", 1, (255, 215, 0))
rulesText4 = myFont2.render("individual officers and soldiers in an army. In addition to those", 1, (255, 215, 0))
rulesText5 = myFont2.render("ranked pieces you can use bombs to protect your flag.", 1, (255, 215, 0))
rulesText6 = myFont2.render("You can capture the other flag by attacking the other team's", 1, (255, 215, 0))
rulesText7 = myFont2.render("units. When attacking, the unit with the higher rank wins. But,", 1, (255, 215, 0))
rulesText8 = myFont2.render("there are exceptions to the rule. The spy, which has a rank of 1,", 1, (255, 215, 0))
rulesText9 = myFont2.render(" can beat the rank of 10. The miners, which have a rank of 3, can", 1, (255, 215, 0))
rulesText10 = myFont2.render("disarm a bomb. Also, each unit can only move 1 space. But, the", 1, (255, 215, 0))
rulesText11 = myFont2.render("scout, which has a rank of 2, can move any number of spaces.", 1, (255, 215, 0))
pygame.mixer.music.load("Sounds/introMusic.mp3")

#Load images/colors onto screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Stratego")
board = pygame.image.load("Images/strategoBoard.jpg")
logo = pygame.image.load("Images/newStrategoLogo.png")
blueCover = pygame.image.load("Images/blueCover.png")
redCover = pygame.image.load("Images/redCover.png")
strategoHowTo = pygame.image.load("Images/strategoHowTo.jpg")
introScreen = pygame.display.set_mode((width, height))
howToScreen = pygame.display.set_mode((width, height))
winScreen = pygame.display.set_mode((width, height))
screen.convert()

def setupUnits():

    #--Blue Units--#

    blueFlag = ranks.RankFlag(0, 0, "blue")
    ranks.allUnits.add(blueFlag)
    ranks.blueUnits.add(blueFlag)

    blueSpy = ranks.RankSpy(6, 1, "blue")
    ranks.allUnits.add(blueSpy)
    ranks.blueUnits.add(blueSpy)

    blueBomb_0 = ranks.RankBomb(0, 1, "blue")
    ranks.allUnits.add(blueBomb_0)
    ranks.blueUnits.add(blueBomb_0)

    blueBomb_1 = ranks.RankBomb(1, 1, "blue")
    ranks.allUnits.add(blueBomb_1)
    ranks.blueUnits.add(blueBomb_1)

    blueBomb_2 = ranks.RankBomb(5, 1, "blue")
    ranks.allUnits.add(blueBomb_2)
    ranks.blueUnits.add(blueBomb_2)

    blue2_0 = ranks.Rank2(3, 0, "blue")
    ranks.allUnits.add(blue2_0)
    ranks.blueUnits.add(blue2_0)

    blue2_1 = ranks.Rank2(8, 0, "blue")
    ranks.allUnits.add(blue2_1)
    ranks.blueUnits.add(blue2_1)

    blue2_2 = ranks.Rank2(9, 0, "blue")
    ranks.allUnits.add(blue2_2)
    ranks.blueUnits.add(blue2_2)

    blue3_0 = ranks.Rank3(7, 0, "blue")
    ranks.allUnits.add(blue3_0)
    ranks.blueUnits.add(blue3_0)

    blue3_1 = ranks.Rank3(3, 1, "blue")
    ranks.allUnits.add(blue3_1)
    ranks.blueUnits.add(blue3_1)

    blue4_0 = ranks.Rank4(4, 0, "blue")
    ranks.allUnits.add(blue4_0)
    ranks.blueUnits.add(blue4_0)

    blue4_1 = ranks.Rank4(7, 1, "blue")
    ranks.allUnits.add(blue4_1)
    ranks.blueUnits.add(blue4_1)

    blue5_0 = ranks.Rank5(2, 0, "blue")
    ranks.allUnits.add(blue5_0)
    ranks.blueUnits.add(blue5_0)

    blue6_0 = ranks.Rank6(1, 0, "blue")
    ranks.allUnits.add(blue6_0)
    ranks.blueUnits.add(blue6_0)

    blue6_1 = ranks.Rank6(5, 0, "blue")
    ranks.allUnits.add(blue6_1)
    ranks.blueUnits.add(blue6_1)

    blue7 = ranks.Rank7(6, 0, "blue")
    ranks.allUnits.add(blue7)
    ranks.blueUnits.add(blue7)

    blue8_0 = ranks.Rank8(2, 1, "blue")
    ranks.allUnits.add(blue8_0)
    ranks.blueUnits.add(blue8_0)

    blue8_1 = ranks.Rank8(9, 1, "blue")
    ranks.allUnits.add(blue8_1)
    ranks.blueUnits.add(blue8_1)

    blue9 = ranks.Rank9(4, 1, "blue")
    ranks.allUnits.add(blue9)
    ranks.blueUnits.add(blue9)

    blue10 = ranks.Rank10(8, 1, "blue")
    ranks.allUnits.add(blue10)
    ranks.blueUnits.add(blue10)

    #--Red Units--#

    redFlag = ranks.RankFlag(0, 9, "red")
    ranks.allUnits.add(redFlag)
    ranks.redUnits.add(redFlag)

    redSpy = ranks.RankSpy(9, 8, "red")
    ranks.allUnits.add(redSpy)
    ranks.redUnits.add(redSpy)

    redBomb_0 = ranks.RankBomb(0, 8, "red")
    ranks.allUnits.add(redBomb_0)
    ranks.redUnits.add(redBomb_0)

    redBomb_1 = ranks.RankBomb(1, 8, "red")
    ranks.allUnits.add(redBomb_1)
    ranks.redUnits.add(redBomb_1)

    redBomb_2 = ranks.RankBomb(5, 8, "red")
    ranks.allUnits.add(redBomb_2)
    ranks.redUnits.add(redBomb_2)

    red2_0 = ranks.Rank2(8, 8, "red")
    ranks.allUnits.add(red2_0)
    ranks.redUnits.add(red2_0)

    red2_1 = ranks.Rank2(8, 9, "red")
    ranks.allUnits.add(red2_1)
    ranks.redUnits.add(red2_1)

    red2_2 = ranks.Rank2(3, 8, "red")
    ranks.allUnits.add(red2_2)
    ranks.redUnits.add(red2_2)

    red3_0 = ranks.Rank3(4, 9, "red")
    ranks.allUnits.add(red3_0)
    ranks.redUnits.add(red3_0)

    red3_1 = ranks.Rank3(7, 9, "red")
    ranks.allUnits.add(red3_1)
    ranks.redUnits.add(red3_1)

    red4_0 = ranks.Rank4(3, 9, "red")
    ranks.allUnits.add(red4_0)
    ranks.redUnits.add(red4_0)

    red4_1 = ranks.Rank4(5, 9, "red")
    ranks.allUnits.add(red4_1)
    ranks.redUnits.add(red4_1)

    red5 = ranks.Rank5(6, 9, "red")
    ranks.allUnits.add(red5)
    ranks.redUnits.add(red5)

    red6_0 = ranks.Rank6(1, 9, "red")
    ranks.allUnits.add(red6_0)
    ranks.redUnits.add(red6_0)

    red6_1 = ranks.Rank6(6, 8, "red")
    ranks.allUnits.add(red6_1)
    ranks.redUnits.add(red6_1)

    red7 = ranks.Rank7(2, 9, "red")
    ranks.allUnits.add(red7)
    ranks.redUnits.add(red7)

    red8_0 = ranks.Rank8(2, 8, "red")
    ranks.allUnits.add(red8_0)
    ranks.redUnits.add(red8_0)

    red8_1 = ranks.Rank8(9, 9, "red")
    ranks.allUnits.add(red8_1)
    ranks.redUnits.add(red8_1)

    red9 = ranks.Rank9(4, 8, "red")
    ranks.allUnits.add(red9)
    ranks.redUnits.add(red9)

    red10 = ranks.Rank10(7, 8, "red")
    ranks.allUnits.add(red10)
    ranks.redUnits.add(red10)


def printRow():
    for row in ranks.grid:
        print(row)            

#Main Functions
setupUnits()
#player1 = True

for unit in ranks.allUnits:
    row, col = unit.getPos()
    ranks.grid[col][row] += 1
printRow()

#buttons for start menu
#startButton = pygame.draw.rect(introScreen, (250, 250, 250), (width/2 - 100, height/2 - 105, 200, 50))
#howToButton = pygame.draw.rect(introScreen, (250, 250, 250), (width/2 - 100, height/2 - 45, 200, 50))


def intro():
    pygame.init()
    intro = True
    
    while intro:
        
        introScreen.fill((0, 0, 128))
        introScreen.blit(logo, (0,559))
        startButton = pygame.draw.rect(introScreen, (128, 0, 0), (width/2 - 100, height/2 - 105, 200, 50))
        howToButton = pygame.draw.rect(introScreen, (128, 0, 0), (width/2 - 100, height/2 - 45, 200, 50))
        introScreen.blit(startLabel, (width/2 - 80, height/2 - 105))
        introScreen.blit(howToLabel, (width/2 - 95, height/2 - 35))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if startButton.collidepoint(pos):
                    print("start")
                    gameloop()
                elif howToButton.collidepoint(pos):
                    howToPlay()
                    print("How To play")

def howToPlay():
    pygame.init()
    howTo = True

    while howTo:
        
        howToScreen.fill((128, 0, 0))
        backButton = pygame.draw.rect(howToScreen, (0, 0, 128), (25, 25, 250, 50))
        howToScreen.blit(backLabel, (35, 35))
        howToScreen.blit(rulesText, (35, 100))
        howToScreen.blit(rulesText2, (35, 125))
        howToScreen.blit(rulesText3, (35, 150))
        howToScreen.blit(rulesText4, (35, 175))
        howToScreen.blit(rulesText5, (35, 200))
        howToScreen.blit(rulesText6, (35, 250))
        howToScreen.blit(rulesText7, (35, 275))
        howToScreen.blit(rulesText8, (35, 300))
        howToScreen.blit(rulesText9, (35, 325))
        howToScreen.blit(rulesText10, (35, 350))
        howToScreen.blit(rulesText11, (35, 375))
        howToScreen.blit(strategoHowTo, (width/2 - 250, 425))
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if backButton.collidepoint(pos):
                    print("Back to Main Menu")
                    intro()

        


def gameloop():
    player1 = True #blue team is player1
    pygame.mixer.music.fadeout(5)
    
    while True:
        if ranks.didWin == True:
            win()

        
        for unit in ranks.allUnits:
            if player1 == True:
                    if unit.team == "red":
                        unit.image = redCover
                    else:
                        unit.image = pygame.image.load(unit.baseImage)
            elif player1 == False:
                    if unit.team == "blue":
                        unit.image = blueCover
                    else:
                        unit.image = pygame.image.load(unit.baseImage)

        screen.blit(board, (0, 0))
        ranks.allUnits.draw(screen)
        pygame.display.flip()

        for event in pygame.event.get():
            for unit in ranks.allUnits:

                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:

                    if unit.selected == True:
                        print(unit.getPos())
                        unit.update()
                        if player1 == True and unit.moved == True:
                            player1 = False
                        elif player1 == False and unit.moved == True:
                            player1 = True
                        printRow()
                    else:
                        unit.selectUnit()
                    print(unit.selected)

pygame.mixer.music.play(1)
intro()

