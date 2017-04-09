import os
import random

import pygame

from gagaframe.shows.base import BaseShow
from gagaframe.utils import scale_keep_ratio, SIZE, get_center_topleft_coord

ALLOWED_EXTENSIONS = ['.jpg', '.jpeg']
TIME_BETWEEN_PICTURES = 1000 * 5 * 60


class PictureShow(BaseShow):
    def load_pictures(self):
        self.pictures = []
        self.current_picture = 0
        for picture in os.listdir(self.directory):
            if not any([picture.endswith(extension) for extension in ALLOWED_EXTENSIONS]):
                continue
            self.pictures.append(os.path.join(self.directory, picture))
        random.shuffle(self.pictures)

    def initialize(self, options, args):
        self.directory = options.picture_directory
        self.next_update_time = 0
        self.load_pictures()

    def reset(self):
        self.load_pictures()

    def get_picture(self):
        picture = pygame.image.load(self.pictures[self.current_picture]).convert()
        picture = scale_keep_ratio(picture, SIZE)
        return picture

    def update_picture(self):
        picture = self.get_picture()
        self.screen.fill((0, 0, 0))
        self.screen.blit(picture, get_center_topleft_coord(SIZE, picture.get_size()))
        pygame.display.flip()
        self.next_update_time = pygame.time.get_ticks() + TIME_BETWEEN_PICTURES

    def run(self, event=None):
        if event is not None:
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if x < SIZE[0] / 3:
                    self.current_picture = (self.current_picture + len(self.pictures) - 1) % len(self.pictures)
                    self.update_picture()
                elif x > (SIZE[0] / 3) * 2:
                    self.current_picture = (self.current_picture + 1) % len(self.pictures)
                    self.update_picture()
                else:
                    self.load_pictures()
                    self.update_picture()
        if pygame.time.get_ticks() >= self.next_update_time:
            self.current_picture = (self.current_picture + 1) % len(self.pictures)
            self.update_picture()
