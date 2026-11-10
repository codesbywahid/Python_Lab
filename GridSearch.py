import pygame  
pygame.init()  
ROWS = 4  
COLS = 4  
CELL_SIZE = 100  
WIDTH = COLS * CELL_SIZE  
HEIGHT = ROWS * CELL_SIZE  
screen = pygame.display.set_mode((WIDTH, HEIGHT))  
pygame.display.set_caption("Grid Search Visualization")  
clock = pygame.time.Clock()  
WHITE = (255, 255, 255)  
BLACK = (0, 0, 0)  
GREEN = (0, 200, 0)  
RED = (220, 0, 0)  
LIGHT_BLUE = (100, 180, 255)  
start = (0, 0)  
goal = (3, 3)  
  
path = [  
    (0, 0),  
    (1, 0),  
    (2, 0),  
    (2, 1),  
    (2, 2),  
    (3, 2),  
    (3, 3)  
] 
def draw_grid():  
    screen.fill(WHITE)  
    for row in range(ROWS):  
        for col in range(COLS):  
            cell = pygame.Rect(  
                col * CELL_SIZE,  
                row * CELL_SIZE,  
                CELL_SIZE,  
                CELL_SIZE  
            ) 
            if (row, col) == start:  
                color = GREEN  
            elif (row, col) == goal:  
                color = RED  
            elif (row, col) in path:  
                color = LIGHT_BLUE  
            else:  
                color = WHITE  
            pygame.draw.rect(screen, color, cell)  
            pygame.draw.rect(screen, BLACK, cell, 2)  
running = True  
while running: 
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            running = False  
    draw_grid()  
    pygame.display.update()  
    clock.tick(30)  
pygame.quit()