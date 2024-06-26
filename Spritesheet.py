import pygame

class Spritesheet:
    def __init__(self, image, rows):
        self.image = pygame.image.load(image)
        self.rows = rows
        self.tile_width = (self.image.get_width())/rows

    
    def get_frame(self, frame):
        return pygame.Surface.subsurface(self.image, (self.tile_width * frame, 0, self.tile_width, self.image.get_height()))