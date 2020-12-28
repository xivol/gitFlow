import pygame


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.values = [[None] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def get_cell(self, mouse_pos):
        if mouse_pos[0] >= self.left and mouse_pos[0] <= self.width * self.cell_size and \
                mouse_pos[1] >= self.top and mouse_pos[1] <= self.height * self.cell_size:
            x = mouse_pos[0]
            y = mouse_pos[1]
            i = (x - self.left) // self.cell_size
            j = (y - self.top) // self.cell_size
            return (i, j)
        return None

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell is not None:
            self.on_click(self, cell)

    def render(self, screen):
        pygame.draw.rect(screen, 'white',
                         (self.left, self.top, self.width * self.cell_size, self.height * self.cell_size), 1)

        for i in range(self.width):
            for j in range(self.height):
                x = self.left + i * self.cell_size
                y = self.top + j * self.cell_size
                pygame.draw.rect(screen, 'white',
                                 (x, y, self.cell_size, self.cell_size), 1)

        for j in range(self.width):
            for i in range(self.height):
                x = self.left + j * self.cell_size + 1
                y = self.top + i * self.cell_size + 1
                if self.values[i][j] is not None:
                    pygame.draw.rect(screen, self.values[i][j],
                                     (x, y, self.cell_size - 2, self.cell_size - 2), 0)
