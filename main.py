from globs import *
import pygame
import map
import player

pygame.init()
W = win_width
H = win_height
win = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

done = False
my_map = map.Map(W, H)
player = player.Player(tile_w*5, tile_h*5)
font = pygame.font.SysFont("Times New Roman", 25)
fps = clock.get_fps()
fps_text = font.render("FPS:" + str(int(fps)), True, white)

while not done:
    # updates
    deltaTime = clock.tick()/1000
    fps = clock.get_fps()   # able to calculate my fps with pygame's clock object
    fps_text = font.render("FPS:" + str(int(fps)), True, white) #put the fps into my on screen font to be shown on screen
    player.update(deltaTime)    # be sure to update player
    for tile in my_map.map:     # iterate through all tiles in map
        if tile.state:
            if player.body[0].pos == tile.pos:
                my_map.makeFood()
                player.grow()

    # inputs
    evt = pygame.event.poll()
    if evt.type == pygame.QUIT:
        done = True
    elif evt.type == pygame.KEYDOWN:
        if evt.key == pygame.K_ESCAPE:
            done = True
    player.input(evt)

    # draw
    win.fill((50, 50, 50))
    player.draw(win)
    my_map.draw(win)
    win.blit(fps_text, (win_width - fps_text.get_width(), win_height - fps_text.get_height()))
    pygame.display.flip()

pygame.quit()