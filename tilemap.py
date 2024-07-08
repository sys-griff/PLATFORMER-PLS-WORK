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
        self.tiles = []

    def load_map(self):
        print(self.map_data['layers'][0]['tiles'][0])

        for layer in self.map_data['layers']:
            for tile in layer['tiles']:
                x = tile[x]
                y = tile[y]
                Tile("temp", x, y)