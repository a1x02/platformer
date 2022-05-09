import pygame
import Images
import GameVars


class Lava(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = Images.lava_img
        self.image = pygame.transform.scale(img, (GameVars.tile_size, GameVars.tile_size // 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
