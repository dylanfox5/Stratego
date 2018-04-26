import pygame
 

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
TRANSPARENT = (255, 255, 255, 0)

WIDTH = 50
HEIGHT = 50
 

MARGIN = 0

grid = []
for row in range(10):
    grid.append([])
    for column in range(10):
        grid[row].append(0)
        
pygame.init()
 

WINDOW_SIZE = [500, 500]
screen = pygame.display.set_mode(WINDOW_SIZE)
board = pygame.image.load("strategoBoard.jpg")
 

pygame.display.set_caption("Array Backed Grid")
 

done = False
 

clock = pygame.time.Clock()
 

while not done:
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            done = True  
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            grid[row][column] = 1
            print("Click ", pos, "Grid coordinates: ", row, column)
 
    #screen.fill(BLACK)
    #screen.blit(board, (0, 0))
 
    for row in range(10):
        for column in range(10):
            color = TRANSPARENT
            if grid[row][column] == 1:
                color = GREEN
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])

    screen.blit(board, (0, 0))
    clock.tick(60)
 
    pygame.display.flip()
 
pygame.quit()
