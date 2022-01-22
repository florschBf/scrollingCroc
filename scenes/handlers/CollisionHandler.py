import pygame.sprite

class CollisionHandler:

    def __init__(self, player_sprite, active_sprites):
        self.player_sprite = player_sprite
        self.active_sprites = active_sprites
        self.player = self.player_sprite.sprite

    def check_for_collisions(self):

        collisions = pygame.sprite.spritecollide(self.player, self.active_sprites, False)
        for collision in collisions:
            print("collisioN!")
            print(collision)
            # lots of collisions potentially... might consider triggering bigger chunks and granting invul for a sec
            # also consider obstacles to just be game over anyway
            self.player.set_health(self.player.return_health() - collision.collision_damage)
            if (self.player.return_health() <= 0):
                # uhoh, game over
                # revive for now
                self.player.set_health(100)
            print(collision.collision_damage)
            print(self.player.return_health())