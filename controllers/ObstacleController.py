import random


class ObstacleController:
    """
    Class that realizes movement patterns for all kinds of non-player game objects
    patterns are straight, zigzag, random and hunter
    straight: goes in a line without changing y
    zigzag: goes diagonally and reverts on screen border
    random: sets random directions and speeds on an interval
    hunter: moves relative to the player, doesnt leave the screen on its own
    """

    def __init__(self, obstacle, move_pattern):
        self.obstacle = obstacle
        self.move_pattern = move_pattern
        if move_pattern == "random":
            # want random, making it random
            self.randomize_speed()
            self.random_counter = 0
        elif move_pattern == "zigzag":
            # want zigzag, need y movement
            self.obstacle.speed[1] = self.obstacle.speed[0]

    def moving(self):
        # handling different move patterns
        self.update_pos()
        if self.move_pattern == "random":
            self.random_counter += 1
            if self.random_counter > 30:
                self.randomize_speed()
                self.random_counter = 0

    def update_pos(self):
        # updating position according to speed
        pos = self.obstacle.get_pos()
        current_x = pos[0]
        current_y = pos[1]
        new_pos_x = current_x - self.obstacle.speed[0]
        new_pos_y = current_y - self.obstacle.speed[1]
        if self.move_pattern != 'hunter':
            if self.obstacle.border_x:
                if new_pos_x > 0:
                    pos[0] = new_pos_x
                else:
                    self.obstacle.speed[0] *= -1
            else:
                pos[0] = new_pos_x
            if self.obstacle.border_y:
                if 0 < new_pos_y < self.obstacle.surface.get_height():
                    pos[1] = new_pos_y
                else:
                    self.obstacle.speed[1] *= -1
            else:
                pos[1] = new_pos_y
        else:
            pos[0] = new_pos_x
            pos[1] = new_pos_y

    def randomize_speed(self):
        # make it random
        # need to check our direction +/-
        if self.obstacle.speed[0] < 0:
            self.obstacle.speed[0] = -random.randint(0, 10)
        else:
            self.obstacle.speed[0] = random.randint(0, 10)
        if self.obstacle.speed[1] < 0:
            self.obstacle.speed[1] = random.randint(0, 10)*-1
        else:
            self.obstacle.speed[1] = random.randint(0, 10)
