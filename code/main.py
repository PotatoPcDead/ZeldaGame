import pygame, sys
from settings import *
from level import Level
from debug import debug

run = True
class Game:
    def __init__(self):

          
        # general setup
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIDTH,HEIGTH), pygame.FULLSCREEN)
        pygame.display.set_caption('Pixi Souls')
        pygame_icon = pygame.image.load('graphics/player/down/down_0.png')
        pygame.display.set_icon(pygame_icon)
        self.level = Level()
    
    def run(self):
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill('black')
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()