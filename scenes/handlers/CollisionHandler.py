import gameObjects.PlayerObject
import pygame.sprite

class CollisionHandler:

    def __init__(self, sprite_to_check, sprites_to_check_against):
        self.sprite_to_check = sprite_to_check
        self.sprites_to_check_against = sprites_to_check_against
        self.current_sprite = None

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
                print(collision)
                print(collision.collision_damage)
                print(self.current_sprite.return_health())
                # lots of collisions potentially... might consider triggering bigger chunks and granting invul for a sec
                # also consider obstacles to just be game over anyway
                self.current_sprite.set_health(self.current_sprite.return_health() - collision.collision_damage)
                if (self.current_sprite.return_health() <= 0):
                    print(type(self.current_sprite))
                    if (isinstance(self.current_sprite, gameObjects.PlayerObject.PlayerObject)):
                        # uhoh, game over actually
                        print(type(self.current_sprite))
                        # revive for now
                        self.current_sprite.set_health(100)
                    else:
                        print(type(self.current_sprite))
                        self.current_sprite.kill()
