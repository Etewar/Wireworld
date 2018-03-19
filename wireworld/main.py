import pygame, sys
from pygame.locals import *

pygame.init()
pygame.display.set_caption("Wireworld")

windowWidth = 800
windowHeigth = 800
cell_size = 20
screen = pygame.display.set_mode((windowWidth, windowHeigth))

W = (167, 168, 170)
Y = (239, 249, 32)
O = (249, 111, 32)
B = (32, 79, 249)
G = (30, 30, 30)
screen.fill(G)

def clear_console():
    print("\033[H\033[J")

def input(mouseX, mouseY, events):
    for event in events:
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit(0)
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                App.board[mouseY//cell_size][mouseX//cell_size] = 1
            if event.button == 8:
                App.board[mouseY//cell_size][mouseX//cell_size] = 2
            if event.button == 3:
                App.board[mouseY//cell_size][mouseX//cell_size] = 3
            if event.button == 9:
                App.board[mouseY//cell_size][mouseX//cell_size] = 0

            #if event.button ==
        else:
            #clear_console()
            print(App.board[mouseY//cell_size][mouseX//cell_size])


class App:
    """
    0. empty (gray, G)
    1. electron head (blue, B)
    2. electron tail (orange, O)
    3. conductor (yellow, Y)
    """

    board = [[0 for x in range(0, windowWidth, cell_size)] for y in range(0, windowHeigth, cell_size)]

    def update_board():
        new_board = App.board.copy()

        for y in range(0, windowHeigth//cell_size):
            for x in range(0, windowWidth//cell_size):
                if App.board[y][x] == 0:
                    new_board[y][x] = 0
                    continue
                elif App.board[y][x] == 1:
                    new_board[y][x] = 2
                    continue
                elif App.board[x][y] == 2:
                    new_board[y][x] = 3
                    continue
                elif App.board[y][x] == 3:
                    neighbours = 0
                    continue

                    for h in range(-1, 2):
                        for w in range(-1, 2):
                            if App.board[y+h][x+w] == 1:
                                neighbours += 1

                    if neighbours == 1 or neighbours == 2:
                        new_board[y][x] = 1
                    else:
                        new_board[y][x] = 3
        App.board = new_board.copy()



    def run():
        while True:
            mouseX, mouseY = pygame.mouse.get_pos()
            input(mouseX, mouseY, pygame.event.get())

            App.update_board()

            for y in range(0, windowHeigth//cell_size):
                for x in range(0, windowWidth//cell_size):
                    if App.board[y][x] == 0:
                        pygame.draw.rect(screen, G, (x*cell_size, y*cell_size, cell_size, cell_size))
                    elif App.board[y][x] == 1:
                        pygame.draw.rect(screen, B, (x*cell_size, y*cell_size, cell_size, cell_size))
                    elif App.board[y][x] == 2:
                        pygame.draw.rect(screen, O, (x*cell_size, y*cell_size, cell_size, cell_size))
                    elif App.board[y][x] == 3:
                        pygame.draw.rect(screen, Y, (x*cell_size, y*cell_size, cell_size, cell_size))
                    pygame.draw.rect(screen, W, (x*cell_size, y*cell_size, cell_size, cell_size), 1)


            pygame.time.delay(100)
            pygame.display.update()


if __name__ == "__main__":
    App.run()
