import gameObjects.PlayerObject
import gameObjects.PowerUp
from gameObjects.Projectile import Projectile
import pygame.sprite


class CollisionHandler:

    def __init__(self, sprite_to_check, sprites_to_check_against, scene, player_collider=False):
        self.sprite_to_check = sprite_to_check
        self.sprites_to_check_against = sprites_to_check_against
        self.current_sprite = None
        self.my_scene = scene
        self.player_collider = player_collider

    def check_for_collisions(self, player_collision=False):
        """
        Method to check for collisions between the sprite_to_check group and the sprites_to_check_against
        :return: nth, collision result also handled here directly
        """
        if self.player_collider:
            player_collision = True
        for sprite in self.sprite_to_check:
            self.current_sprite = sprite

            collisions = pygame.sprite.spritecollide(sprite, self.sprites_to_check_against, False)
            for collision in collisions:

                # lots of collisions potentially... might consider triggering bigger chunks and granting invul for a sec
                # also consider obstacles to just be game over anyway

                if isinstance(collision, gameObjects.PowerUp.PowerUp):
                    # powerup found
                    print("player picked up a powerup")
                    if not collision.already_destroyed:
                        collision.powerup(self.my_scene)
                        collision.already_destroyed = True
                    collision.kill()

                # check if player is invulnerable
                if player_collision:
                    if self.my_scene.scene_controller.invulnerable:
                        pass
                    else:
                        self.current_sprite.set_health(self.current_sprite.return_health() - collision.collision_damage)
                else:
                    self.current_sprite.set_health(self.current_sprite.return_health() - collision.collision_damage)

                if self.current_sprite.return_health() <= 0:
                    if player_collision and not self.current_sprite.game_over:
                        # uhoh, this is the player - lost a life or game over actually
                        # revive for now, this is invulnerable mode
                        if self.current_sprite.lives > 0:
                            self.current_sprite.set_health(100)
                            self.current_sprite.lives -= 1
                            if self.my_scene.controller.projectiles_per_shot > 1:
                                self.my_scene.controller.projectiles_per_shot -= 1
                        else:
                            # game really over
                            self.current_sprite.game_over = True
                            self.my_scene.game_over_message()
                    else:
                        # was not the player - so the player actually shot sth.
                        # we grant points - call function on PlayerObjects Controller
                        if not self.current_sprite.already_destroyed:
                            self.my_scene.my_player.score += self.current_sprite.score_value
                            self.current_sprite.already_destroyed = True
                        self.current_sprite.kill()
                        self.my_scene.scene_controller.sound_control.play_sound("exploding_enemy")
                        if len(self.my_scene.active_sprites.sprites()) == 0:
                            # that was the last active obstacle - tell the encounter controller, when this happend
                            try:
                                self.my_scene.encounters.board_clear = self.my_scene.time_handler.elapsed_time
                            except Exception:
                                # endless mode works differently, not very elegant but works
                                print('Endless mode not working with encounter file')
                                pass

                # if this was a projectile in the collision, it should be removed
                if isinstance(collision, Projectile):
                    collision.kill()
