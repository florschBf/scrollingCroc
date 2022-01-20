import pygame.key


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
        # TODO implement mouse support
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

                self.menu.scene_controller.launch(scene)

        print(event.type)

    def update(self):
        if self.selectorNeedsMoving:
            self.set_selector_pos()
            self.selectorNeedsMoving = False

        #print(self.selector.rect)

    def set_selector_pos(self):
        # get position of selected item
        print("trying to move selector...")
        text_item = self.selector.get_selected()
        if text_item == 0:
            self.selector.setPos(self.menu.menu_display.get_width() / 2 - 50, self.menu.menu_display.get_height() / 2 - 120)
        elif text_item == 1:
            self.selector.setPos(self.menu.menu_display.get_width() / 2 - 50, self.menu.menu_display.get_height() / 2 - 90)
        elif text_item == 2:
            self.selector.setPos(self.menu.menu_display.get_width() / 2 - 50, self.menu.menu_display.get_height() / 2 - 60)
        elif text_item == 3:
            self.selector.setPos(self.menu.menu_display.get_width() / 2 - 50, self.menu.menu_display.get_height() / 2 - 30)
