import pygame.key
import sys


class MenuController:

    def __init__(self, selector, menu):
        self.selector = selector
        self.menu = menu
        self.set_selector_pos()
        self.selectorNeedsMoving = False

    # def printMyEvent(self, event):
    #     print(event)

    def handle(self, event):
        """
        Method to handle player input on start_menu scene
        :param event: the player input to handle
        :return: None
        """
        # Get keypress - TODO decide on keydown / up handling here in menu
        # TODO implement mouse support?
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                print('moving selector up')
                self.selector.prev_item()
                self.selectorNeedsMoving = True

            elif event.key == pygame.K_DOWN:
                print('moving selector down')
                self.selector.next_item()
                self.selectorNeedsMoving = True

            elif event.key == pygame.K_RETURN:
                print('pew pew')
                selected = self.selector.get_selected()

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

        print(event.type)

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

    def reset_menu_pos(self):
        self.selector.set_selected(0)
        self.selectorNeedsMoving = True
