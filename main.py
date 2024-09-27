import pygame
import color
import numpy as np
import random

pygame.init()

BLOCK = 10
WIDTH, HEIGHT = BLOCK*21, BLOCK*21

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Draw circle")
FPS = 60

arr_check = [[0 for _ in range(int(WIDTH/BLOCK))] for _ in range(int(HEIGHT/BLOCK))]

# save wall cells
vector_wall = []  

# save par path cells
vector_path = [[[-1, -1] for _ in range(int(WIDTH/BLOCK))] for _ in range(int(HEIGHT/BLOCK))]

# def delete_wall_cell(x, y):
    

def create_table():
    for i in range(0, int(WIDTH/BLOCK)):
        arr_check[i][0] = 1
    
    for j in range(0, int(HEIGHT/BLOCK)):
        arr_check[0][j] = 1

    for i in range(0, int(WIDTH/BLOCK)):
        arr_check[i][int(WIDTH/BLOCK)-1] = 1
    
    for j in range(0, int(HEIGHT/BLOCK)):
        arr_check[int(WIDTH/BLOCK)-1][j] = 1

    for i in range(1, int(WIDTH/BLOCK)-1):
        for j in range(1, int(HEIGHT/BLOCK)-1):
            if i % 2 == 1 and j % 2 == 1:
                arr_check[i][j] = 0
                vector_path[i][j] = [i, j]
            else:
                arr_check[i][j] = 1
                vector_wall.append([i, j])


def random_delete_wall():
    while len(vector_wall):

        pos = random.randint(0,len(vector_wall)-1)
        x = vector_wall[pos][0]
        y = vector_wall[pos][1]
        vector_wall.pop(pos)

        # if delete_wall_cell(x, y):
            # arr_check[x][y] = 0


def draw_window():
    WIN.fill(color.BLACK)

def draw_grid():
    for i in range(0, int(WIDTH/BLOCK)):
        for j in range(0, int(HEIGHT/BLOCK)):
            x = i*BLOCK
            y = j*BLOCK
            if arr_check[i][j] == 0:
                pygame.draw.rect(WIN, color.WHITE, (x, y, BLOCK, BLOCK))
            else:
                pygame.draw.rect(WIN, color.BLACK, (x, y, BLOCK, BLOCK))

def main():
    create_table()
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()
        random_delete_wall()
        draw_grid()
        
        pygame.display.flip()

    pygame.quit()

main()