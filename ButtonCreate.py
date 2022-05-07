import Images
import ScreenSetup
import Button

# create buttons
restart_button = Button.Button(ScreenSetup.screen_width // 2 - 50, ScreenSetup.screen_height // 2 + 100,
                               Images.restart_img)
start_button = Button.Button(ScreenSetup.screen_width // 2 - 350, ScreenSetup.screen_height // 2, Images.start_img)
exit_button = Button.Button(ScreenSetup.screen_width // 2 + 150, ScreenSetup.screen_height // 2, Images.exit_img)
exit_button_level = Button.Button(ScreenSetup.screen_width // 2 - 50, ScreenSetup.screen_height // 2 + 300,
                               Images.exit_img)