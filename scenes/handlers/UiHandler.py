import uiObjects.TimeDisplay
from uiObjects import *

class UiHandler():

    def __init__(self, scene):
        self.scene = scene
        # ui sprite group to manage
        self.ui_sprites = self.scene.ui

    def create_health_display(self):
        self.health_display = uiObjects.HealthDisplay.HealthDisplay(self.scene.my_player)
        self.health_display.add(self.ui_sprites)
        self.position_new_toprow_element(self.health_display)

    def create_time_display(self, initial_value):
        self.time_display = uiObjects.TimeDisplay.TimeDisplay(initial_value)
        self.time_display.add(self.ui_sprites)
        self.position_new_toprow_element(self.time_display)

    def position_new_toprow_element(self, element):
        """
        Method to position top row UI elements next to each other
        Counting number of elements, new one is always last, leaving 100px for each element to feel comfy
        :param element: the new UI Element
        :return:
        """
        my_position = len(self.ui_sprites.sprites())
        offset = 150 * my_position
        element.set_pos(offset, element.get_pos().x)

    def update(self):
        self.time_display.update()
        self.health_display.update()