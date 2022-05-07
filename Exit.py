import pygame
import GameVars
import Images


class Exit(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = Images.exit_door
        self.image = pygame.transform.scale(img, (GameVars.tile_size, int(GameVars.tile_size * 1.5)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
