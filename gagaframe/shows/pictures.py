import os

import pygame

from gagaframe.shows.base import BaseShow
from gagaframe.utils import scale_keep_ratio, SIZE, get_center_topleft_coord

DIRECTORY = '/media/cloud/GagaFrame'
ALLOWED_EXTENSIONS = ['.jpg', '.jpeg']
TIME_BETWEEN_PICTURES = 1000 * 5 * 60


class PictureShow(BaseShow):
    def load_pictures(self):
        self.pictures = []
        self.current_picture = 0
        for picture in os.listdir(DIRECTORY):
            if not any([picture.endswith(extension) for extension in ALLOWED_EXTENSIONS]):
                continue
            self.pictures.append(os.path.join(DIRECTORY, picture))

    def initialize(self):
        self.next_update_time = 0
        self.load_pictures()

    def reset(self):
        self.load_pictures()

    def get_next_picture(self):
        picture = pygame.image.load(self.pictures[self.current_picture]).convert()
        picture = scale_keep_ratio(picture, SIZE)
        self.current_picture = (self.current_picture + 1) % len(self.pictures)
        return picture

    def run(self, event=None):
        current_time = pygame.time.get_ticks()
        if current_time >= self.next_update_time:
            picture = self.get_next_picture()
            self.screen.fill((0, 0, 0))
            self.screen.blit(picture, get_center_topleft_coord(SIZE, picture.get_size()))
            pygame.display.flip()
            self.next_update_time = current_time + TIME_BETWEEN_PICTURES
