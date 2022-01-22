class ObstacleController:

    def __init__(self, obstacle, move_pattern):
        self.obstacle = obstacle
        self.move_pattern = move_pattern

    def moving(self):
        if self.move_pattern == "straight":
            print("straight movement")
        elif self.move_pattern == "zigzag":
            # we want zig zag, so need to add y-motion to the object
            self.obstacle.speed[1] = self.obstacle.speed[0]
            new_pos_x = self.obstacle.__getattribute__("center")[0] - self.obstacle.speed[0]
            new_pos_y = self.obstacle.__getattribute__("center")[1] - self.obstacle.speed[1]
            new_pos = [new_pos_x, new_pos_y]
            self.obstacle.__setattr__("center", new_pos)
            if self.obstacle.permanent == True:
                if new_pos[0] < 0 or new_pos[0] > self.gameboard.get_width():
                    self.obstacle.speed[0] = -self.obstacle.speed[0]
                if new_pos[1] < 0 or new_pos[1] > self.gameboard.get_height():
                    self.obstacle.speed[1] = -self.obstacle.speed[1]
        elif self.move_pattern == "random":
            print("random movement")
