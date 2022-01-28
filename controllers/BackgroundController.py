import pygame.image
import pygame.surface


class BackgroundController:
    def __init__(self, main_surface):
        self.screen = main_surface
        # load images here
        self.space_bg = pygame.image.load('assets/drawables/background/space/parallax-space-background_scaled.png').convert()
        self.space_stars = pygame.image.load('assets/drawables/background/space/parallax-space-stars_scaled.png').convert_alpha()
        self.space_ring_planet = pygame.image.load('assets/drawables/background/space/parallax-space-ring-planet_scaled.png').convert_alpha()
        self.space_far_planets = pygame.image.load('assets/drawables/background/space/parallax-space-far-planets_scaled.png').convert_alpha()
        self.space_big_planet = pygame.image.load('assets/drawables/background/space/parallax-space-big-planet_scaled.png').convert_alpha()
        # set movement variables for parallax
        self.space_big_planet_location = [720, 360]
        self.space_ring_planet_location = [380, 180]
        self.space_far_planets_location = [426, 100]
        self.space_stars_location = [0, 0]

        self.front_speed = .75
        self.middle_speed = .35
        self.back_speed = .15
        self.far_speed = .01

    def start_parallax(self, location):
        screen_w = self.screen.get_width()
        screen_h = self.screen.get_height()
        if location == 'space':
            self.screen.blit(self.space_bg, (0, 0, screen_w, screen_h))
            self.screen.blit(self.space_stars, (self.space_stars_location[0], 0, screen_w, screen_h))
            self.screen.blit(self.space_far_planets, (self.space_far_planets_location[0], 100, screen_w, screen_h))
            self.screen.blit(self.space_ring_planet, (self.space_ring_planet_location[0], 180, screen_w, screen_h))
            self.screen.blit(self.space_big_planet, (self.space_big_planet_location[0], self.space_big_planet_location[1], screen_w, screen_h))

            self.update_image_pos(self.space_big_planet, self.space_big_planet_location, "front")
            self.update_image_pos(self.space_ring_planet, self.space_ring_planet_location, "middle")
            self.update_image_pos(self.space_far_planets, self.space_far_planets_location, "back")
            self.update_image_pos(self.space_stars, self.space_stars_location, "far")

    def update_image_pos(self, image, image_pos, front_middle_back):
        if front_middle_back == 'front':
            if image_pos[0] < 0 - image.get_width():
                image_pos[0] = self.screen.get_width() + image.get_width() * 2
            image_pos[0] -= self.front_speed
        elif front_middle_back == 'middle':
            if image_pos[0] < 0 - image.get_width():
                image_pos[0] = self.screen.get_width() + image.get_width()
            image_pos[0] -= self.middle_speed
        elif front_middle_back == 'back':
            if image_pos[0] < 0 - image.get_width():
                image_pos[0] = self.screen.get_width() + image.get_width()
            image_pos[0] -= self.back_speed
        elif front_middle_back == 'far':
            if image_pos[0] < 0 - image.get_width():
                image_pos[0] = self.screen.get_width() + image.get_width()
            image_pos[0] -= self.far_speed
