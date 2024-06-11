import pygame
import sys

from Gameobject import Gameobject
from Player import Player
from Spritesheet import Spritesheet

class Game:
    def __init__(self):
        
        playerimg = pygame.image.load("_Idle.png")

        print(playerimg.get_height())
        
        self.background = pygame.image.load("Clouds.png")
        self.background = pygame.transform.scale(self.background, (960, 540))

        self.idle = Spritesheet(playerimg, 10)

        self.player = Player((0, 380), 2400, 160, "_Idle.png", self, self.idle)

        self.clock = pygame.time.Clock()

        self.clock.tick(120)

        pygame.init()

        self.screen_width = 960
        self.screen_height = 540
        self.screen_color = (135, 206, 235)

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Pygame Screen")
        self.idle = Spritesheet(playerimg, 10)

    def run(self):
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            keys = pygame.key.get_pressed()

            self.player.handle_input(keys)

            self.player.update()

            self.screen.blit(self.background, (0, 0))

            self.player.render()

            pygame.display.flip()

        # Quit Pygame
        pygame.quit()
        sys.exit()

game = Game()

game.run()