from Gameobject import Gameobject
from Spritesheet import Spritesheet
import pygame

class Player(Gameobject):
    def __init__(self, pos, width, height, img, game, spritesheet):
        super().__init__(pos, width, height, img, game)

        self.direction = 0
        self.x_velocity = 0
        self.y_velocity = 0
        self.spritesheet = Spritesheet
    
    def handle_input(self, keys):
        if keys[pygame.K_w]:
            self.y_velocity = -3
        
        elif keys[pygame.K_d]:
            self.x_velocity = 3
            self.direction = 1

        elif keys[pygame.K_s]:
            self.y_velocity = 3

        elif keys[pygame.K_a]:
            self.x_velocity = -3
            self.direction = -1
        else:
            self.y_velocity = 0
            self.x_velocity = 0



    def render(self):
        img = pygame.Surface.subsurface(self.img, (0, 0, 2400//10, 160))
        
        img = self.spritesheet.get_frame(6)
        
        if self.direction < 0:
            img = pygame.transform.flip(img, True, False)

        self.game.screen.blit(img, self.pos)

    def update(self):
        self.pos[0] += self.x_velocity
        self.pos[1] += self.y_velocity