import pygame
import globs
import tile_obj
import random

class Map:
    def __init__(self, W, H):
        self.mFont = pygame.font.SysFont("Times New Roman", 25)
        self.created_by = self.mFont.render("Nick Bennett", True, globs.white)
        self.name = self.mFont.render("SNAKE", True, globs.white)
        self.width = W
        self.height = H
        self.tile_h = globs.tile_h
        self.tile_w = globs.tile_w
        self.map = []
        # Create the map list of tile objects
        for x in range(int(self.width/self.tile_w)):
            for y in range(int(self.height/self.tile_h)):
                self.map.append(tile_obj.Tile(x*self.tile_w, y*self.tile_h, False))

        bounds = int(self.width/self.tile_w) * int(self.height/self.tile_h)
        self.i = random.randint(0, bounds)
        self.map[self.i].change_state()

    def makeFood(self):
        self.map[self.i].change_state()
        bounds = int(self.width / self.tile_w) * int(self.height / self.tile_h)
        self.i = random.randint(0, bounds-1)
        self.map[self.i].change_state()

    def draw(self, surf):
        # drawing all the individual tiles
        for tile in self.map:
            tile.draw(surf)

        surf.blit(self.created_by, (0, 0))
        surf.blit(self.name, (globs.win_width - self.name.get_width(), 0))