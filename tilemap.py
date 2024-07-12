import pygame
import json
from tile import Tile

class Tilemap:
    def __init__(self, map_data, tileset):
        self.map_data = map_data
        self.tileset = tileset
        self.tile_size = self.map_data['tileSize']
        self.map_width = self.map_data['mapWidth']
        self.map_height = self.map_data['mapHeight']
        self.physical_tiles = []
        self.aesthetic_tiles = []
        self.scale = 2.5
        self.x = 0
        self.y = 392

    def get_tile(self, id):
        x_check = 1

        id = int(id)

        if id == 0:
            x_check = 0
        else:
            x_check = 1
        
        y = id // 8
        x = id - (y * 8)
        return pygame.Surface.subsurface(self.tileset, (x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size))

    def load_map(self):

        for (i, layer) in enumerate (self.map_data['layers']):
            for tile in layer['tiles']:
                type = ""
                x = tile['x']
                y = tile['y']
                if i == 0:
                    type = "physical"
                    self.physical_tiles.append(Tile(self.get_tile(tile['id']), x * self.tile_size * self.scale, y * self.tile_size * self.scale, type, (self.tile_size * self.scale)))

    def render(self, screen):
        for tile in self.physical_tiles:
            img = pygame.transform.scale(tile.img, (self.tile_size * self.scale, self.tile_size * self.scale))
            screen.blit(img, (tile.x, tile.y))