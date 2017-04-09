from random import randint

import pygame
from copy import deepcopy

from gagaframe.shows.base import BaseShow
from gagaframe.utils import SIZE

POPULATED = 1
EMPTY = 0

POPULATED_COLOR = (255, 255, 255)
EMPTY_COLOR = (0, 0, 0)
TIME_BETWEEN_UPDATE = 250


class LifeShow(BaseShow):
    def init_map(self):
        self.map = [0] * SIZE[1]
        for y in range(SIZE[1]):
            self.map[y] = [0] * SIZE[0]
            for x in range(SIZE[0]):
                self.map[y][x] = randint(0, 1)

    def initialize(self):
        self.next_update_time = 0
        self.init_map()

    def reset(self):
        self.init_map()

    def print_map(self):
        self.screen.fill((0, 0, 0))
        for y in range(SIZE[1]):
            for x in range(SIZE[0]):
                if self.map[y][x] == POPULATED:
                    self.screen.set_at((x, y), POPULATED_COLOR)
        pygame.display.flip()

    def get_point(self, x, y):
        x = (x + SIZE[0]) % SIZE[0]
        y = (y + SIZE[1]) % SIZE[1]
        return x, y

    def get_point_value(self, x, y):
        points = [
            self.get_point(x - 1, y),
            self.get_point(x + 1, y),
            self.get_point(x, y - 1),
            self.get_point(x, y + 1),
            self.get_point(x - 1, y - 1),
            self.get_point(x - 1, y + 1),
            self.get_point(x + 1, y - 1),
            self.get_point(x + 1, y + 1)
        ]
        return sum([self.map[y][x] for x, y in points])

    def update_map(self):
        new_map = deepcopy(self.map)
        for y in range(SIZE[1]):
            for x in range(SIZE[0]):
                point_value = self.get_point_value(x, y)
                if self.map[y][x] == POPULATED:
                    if point_value < 2 or point_value > 3:
                        new_map[y][x] = EMPTY
                else:
                    if point_value == 3:
                        new_map[y][x] = POPULATED
        self.map = new_map

    def run(self, event=None):
        current_time = pygame.time.get_ticks()
        if current_time >= self.next_update_time:
            self.update_map()
            self.print_map()
            self.next_update_time = current_time + TIME_BETWEEN_UPDATE
