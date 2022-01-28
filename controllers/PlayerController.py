import pygame.key

from gameObjects.Projectile import Projectile


class PlayerController:
    """
    Class that controls all input for the playerobject, e.g. movement and shooting
    """

    def __init__(self, player, scene):
        """
        Constructor for player controllers
        :param player: Player object that will be controlled with inputs
        """
        self.player = player
        self.scene = scene
        '''movement settings - switch up to change player move behaviour
        drag slows down when not accelerating, responsiveness controls quickness of controls'''
        self.responsiveness = 1
        self.drag = 0.1
        self.maxSpeed = 10
        self.accelerating = False
        self.decelerating = False
        self.rising = False
        self.falling = False
        self.projectiles_per_shot = 1
        self.shooting = False
        self.shot_timer = 0
        self.shot_delay = 20

    def handle(self, event):
        """
        Methode zum Verarbeiten von Keyboard, Maus und Controller-Input
        :param event: Player Input
        :return:
        """
        if self.scene.interrupted:
            # message to player being displayed. on input, remove and proceed with game
            self.scene.ui_handler.remove_ui_element(self.scene.ui_handler.message_to_player)
        else:
            # Get keypress
            if event.type == pygame.KEYDOWN:
                # arrows for movement
                if event.key == pygame.K_LEFT:
                    self.decelerating = True
                elif event.key == pygame.K_RIGHT:
                    print(self.accelerating)
                    self.accelerating = True
                    print(self.accelerating)
                elif event.key == pygame.K_UP:
                    self.rising = True
                elif event.key == pygame.K_DOWN:
                    self.falling = True
                elif event.key == pygame.K_SPACE:
                    # shooting
                    self.shooting = True

            # Get keyup
            elif event.type == pygame.KEYUP:
                # arrow up = stop movement
                if event.key == pygame.K_LEFT:
                    self.decelerating = False
                elif event.key == pygame.K_RIGHT:
                    self.accelerating = False
                elif event.key == pygame.K_UP:
                    self.rising = False
                elif event.key == pygame.K_DOWN:
                    self.falling = False
                elif event.key == pygame.K_SPACE:
                    self.shooting = False

                # escape for start menu / pause
                elif event.key == pygame.K_ESCAPE:
                    # THIS LEAVES THE SCENE BELOW INTACT - WIE PAUSE
                    self.scene.new_scene("start_menu")

    def stop_movement(self):
        self.accelerating = False
        self.decelerating = False
        self.rising = False
        self.falling = False

    def shoot(self):
        if self.shot_timer < 10:
            self.shot_timer = self.shot_delay

            for x in range(self.projectiles_per_shot):
                if x == 0:
                    self.bubble_shot(1, 0)
                elif x == 1:
                    self.bubble_shot(1, 1)
                elif x == 2:
                    self.bubble_shot(1, -1)
                elif x == 3:
                    self.bubble_shot(5, 3)
                elif x == 4:
                    self.bubble_shot(5, -3)
                else:
                    pass

    def bubble_shot(self, x_offset, y_offset):
        """
        Method to spawn bubble projectiles for player
        :param x_offset: shooting angles are controlled with these offsets, basically an imaginary target to calc with
        :param y_offset: shooting angles are controlled with these offsets, basically an imaginary target to calc with
        :return:
        """
        # player just shoots straight ahead usually, on upgrade starts branching out with offset
        playerpos = self.player.get_pos()
        shot = Projectile(self.scene.gameboard, 100, (playerpos.x + self.player.image.get_width(),
                                                      playerpos.y + self.player.image.get_height() / 2),
                          self.player.projectile_image)
        self.scene.scene_controller.sound_control.play_sound("bubble_shot")
        target = (playerpos.x + x_offset, playerpos.y + y_offset)
        shot.set_shot_direction(target, playerpos)
        shot.add(self.scene.projectiles_player)

    def update(self):
        """
        Movement is realized through a changing speed tuple variable
        Increased on acceleration/rise
        Decreased on decelerate/fall
        :return:
        """
        if self.player.game_over:
            self.scene.game_over()
        speed = self.player.get_speed()
        if self.shooting:
            self.shoot()
        if self.shot_timer > 0:
            self.shot_timer -= 1
        # x movement
        if self.accelerating:
            if speed[0] < self.maxSpeed:
                self.player.accelerate(self.responsiveness)
        elif self.decelerating:
            if speed[0] > -self.maxSpeed:
                self.player.decelerate(self.responsiveness)
        else:
            # no movement, apply default drag
            if speed[0] > 0:
                self.player.decelerate(self.drag)
            elif speed[0] < 0:
                self.player.accelerate(self.drag)

        # y movement
        if self.rising:
            if speed[1] < self.maxSpeed:
                self.player.rise(self.responsiveness/2)
        elif self.falling:
            if speed[1] > -self.maxSpeed:
                self.player.fall(self.responsiveness/2)
        else:
            # no movement, apply default drag
            if speed[1] < 0:
                self.player.fall(self.drag)
            elif speed[1] > 0:
                self.player.rise(self.drag)

        # Handle movement every frame
        new_pos_x = self.player.rect.x + self.player.movement[0]  # upper left corner x and y
        new_pos_y = self.player.rect.y + self.player.movement[1]

        if self.player.borderX[0] < new_pos_x < self.player.borderX[1] - self.player.image.get_width():
            self.player.rect.x = new_pos_x
        elif new_pos_x < self.player.borderX[0]:
            # hit left edge, bounce from border
            self.player.movement[0] = 4
        elif new_pos_x > self.player.borderX[1]-self.player.image.get_width():
            # hit right edge, bounce from border
            self.player.movement[0] = -4

        if self.player.borderY[0]-self.player.image.get_height()/2 < new_pos_y < self.player.borderY[1]-self.player.image.get_height()/2:
            self.player.rect.y = new_pos_y
        elif new_pos_y < self.player.borderY[0]:
            # hit top edge, bounce from border
            self.player.movement[1] = 4
        elif new_pos_y > self.player.borderY[1]-self.player.image.get_height():
            # hit bottom edge, bounce from border
            self.player.movement[1] = -4
