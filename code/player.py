import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites):

        super().__init__(groups)
        # defining image
        self.image = pygame.image.load(
            "graphics/test/player.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(-30, -26)

        # Creating vector
        self.direction = pygame.math.Vector2()
        self.speed = 15
        self.obstacle_sprites = obstacle_sprites

    # input function
    def input(self):
        keys = pygame.key.get_pressed()
            # y movement
        if keys[pygame.K_UP]: # Up to move up
                self.direction.y = -1
        elif keys[pygame.K_DOWN]: # Down to move down
                self.direction.y = 1
        else:
            self.direction.y = 0
            # x movement
        if keys[pygame.K_LEFT]: # Left to move left
            self.direction.x = -1
        elif keys[pygame.K_RIGHT]: # Right to move right
            self.direction.x = 1
        else:
            self.direction.x = 0 # none 
        if keys[pygame.K_ESCAPE]:
            run = False
            pygame.quit()

    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        self.hitbox.x += self.direction.x * speed
        self.collision("horizontal")
        self.hitbox.y += self.direction.y * speed
        self.collision("vertical")
        self.rect.center = self.hitbox.center

    def collision(self, direction):

        if direction == "horizontal":
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0: # moving right
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0: # moving left
                        self.hitbox.left = sprite.hitbox.right          
        if direction == "vertical":
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0: # moving down
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0: # moving up
                        self.hitbox.top = sprite.hitbox.bottom

    def update(self):
        self.input()
        self.move(self.speed)