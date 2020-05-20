import random

from cell import Cell


class Board:
    def __init__(self, x_size: int, y_size: int, points_count: int):
        self.x_size = x_size
        self.y_size = y_size
        self.food_cells = list(map(
            lambda _: Cell(self.random_pos(), 1000),
            range(1, points_count)))

    def random_pos(self) -> (int, int):
        return random.randrange(self.x_size), random.randrange(self.y_size)

    def detect_collisions(self, player: Cell):
        new_food_cells = []
        for cell in self.food_cells:
            if cell.distance(player) < cell.radius + player.radius:
                player.volume += cell.volume
            else:
                new_food_cells.append(cell)
        self.food_cells = new_food_cells

    def find_closest_cell(self, player: Cell) -> Cell:
        return sorted(self.food_cells, key=lambda cell: cell.distance(player))[0]
