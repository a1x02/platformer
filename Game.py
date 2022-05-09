import pygame
import GameVars
import Images
import ScreenSetup
import ButtonCreate
import GroupSetup


def game_run():
    pygame.init()

    while GameVars.run:
        GameVars.clock.tick(GameVars.fps)

        ScreenSetup.screen.blit(Images.bg_img, (0, 0))
        ScreenSetup.screen.blit(Images.sun_img, (100, 100))

        if GameVars.main_menu == True:
            if ButtonCreate.exit_button.draw():
                GameVars.run = False
            if ButtonCreate.start_button.draw():
                GameVars.main_menu = False
        else:
            GameVars.levels[GameVars.level].draw()

            if GameVars.game_over == 0:
                GroupSetup.blob_group.update()

            GroupSetup.blob_group.draw(ScreenSetup.screen)
            GroupSetup.lava_group.draw(ScreenSetup.screen)
            GroupSetup.exit_group.draw(ScreenSetup.screen)

            GameVars.game_over = GameVars.player.update(GameVars.game_over)

            # if player has died
            if GameVars.game_over == -1:
                if ButtonCreate.restart_button.draw():
                    GameVars.player.reset(100, ScreenSetup.screen_height - 130)
                    GameVars.game_over = 0
                if ButtonCreate.exit_button_level.draw():
                    GameVars.run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GameVars.run = False

        pygame.display.update()

    pygame.quit()
