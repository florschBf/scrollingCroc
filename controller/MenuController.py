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
        #Get keypress
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                print('moving selector up')
                self.selector.next_item()
                self.selectorNeedsMoving = True

            elif event.key == pygame.K_DOWN:
                print('moving selector down')
                self.selector.prev_item()
                self.selectorNeedsMoving = True

            elif event.key == pygame.K_RETURN:
                print('pew pew')

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
        selected_item = self.menu.text_items[text_item]
        print(selected_item.get_rect().x, selected_item.get_rect().y)

        self.selector.rect.x = selected_item.get_rect().x - 50
        self.selector.rect.y = selected_item.get_rect().y
