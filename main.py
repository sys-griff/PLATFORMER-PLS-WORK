import pygame
import sys
import json

from Gameobject import Gameobject
from Player import Player
from Spritesheet import Spritesheet
from tilemap import Tilemap

class Game:
    def __init__(self):
        
        playerimg = pygame.image.load("_Idle.png")

        print(playerimg.get_height())
        
        self.background = pygame.image.load("Clouds.png")
        self.background = pygame.transform.scale(self.background, (960, 540))


        self.player = Player((0, 380), 2400, 55555, "_Idle.png", self, self.load_animations())

        map_data = ""

        with open("map.json", 'r') as f:
            map_data = json.load(f)

        self.tilemap = Tilemap(map_data, pygame.image.load("spritesheet.png"))



        self.tilemap.load_map()

        self.clock = pygame.time.Clock()

        pygame.init()

        self.screen_width = 960
        self.screen_height = 540
        self.screen_color = (135, 206, 235)

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Pygame Screen")

    def load_animations(self):
        return {"Idle": Spritesheet("_Idle.png", 10),
                  "Run": Spritesheet("_Run.png", 10)}

    def run(self):
        while True:
            
            elapsed_time = pygame.time.get_ticks()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            self.clock.tick(60)

            fps = self.clock.get_fps()

            keys = pygame.key.get_pressed()

            self.player.handle_input(keys)

            self.player.update()

            self.screen.blit(self.background, (0, 0))

            self.player.render(elapsed_time)

            pygame.display.flip()

        # Quit Pygame
        pygame.quit()
        sys.exit()

game = Game()

game.run()