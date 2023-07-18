import pygame 
from settings import *
from tile import Tile
from player import Player
from debug import debug
from support import *
from random import choice

class Level:
    def __init__(self):

        # get the display surface
        self.display_surface = pygame.display.get_surface()

        # Sprite Group Setup
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()
        
        # sprite setup
        self.create_map()

    def create_map(self):
        layout = {
            "boundary": import_csv_layout('map/map_FLoorBlocks.csv'),
            "grass": import_csv_layout("map/map_Grass.csv"),
            "object": import_csv_layout("map/map_Details.csv"),
        }
        graphics = {
            "grass": import_folder("graphics/Grass"),
            "objects": import_folder("graphics/objects")
        }
        
        for style, layout in layout.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != "-1":
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                        if style == "boundary":
                            Tile((x, y), [ self.obstacle_sprites],"invisible")
                        if style == "grass":
                            # create a grass tile
                            random_grass_image = choice(graphics["grass"])
                            Tile((x, y), [self.visible_sprites, self.obstacle_sprites], "grass", random_grass_image)
                        
                        if style == "object":
                            # create an object tile
                            surf = choice(graphics["objects"])
                            Tile((x,y), [self.visible_sprites, self.obstacle_sprites], "object", surf)
        self.player = Player((2000, 1430),[self.visible_sprites], self.obstacle_sprites)                 

    def run(self):

        #Update and draw the game       
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):

        # general setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()
        self.half_width = self.display_surface.get_size()[0]// 2
        self.half_height = self.display_surface.get_size()[1]// 2

        # creating th floor
        self.floor_surf = pygame.image.load("graphics/tilemap/ground.png").convert()
        self.floor_rect = self.floor_surf.get_rect(topleft = (0, 0))
    
    def custom_draw(self, player):

        # getting the offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        # drawing th floor
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf, floor_offset_pos)

        #for sprite in self.sprites():
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset 
            self.display_surface.blit(sprite.image, offset_pos)