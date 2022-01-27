import pygame.key
import sys


class MenuController:

    def __init__(self, selector, menu):
        self.selector = selector
        self.menu = menu
        self.menu_state = "start"

        self.set_selector_pos()
        self.selectorNeedsMoving = False

    def set_menu_state(self, state):
        self.menu_state = state
        self.selector.menu_type = state
        self.set_selector_pos()
        self.selectorNeedsMoving = False

    def handle(self, event):
        """
        Method to handle player input on start_menu scene
        :param event: the player input to handle
        :return: None
        """
        # Get keypress - TODO decide on keydown / up handling here in menu
        # TODO implement mouse support?
        if event.type == pygame.KEYUP:
            if self.menu_state == "highscore":
                self.menu.new_scene("options")
            else:
                if event.key == pygame.K_UP:
                    print('moving selector up')
                    self.selector.prev_item()
                    self.selectorNeedsMoving = True

                elif event.key == pygame.K_DOWN:
                    print('moving selector down')
                    self.selector.next_item()
                    self.selectorNeedsMoving = True

                elif event.key == pygame.K_RETURN:
                    selected = self.selector.get_selected()

                    if self.menu_state == "start":
                        if selected == 0:
                            scene = "tutorial"
                        elif selected == 1:
                            scene = "play"
                        elif selected == 2:
                            scene = "endless"
                        elif selected == 3:
                            scene = "options"
                        elif selected == 4:
                            pygame.quit()
                            sys.exit()
                        if selected != 4:
                            self.menu.new_scene(scene)

                    elif self.menu_state == "options":
                        if selected == 0:
                            # toggle music
                            self.menu.scene_controller.toggle_music()
                        elif selected == 1:
                            # toggle sound
                            self.menu.scene_controller.toggle_sound()
                        elif selected == 2:
                            # toggle invulnerable
                            self.menu.scene_controller.toggle_invulnerable()
                        elif selected == 3:
                            scene = "highscore"
                            self.menu.new_scene(scene)
                        elif selected == 4:
                            scene = "start_menu"
                            self.menu.new_scene(scene)

    def update(self):
        if self.selectorNeedsMoving:
            self.set_selector_pos()
            self.selectorNeedsMoving = False

    def set_selector_pos(self):
        """
        Method to set selector position next to selected menu item
        :return:
        """
        # get position of selector and set it to hardcoded menu values
        text_item = self.selector.get_selected()
        if self.menu_state == 'start':
            if text_item == 0:
                self.selector.set_pos(590, 270)
            elif text_item == 1:
                self.selector.set_pos(590, 300)
            elif text_item == 2:
                self.selector.set_pos(590, 330)
            elif text_item == 3:
                self.selector.set_pos(590, 360)
            elif text_item == 4:
                self.selector.set_pos(590, 390)
        elif self.menu_state == 'options':
            if text_item == 0:
                self.selector.set_pos(530, 270)
            elif text_item == 1:
                self.selector.set_pos(530, 300)
            elif text_item == 2:
                self.selector.set_pos(530, 330)
            elif text_item == 3:
                self.selector.set_pos(530, 360)
            elif text_item == 4:
                self.selector.set_pos(530, 390)

    def reset_menu_pos(self):
        self.selector.set_selected(0)
        self.selectorNeedsMoving = True
