from __future__ import annotations
import math


class Cell:
    def __init__(self, pos, initial_volume, initial_velocity=0):
        self.x = pos[0]
        self.y = pos[1]
        self.initial_volume = initial_volume
        self.volume = initial_volume
        self.velocity = initial_velocity

    @property
    def position(self) -> tuple:
        return self.x, self.y

    @property
    def radius(self) -> int:
        return int(math.sqrt(self.volume / math.pi))

    def move_into(self, target_pos: tuple):
        angle = math.atan2(target_pos[1] - self.y, target_pos[0] - self.x)
        effective_velocity = self.velocity / self.volume * self.initial_volume
        self.x += effective_velocity * math.cos(angle)
        self.y += effective_velocity * math.sin(angle)

    def distance(self, other: Cell):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
