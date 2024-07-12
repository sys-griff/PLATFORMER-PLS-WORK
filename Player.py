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
        self.collide = False
        self.jump = False
    
    def handle_input(self, keys):

        next_action = "Idle"

        if keys[pygame.K_w] and self.jump == False:
            self.y_velocity = -7
            next_action = "Jump"
            self.jump = True
        
        elif keys[pygame.K_d]:
            self.x_velocity = 5
            self.direction = 1
            next_action = "Run"

        elif keys[pygame.K_a]:
            self.x_velocity = -5
            self.direction = -1
            next_action = "Run"
        else:
            self.x_velocity = 0
            next_action = "Idle"

        self.change_action(next_action)

    def change_action(self, next_action):
        if next_action != self.action:
            self.frame = 0
            self.action = next_action

    def render(self, elapsed_time):

        if elapsed_time - self.curr_time > self.animation_time:
            self.curr_time = elapsed_time
            self.frame += 1
        
        if self.frame > self.animations[self.action].rows - 1:
            self.frame = 0

        #img = pygame.Surface.subsurface(self.img, (0, 0, 2400//10, 160))
        
        img = self.animations[self.action].get_frame(self.frame)

        img = pygame.transform.scale(img, (270, 180))
        
        if self.direction < 0:
            img = pygame.transform.flip(img, True, False)

        self.game.screen.blit(img, self.pos)


    def collisions(self, tiles, screen):

        player_rect = pygame.Rect(self.pos[0] + 95, self.pos[1] + 170, 60, 10)

        self.collide = False

        for tile in tiles:
            tile_rect = pygame.Rect(tile.x, tile.y, tile.size, tile.size)

            print("tile coordinates:", tile.x, tile.y, tile.size)

            #pygame.draw.rect(screen, (0, 255, 0), tile_rect)

            if tile_rect.colliderect(player_rect):
                self.collide = True
                self.y_velocity = 0
                self.jump = False
            

    def update(self):

        if self.collide == False:
            self.y_velocity += 0.3
        self.pos[0] += self.x_velocity
        self.pos[1] += self.y_velocity