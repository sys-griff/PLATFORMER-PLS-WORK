from Gameobject import Gameobject
from Spritesheet import Spritesheet
import pygame

class Player(Gameobject):
    def __init__(self, pos, width, height, img, game, animations):
        super().__init__(pos, width, height, img, game)

        self.direction = 0
        self.x_velocity = 0
        self.y_velocity = 0
        self.animations = animations
        self.curr_time = 0
        self.animation_time = 100
        self.frame = 0
        self.action = "Idle"
    
    def handle_input(self, keys):
        if keys[pygame.K_w]:
            self.y_velocity = -5
            self.action = "Run"
        
        elif keys[pygame.K_d]:
            self.x_velocity = 5
            self.direction = 1
            self.action = "Run"

        elif keys[pygame.K_a]:
            self.x_velocity = -5
            self.direction = -1
            self.action = "Run"
        else:
            self.y_velocity = 0
            self.x_velocity = 0
            self.action = "Idle"



    def render(self, elapsed_time):

        if elapsed_time - self.curr_time > self.animation_time:
            self.curr_time = elapsed_time
            self.frame += 1
        
        if self.frame > 9:
            self.frame = 0

        #img = pygame.Surface.subsurface(self.img, (0, 0, 2400//10, 160))
        
        img = self.animations[self.action].get_frame(self.frame)

        img = pygame.transform.scale(img, (2700//10, 180))
        
        if self.direction < 0:
            img = pygame.transform.flip(img, True, False)

        self.game.screen.blit(img, self.pos)

    def update(self):
        self.pos[0] += self.x_velocity
        self.pos[1] += self.y_velocity