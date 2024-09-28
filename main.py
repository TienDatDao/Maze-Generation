import pygame
import color
import numpy as np
import random
import sys

sys.setrecursionlimit(2000)

pygame.init()


BLOCK = 20
BLOCK_WIDTH = 51
BLOCK_HEIGHT = 51
WIDTH, HEIGHT = BLOCK*BLOCK_WIDTH, BLOCK*BLOCK_HEIGHT

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Draw circle")
FPS = 60

arr_check = [[0 for _ in range(int(WIDTH/BLOCK)+5)] for _ in range(int(HEIGHT/BLOCK)+5)]

def create_table():
    for i in range(1, int(WIDTH/BLOCK)-1):
        for j in range(1, int(HEIGHT/BLOCK)-1):
            if i % 2 == 1 and j % 2 == 1:
                arr_check[i][j] = 1

def delete_wall(x, y, x_, y_):
    if x == x_:
        arr_check[x][int((y+y_)/2)] = 2
    else:
        arr_check[int((x+x_)/2)][y] = 2

def dfs(par_x, par_y, x, y):
    arr_d = [[0,2], [0, -2], [2, 0], [-2, 0]]
    check = True
    while check and len(arr_d) > 0:
        pos = random.randint(0, len(arr_d) - 1)
        x_ = x + arr_d[pos][0]
        y_ = y + arr_d[pos][1]
        if x_ > 0 and x_ < int(WIDTH/BLOCK)-1 and y_ > 0 and y_ < int(HEIGHT/BLOCK)-1 and arr_check[x_][y_] == 1:
            delete_wall(x, y, x_, y_)
            arr_check[x_][y_] = 2
            dfs(x, y, x_, y_)
            # check = False
        arr_d.pop(pos)

    

def draw_window():
    WIN.fill(color.BLACK)

def draw_grid():
    for i in range(0, int(WIDTH/BLOCK)):
        for j in range(0, int(HEIGHT/BLOCK)):
            x = i*BLOCK
            y = j*BLOCK
            if arr_check[i][j] == 0:
                pygame.draw.rect(WIN, color.BLACK, (x, y, BLOCK, BLOCK))
            else:
                pygame.draw.rect(WIN, color.WHITE, (x, y, BLOCK, BLOCK))

def main():
    create_table()
    arr_check[1][1] = 2
    dfs(1, 1, 1, 1)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()

        draw_grid()
        
        pygame.display.flip()

    pygame.quit()

main()
