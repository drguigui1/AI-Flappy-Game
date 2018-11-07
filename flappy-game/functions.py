"""
Copyright :
 - Cesar Belley
 - Pierre Guillaume
"""

import pygame
from math import exp

def floor(nb):
    if nb > 255:
        return 255
    elif nb < 0:
        return 0
    else:
        return nb

def change_color(path, r, g, b):
    """
    Multiply each pixel (r,g,b) by these three values
    """

    img = pygame.image.load(path).convert_alpha()
    pixels = pygame.PixelArray(img)

    for i in range(len(pixels)):
        for j in range(len(pixels[i])):
            (r_, g_, b_, a_)= img.unmap_rgb(pixels[i][j])
            pixels[i][j] = (floor(r_ * r),floor(g_ * g) , floor(b_ * b), a_)


    img = pixels.make_surface()
    return img

#math
def sigmoid(x):
	return 1 / (1 + exp(-x))
