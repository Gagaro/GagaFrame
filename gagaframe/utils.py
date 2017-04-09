import pygame

SIZE = WIDTH, HEIGHT = 480, 320


def scale_keep_ratio(img, size):
    """ Scales 'img' to fit into box bx/by.
     This method will retain the original image's aspect ratio """
    bx, by = size
    ix, iy = img.get_size()
    if ix > iy:
        # fit to width
        scale_factor = bx / float(ix)
        sy = scale_factor * iy
        if sy > by:
            scale_factor = by / float(iy)
            sx = scale_factor * ix
            sy = by
        else:
            sx = bx
    else:
        # fit to height
        scale_factor = by / float(iy)
        sx = scale_factor * ix
        if sx > bx:
            scale_factor = bx / float(ix)
            sx = bx
            sy = scale_factor * iy
        else:
            sy = by

    return pygame.transform.scale(img, (int(sx), int(sy)))


def get_center_topleft_coord(container, size):
    x = (container[0] - size[0]) / 2
    y = (container[1] - size[1]) / 2
    return x, y
