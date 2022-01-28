from uiObjects.HealthDisplay import HealthDisplay
from uiObjects.TimeDisplay import TimeDisplay
from uiObjects.ScoreDisplay import ScoreDisplay
from uiObjects.PlayerReadMe import PlayerReadMe
from uiObjects.LifeDisplay import LifeDisplay
from uiObjects.InfoBar import InfoBar
from uiObjects.HighscoreInput import HighscoreInput


class UiHandler:

    def __init__(self, scene):
        self.info_bar = InfoBar()
        self.scene = scene
        # ui sprite group to manage
        self.ui_sprites = self.scene.ui
        self.ui_overlay = self.scene.ui_on_top
        self.highscore_input_bool = False

    def create_info_bar(self):
        self.info_bar.add(self.ui_sprites)
        self.info_bar.set_pos(0, 0)
        return self.info_bar

    def create_health_display(self, infobar):
        self.health_display = HealthDisplay(self.scene.my_player, infobar)
        self.health_display.add(self.ui_sprites)
        self.position_new_toprow_element(self.health_display)
        return self.health_display

    def create_time_display(self, initial_value, infobar):
        self.time_display = TimeDisplay(initial_value, infobar)
        self.time_display.add(self.ui_sprites)
        self.position_new_toprow_element(self.time_display)
        return self.time_display

    def create_score_display(self, infobar):
        self.score_display = ScoreDisplay(self.scene.my_player, infobar)
        self.score_display.add(self.ui_sprites)
        self.position_new_toprow_element(self.score_display)
        return self.score_display

    def create_life_display(self, infobar):
        self.life_display = LifeDisplay(self.scene.my_player, infobar)
        self.life_display.add(self.ui_sprites)
        self.position_new_toprow_element(self.life_display)
        return self.life_display

    def create_message_to_player(self, *args):
        self.message_to_player = PlayerReadMe()
        self.message_to_player.set_message(*args)
        self.message_to_player.add(self.ui_overlay)
        self.message_to_player.set_pos(self.scene.gameboard.get_width()/2 - 300, self.scene.gameboard.get_height()/2)
        self.message_to_player.update()
        self.scene.interrupted = True
        return self.message_to_player

    def create_highscore_input(self, *args):
        if self.scene.scene_controller.compare_scores(self.scene.get_score()):
            self.highscore_input = HighscoreInput()
            print('should be a highscore')
            # add input for name
            self.highscore_input.score_high_enough = True
            self.highscore_input.set_message('Wow!', 'Das reicht für die Highscore.', 'Bitte den Namen eintragen und mit Return bestätigen:')
        else:
            self.highscore_input = PlayerReadMe()
            self.highscore_input.set_message(*args)
        self.highscore_input.add(self.ui_overlay)
        self.highscore_input.set_pos(self.scene.gameboard.get_width()/2 - 300, self.scene.gameboard.get_height()/2)
        self.highscore_input.update()
        self.scene.interrupted = True
        self.highscore_input_bool = True

        return self.highscore_input

    def write_to_input(self, char):
        if len(self.highscore_input.name_string) < 26:
            self.highscore_input.name_string += char
            print(self.highscore_input.name_string)
        else:
            # string getting too long, sorry
            pass

    def delete_from_input(self):
        if len(self.highscore_input.name_string) > 11:
            self.highscore_input.name_string = self.highscore_input.name_string[:-1]
            print("deleting last char")
            print(self.highscore_input.name_string)
        else:
            print('not deleting "Dein Name: "')

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
