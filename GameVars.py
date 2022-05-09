import pygame
import Player
import ScreenSetup
import World
import WorldData

# define game variables


tile_size = 50
game_over = 0
main_menu = True
level = 0
max_level = 7
run = True

clock = pygame.time.Clock()
fps = 60

player = Player.Player(100, ScreenSetup.screen_height - 130)
world1 = World.World(WorldData.level_1)
world2 = World.World(WorldData.level_2)
world3 = World.World(WorldData.level_3)
world4 = World.World(WorldData.level_4)
world5 = World.World(WorldData.level_5)
world6 = World.World(WorldData.level_6)
world7 = World.World(WorldData.level_7)

levels = [world1, world2, world3, world4, world5, world6, world7]
