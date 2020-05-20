import pygame

from board import Board
from cell import Cell
from screen_helper import to_screen_pos, to_game_pos


BOARD_SIZE = (5000, 5000)
INITIAL_VOLUME = 40000
INITIAL_VELOCITY = 10

FOOD_COUNT = 200

pygame.init()
pygame.display.set_caption("Cells")
win = pygame.display.set_mode(to_screen_pos(BOARD_SIZE))

board = Board(*BOARD_SIZE, FOOD_COUNT)
player = Cell(board.random_pos(), INITIAL_VOLUME, INITIAL_VELOCITY)
enemy = Cell(board.random_pos(), INITIAL_VOLUME, INITIAL_VELOCITY)
# enemy2 = Cell(board.random_pos(), INITIAL_VOLUME, 20)


def main_loop():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        if board.food_cells == 0:
            return
        pygame.time.delay(2)

        play(player, False)
        play(enemy, True)
        # play(enemy2, True)

        clear_screen()
        draw_cell_and_result(player, (10, 50), (255, 0, 0))
        draw_cell_and_result(enemy, (210, 50), (255, 0, 255))
        # draw_cell_and_result(enemy2, (410, 50), (0, 255, 255))

        for food in board.food_cells:
            draw_cell(food, (0, 255, 0))

        pygame.display.update()


def play(cell, is_ai):
    if is_ai:
        cell.move_into(board.find_closest_cell(cell).position)
    else:
        cell.move_into(to_game_pos(pygame.mouse.get_pos()))
    board.detect_collisions(cell)


def clear_screen():
    win.fill((0, 0, 0))


def draw_cell_and_result(cell, position, color):
    draw_cell(cell, color)
    display_result(cell, position, color)


def draw_cell(cell: Cell, color: (int, int)):
    pygame.draw.circle(win, color, to_screen_pos(cell.position), to_screen_pos(cell.radius))


def display_result(cell: Cell, position: (int, int), color: (int, int, int)):
    myfont = pygame.font.SysFont("Comic Sans MS", 30)
    label = myfont.render(str(cell.volume - INITIAL_VOLUME), 1, color)
    win.blit(label, position)


main_loop()
print("Player: " + str(player.volume))
print("Enemy: " + str(enemy.volume))

pygame.quit()
