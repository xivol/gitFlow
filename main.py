import pygame
from board import Board


def change_value(board, cell):
    i, j = cell
    board.values[j][i] += 1
    board.values[j][i] %= 2


def change_line(board, cell):
    i, j = cell
    board.values[j][i] += 1
    board.values[j][i] %= 2
    for k in range(board.width):
        board.values[j][k] += 1
        board.values[j][k] %= 2
    for l in range(board.height):
        board.values[l][i] += 1
        board.values[l][i] %= 2


def change_color(board, cell):
    j, i = cell
    col = board.values[i][j]
    if col is None:
        board.values[i][j] = 'green'
    elif col == 'blue':
        board.values[i][j] = None
    else:
        board.values[i][j] = 'blue'


if __name__ == "__main__":
    size = width, height = 400, 400
    screen = pygame.display.set_mode(size)

    board = Board(10, 10)
    board.set_view(10, 10, 30)
    board.on_click = change_color

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
