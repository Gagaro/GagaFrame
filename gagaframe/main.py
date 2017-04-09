from optparse import OptionParser
import sys

import pygame

from gagaframe.shows.pictures import PictureShow
from gagaframe.utils import SIZE


def main(options, args):
    pygame.init()

    screen = pygame.display.set_mode(SIZE, options.fullscreen and pygame.FULLSCREEN or 0)
    pygame.mouse.set_visible(False)

    clock = pygame.time.Clock()

    show = PictureShow(screen)
    show.initialize(options, args)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            show.run(event)
        show.run()
        clock.tick(30)


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-f', '--fullscreen', action="store_true", dest="fullscreen", default=False)
    parser.add_option('-d', '--picture-directory', type="string", dest="picture_directory")
    (options, args) = parser.parse_args()
    main(options, args)
