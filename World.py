import pygame
import ScreenSetup
import Lava
import GroupSetup
import Enemy
import Exit

tile_size = 50


class World():
    def __init__(self, data):
        self.tile_list = []

        # load images
        dirt_img = pygame.image.load('img/dirt.png')
        grass_img = pygame.image.load('img/grass.png')

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(grass_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 3:
                    blob = Enemy.Enemy(col_count * tile_size, row_count * tile_size + 15)
                    GroupSetup.blob_group.add(blob)
                if tile == 6:
                    lava = Lava.Lava(col_count * tile_size, row_count * tile_size + (tile_size // 2))
                    GroupSetup.lava_group.add(lava)
                if tile == 8:
                    exit = Exit.Exit(col_count * tile_size, row_count * tile_size - (tile_size // 2))
                    GroupSetup.exit_group.add(exit)

                col_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            ScreenSetup.screen.blit(tile[0], tile[1])
            #pygame.draw.rect(ScreenSetup.screen, (255, 255, 255), tile[1], 2)
