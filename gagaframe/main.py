import os
import sys

import pygame

DIRECTORY = '/media/cloud/GagaFrame'
SIZE = WIDTH, HEIGHT = 320, 240
ALLOWED_EXTENSIONS = ['.jpg', '.jpeg']


pictures = []
for picture in os.listdir(DIRECTORY):
    if not any([picture.endswith(extension) for extension in ALLOWED_EXTENSIONS]):
        continue
    pictures.append(os.path.join(DIRECTORY, picture))


pygame.init()
screen = pygame.display.set_mode(SIZE)
#screen = pygame.display.set_mode(SIZE, pygame.FULLSCREEN)

picture = pygame.image.load(pictures[0])
picture = pygame.transform.scale(picture, SIZE)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((0, 0, 0))
    screen.blit(picture, picture.get_rect())
    pygame.display.flip()
