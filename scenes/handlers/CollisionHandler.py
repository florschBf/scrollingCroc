import gameObjects.PlayerObject
from gameObjects.Projectile import Projectile
import pygame.sprite

class CollisionHandler:

    def __init__(self, sprite_to_check, sprites_to_check_against, scene):
        self.sprite_to_check = sprite_to_check
        self.sprites_to_check_against = sprites_to_check_against
        self.current_sprite = None
        self.my_scene = scene

    def check_for_collisions(self):
        """
        Method to check for collisions between the sprite_to_check group and the sprites_to_check_against
        :return: nth, collision result also handled here directly
        """
        for sprite in self.sprite_to_check:
            self.current_sprite = sprite
            collisions = pygame.sprite.spritecollide(sprite, self.sprites_to_check_against, False)
            for collision in collisions:
                print("collisioN!")
                # lots of collisions potentially... might consider triggering bigger chunks and granting invul for a sec
                # also consider obstacles to just be game over anyway
                self.current_sprite.set_health(self.current_sprite.return_health() - collision.collision_damage)
                if (self.current_sprite.return_health() <= 0):
                    print(type(self.current_sprite))
                    if isinstance(self.current_sprite, gameObjects.PlayerObject.PlayerObject):
                        # uhoh, game over actually
                        print(type(self.current_sprite))
                        # revive for now
                        self.current_sprite.set_health(100)
                    else:
                        print(type(self.current_sprite))
                        # was not the player - so the player actually shot sth.
                        # we grant points - call function on PlayerObjects Controller
                        if self.current_sprite.already_destroyed == False:
                            self.my_scene.my_player.score += self.current_sprite.score_value
                            self.current_sprite.already_destroyed == True
                        self.current_sprite.kill()

                # if this was a projectile in the collision, it should be removed
                if isinstance(collision, Projectile):
                    collision.kill()

