import sys

import pygame

from gagaframe.shows.life import LifeShow
from gagaframe.shows.pictures import PictureShow
from gagaframe.utils import SIZE

pygame.init()

screen = pygame.display.set_mode(SIZE)
#screen = pygame.display.set_mode(SIZE, pygame.FULLSCREEN)

clock = pygame.time.Clock()

#show = PictureShow(screen)
show = LifeShow(screen)
show.initialize()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        show.run(event)
    show.run()
    clock.tick(30)
