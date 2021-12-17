import pygame
from math3d import *
import globs
import tile_obj

class Player:
    right = 1
    up = 2
    left = -1
    down = -2
    def __init__(self, x, y):
        self.pos = vec2(x, y)
        dir = Player.right
        self.body = [tile_obj.Tile(self.pos.x, self.pos.y, False, True, dir),
                     tile_obj.Tile(self.pos.x-globs.tile_w, self.pos.y, False, True, dir),
                     tile_obj.Tile(self.pos.x-(globs.tile_w*2), self.pos.y, False, True, dir)]
        self.elapsed = 0
        self.directions = []
        self.font = pygame.font.SysFont("Times New Roman", 25)
        self.text = self.font.render("Score: " + str(len(self.body)-3), True, globs.white)

    def update(self, dt):
        self.elapsed += dt
        if self.elapsed > globs.move_delay:
            if len(self.directions) > 0:
                for dir in self.directions:
                    dir[2] = self.update_tiles(dir[0], dir[1], dir[2])
                for dir in self.directions:
                    if len(self.body) == dir[2]:
                       self.directions.remove(dir)

            # moving tiles based on their own directions
            for tile in self.body:
                if tile.direction == Player.right:
                    tile.pos.x += globs.tile_w
                elif tile.direction == Player.left:
                    tile.pos.x -= globs.tile_w
                elif tile.direction == Player.down:
                    tile.pos.y += globs.tile_w
                elif tile.direction == Player.up:
                    tile.pos.y -= globs.tile_w

                if tile.pos.x >= globs.win_width:
                    tile.pos.x = 0
                elif tile.pos.x < 0:
                    tile.pos.x = globs.win_width - globs.tile_w
                if tile.pos.y >= globs.win_height:
                    tile.pos.y = 0
                elif tile.pos.y < 0:
                    tile.pos.y = globs.win_height - globs.tile_h

                # checking if running into self
                for other_tile in self.body:
                    if tile != other_tile:
                        if tile.pos == other_tile.pos:
                            self.die()

            self.font = pygame.font.SysFont("Times New Roman", 25)
            self.text = self.font.render("Score: " + str(len(self.body) - 3), True, globs.white)
            self.elapsed = 0

        self.pos = self.body[0].pos

    def update_tiles(self, position, dir, tiles_affected):

        # updating the individual body tiles directions
        body_len = len(self.body)
        j = tiles_affected
        i = tiles_affected
        while i < body_len:
            if self.body[i].pos == position:
                self.body[i].direction = dir
                j += 1
            i += 1
        return j

    def grow(self):
        body_len = len(self.body)
        tail_tile = self.body[body_len-1]
        tail_dir = tail_tile.direction
        if tail_dir == Player.right:
            x = tail_tile.pos.x - globs.tile_w
            y = tail_tile.pos.y
            self.body.append(tile_obj.Tile(x, y, False, True, tail_dir))
        if tail_dir == Player.left:
            x = tail_tile.pos.x + globs.tile_w
            y = tail_tile.pos.y
            self.body.append(tile_obj.Tile(x, y, False, True, tail_dir))
        if tail_dir == Player.up:
            x = tail_tile.pos.x
            y = tail_tile.pos.y + globs.tile_h
            self.body.append(tile_obj.Tile(x, y, False, True, tail_dir))
        if tail_dir == Player.down:
            x = tail_tile.pos.x
            y = tail_tile.pos.y - globs.tile_h
            self.body.append(tile_obj.Tile(x, y, False, True, tail_dir))

    def input(self, evt):
        if evt.type == pygame.KEYDOWN:
            if evt.key == pygame.K_a or evt.key == pygame.K_LEFT:
                if self.body[0].direction != Player.right:
                    dir = Player.left
                    self.directions.append([self.pos.copy(), dir, 0])
            if evt.key == pygame.K_d or evt.key == pygame.K_RIGHT:
                if self.body[0].direction != Player.left:
                    dir = Player.right
                    self.directions.append([self.pos.copy(), dir, 0])
            if evt.key == pygame.K_w or evt.key == pygame.K_UP:
                if self.body[0].direction != Player.down:
                    dir = Player.up
                    self.directions.append([self.pos.copy(), dir, 0])
            if evt.key == pygame.K_s or evt.key == pygame.K_DOWN:
                if self.body[0].direction != Player.up:
                    dir = Player.down
                    self.directions.append([self.pos.copy(), dir, 0])

    def draw(self, surf):
        for tile in self.body:
            tile.draw(surf)
        surf.blit(self.text, (int(globs.win_width/2) - int(self.text.get_width()/2), globs.tile_h))

    def die(self):
        body_len = len(self.body)-1
        while body_len > 2:
            self.body.remove(self.body[body_len])
            body_len -= 1

