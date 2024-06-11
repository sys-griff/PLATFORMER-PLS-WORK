from Gameobject import Gameobject
import pygame

class Player(Gameobject):
    def __init__(self, pos, width, height, img, game):
        super().__init__(pos, width, height, img, game)

        self.direction = 0
        self.x_velocity = 0
        self.y_velocity = 0
    
    def handle_input(self, keys):
        if keys[pygame.K_w]:
            self.y_velocity = -3
        
        elif keys[pygame.K_d]:
            self.x_velocity = 3

        elif keys[pygame.K_s]:
            self.y_velocity = 3

        elif keys[pygame.K_a]:
            self.x_velocity = -3
        else:
            self.y_velocity = 0
            self.x_velocity = 0

    
    def update(self):
        self.pos[0] += self.x_velocity
        self.pos[1] += self.y_velocity