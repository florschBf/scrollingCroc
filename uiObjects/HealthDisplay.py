import pygame
import pygame.font
import pygame.sprite
from uiObjects.UiObject import UiObject


class HealthDisplay(UiObject):

    def __init__(self, my_player, infobar):

        pygame.font.init()
        self.menu_font = pygame.font.get_default_font()  # getting default font for now just to render sth
        self.font_renderer = pygame.font.SysFont(self.menu_font, 30)

        self.my_player = my_player
        self.infobar = infobar

        # colors for health bar
        self.feeling_good_color = (0,204,34)
        self.hurt_color = (255,170,0)
        self.hurt_badly_color = (230,38,0)

        # player health value
        self.player_health = self.my_player.return_health()

        #bar instead of text to give some more visual indication
        self.healthbar = pygame.Surface([self.player_health,30])
        self.healthbar.fill(self.feeling_good_color)
        # empty image cause we're just blitting crocs on infobar. kind of makes this a controller? too late to change
        self.image = pygame.Surface ([0, 0])

        self.infobar.image.blit(self.healthbar, (18, 60, 100, 30))

        super().__init__()

    def update(self):
        self.player_health = self.my_player.return_health()
        # not updating text anymore, used to be done here to display number
        # self.text = self.font_renderer.render("Energie: " + str(self.player_health), True, self.feeling_good_color)
        if not self.my_player.game_over:
            self.healthbar = pygame.Surface([int(self.player_health), 30])
            if self.player_health > 80:
                self.healthbar.fill(self.feeling_good_color)
            elif self.player_health < 80 and self.player_health > 40:
                self.healthbar.fill(self.hurt_color)
            elif self.player_health < 40:
                self.healthbar.fill(self.hurt_badly_color)

        #erase healthbar and redraw the update
        self.infobar.image.blit(self.healthbar, (18, 60, 100, 30))

