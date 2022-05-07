import pygame

import ScreenSetup
import GameVars


def draw_grid():
    for line in range(0, 20):
        pygame.draw.line(ScreenSetup.screen, (255, 255, 255),
                         (0, line * GameVars.tile_size),
                         (ScreenSetup.screen_width, line * GameVars.tile_size))
        pygame.draw.line(ScreenSetup.screen, (255, 255, 255),
                         (line * GameVars.tile_size, 0),
                         (line * GameVars.tile_size, ScreenSetup.screen_height))
