from uiObjects.HealthDisplay import HealthDisplay
from uiObjects.TimeDisplay import TimeDisplay
from uiObjects.ScoreDisplay import ScoreDisplay

class UiHandler():

    def __init__(self, scene):
        self.scene = scene
        # ui sprite group to manage
        self.ui_sprites = self.scene.ui

    def create_health_display(self):
        self.health_display = HealthDisplay(self.scene.my_player)
        self.health_display.add(self.ui_sprites)
        self.position_new_toprow_element(self.health_display)
        return self.health_display

    def create_time_display(self, initial_value):
        self.time_display = TimeDisplay(initial_value)
        self.time_display.add(self.ui_sprites)
        self.position_new_toprow_element(self.time_display)
        return self.time_display

    def create_score_display(self):
        self.score_display = ScoreDisplay(self.scene.my_player)
        self.score_display.add(self.ui_sprites)
        self.position_new_toprow_element(self.score_display)
        return self.score_display

    def position_new_toprow_element(self, element):
        """
        Method to position top row UI elements next to each other
        Counting number of elements, new one is always last, leaving 100px for each element to feel comfy
        :param element: the new UI Element
        :return:
        """
        my_position = len(self.ui_sprites.sprites())
        offset = (120 * (my_position-1)) + 20
        element.set_pos(offset, element.get_pos().x)

    def update(self):
        self.time_display.update()
        self.health_display.update()
