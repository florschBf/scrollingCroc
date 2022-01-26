from uiObjects.HealthDisplay import HealthDisplay
from uiObjects.TimeDisplay import TimeDisplay
from uiObjects.ScoreDisplay import ScoreDisplay
from uiObjects.PlayerReadMe import PlayerReadMe
from uiObjects.LifeDisplay import LifeDisplay

class UiHandler():

    def __init__(self, scene):
        self.scene = scene
        # ui sprite group to manage
        self.ui_sprites = self.scene.ui
        self.ui_overlay = self.scene.ui_on_top

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

    def create_life_display(self):
        self.life_display = LifeDisplay(self.scene.my_player)
        self.life_display.add(self.ui_sprites)
        self.position_new_toprow_element(self.life_display)

    def create_message_to_player(self, *args):
        self.message_to_player = PlayerReadMe()
        self.message_to_player.set_message(*args)
        self.message_to_player.add(self.ui_overlay)
        self.message_to_player.set_pos(self.scene.gameboard.get_width()/2 - 300, self.scene.gameboard.get_height()/1.5)
        self.message_to_player.update()
        self.scene.interrupted = True
        return self.message_to_player

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

    def remove_ui_element(self, element_to_remove):
        element_to_remove.kill()

    def hide_ui_element(self, element_to_hide):
        element_to_hide.groups().add(self.scene.hidden_sprites)
        element_to_hide.groups().remove(self.scene.ui)

    def update(self):
        self.time_display.update()
        self.health_display.update()
