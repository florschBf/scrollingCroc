from controllers.ObstacleController import ObstacleController


class BossController(ObstacleController):

    def __init__(self, boss, move_pattern, target_player, scene):
        super().__init__(boss, 'boss')
        self.boss = boss
        self.player = target_player
        self.scene = scene

        self.base_move_freq = 180
        self.special_move_freq = 250
        self.spawn_freq = 400
        self.ultimate_freq = 1000
        self.relief_freq = 570

    def attack(self):
        """
        Method that monitors our timers and triggers attack methods on the boss where needed
        :return:
        """
        if self.boss.base_move_timer >= self.base_move_freq:
            self.boss.base_move()
            self.boss.base_move_timer = 0
        if self.boss.special_move_timer >= self.special_move_freq:
            self.boss.special_move()
            self.boss.special_move_timer = 0
        if self.boss.spawn_timer >= self.spawn_freq:
            self.boss.spawn_obstacles()
            self.boss.spawn_timer = 0
        if self.boss.ultimate_timer >= self.ultimate_freq:
            self.boss.ultimate()
            self.boss.ultimate_timer = 0
        if self.boss.relief_timer >= self.relief_freq:
            self.boss.relief()
            self.boss.relief_timer = 0

    def moving(self):
        # handling different move patterns
        self.update_pos()
        print(self.boss.return_health())

    def update_pos(self):
        # overwriting Obstacle movement, not calling super()
        if self.boss.get_pos().x > 1130:
            print("boss moving inwards")
            # slowly move image inside frame
            self.boss.set_pos(self.boss.get_pos().x - 2, self.boss.get_pos().y)
        else:
            # we're on our x position, lets move up and down
            # updating position according to speed
            pos = self.boss.get_pos()
            current_x = pos[0]
            current_y = pos[1]
            new_pos_x = current_x + self.boss.speed[0]
            new_pos_y = current_y + self.boss.speed[1]

            if self.boss.border_x:
                # border x never an issue with boss pattern/class
                if new_pos_x > 0:
                    pos[0] = new_pos_x
                else:
                    self.boss.speed[0] *= -1
            else:
                pos[0] = new_pos_x
            if self.boss.border_y:
                # constantly triggering reversal on y border though
                if 0 < new_pos_y < self.boss.surface.get_height() - self.boss.image.get_height():
                    pos[1] = new_pos_y
                else:
                    self.boss.speed[1] *= -1
            else:
                pos[1] = new_pos_y
