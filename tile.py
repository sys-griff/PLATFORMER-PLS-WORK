import pygame

class Tile:
    def __init__(self, img, x, y, type, size):
        self.img = img
        self.x = x
        self.y = y
        self.type = type
        self.size = size
