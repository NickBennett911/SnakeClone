import pygame
from math3d import *
import globs

class Tile:
    def __init__(self, x, y, state, Player_piece=False, move_dir=None):
        self.state = state
        self.pos = vec2(x, y)
        self.player = Player_piece
        self.direction = move_dir

    def change_state(self):
        self.state = not self.state


    def draw(self, surf):
        rect = (self.pos.x, self.pos.y, globs.tile_w, globs.tile_w)
        if self.state and not self.player:
            pygame.draw.rect(surf, globs.red, rect)
        elif self.player:
            pygame.draw.rect(surf, globs.green, rect)
        if globs.grid_on:
            pygame.draw.rect(surf, globs.white, rect, 1)
