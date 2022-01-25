import pygame
import pygame.font
import pygame.sprite
from uiObjects.UiObject import UiObject


class HealthDisplay(UiObject):

    def __init__(self, my_player):

        pygame.font.init()
        self.menu_font = pygame.font.get_default_font()  # getting default font for now just to render sth
        self.font_renderer = pygame.font.SysFont(self.menu_font, 30)

        self.my_player = my_player

        # colors for health bar
        self.feeling_good_color = (0,204,34)
        self.hurt_color = (255,170,0)
        self.hurt_badly_color = (230,38,0)

        # player health value
        self.player_health = self.my_player.return_health()

        #text item
        self.text = self.font_renderer.render(str(self.player_health), True, self.feeling_good_color)
        #bar below it to give some indication
        self.healthbar = pygame.Surface([self.player_health,15])
        self.healthbar.fill(self.feeling_good_color)

        self.image = pygame.Surface ([100, 60])
        self.image.blit(self.text, (50, 25, 100, 30))
        self.image.blit(self.healthbar, (50, 40, 100, 30))

        super().__init__()

    def update(self):
        self.player_health = self.my_player.return_health()
        self.text = self.font_renderer.render(str(self.player_health), True, self.feeling_good_color)
        self.healthbar = pygame.Surface([int(self.player_health), 15])
        if self.player_health > 80:
            self.healthbar.fill(self.feeling_good_color)
        elif self.player_health < 80 and self.player_health > 40:
            self.healthbar.fill(self.hurt_color)
        elif self.player_health < 40:
            self.healthbar.fill(self.hurt_badly_color)

        self.image.blit(self.text, (50, 25, 100, 30))
        self.image.blit(self.healthbar, (50, 40, 100, 30))
