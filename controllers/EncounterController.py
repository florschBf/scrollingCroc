import json
from gameObjects.Obstacle import Obstacle
from gameObjects.Enemy import Enemy

class EncounterController:

    def __init__(self, level, scene):
        self.scene = scene
        self.endless = False
        self.game_over = False

        if level == 'tutorial':
            f = open('assets/encounters/tut.json')
            self.encounters = json.load(f)['encounters']
        elif level == 'play':
            f = open('assets/encounters/tut.json')
            self.encounters = json.load(f)['encounters']
        else:
            self.endless = True
            self.encounters = None

        print("The encounter infos I got for my level:")
        print(self.encounters)

        # keep track of the encounters we ran
        self.current_encounter = 0
        self.last_timestamp = None # e.g. the last moment in time we ran an encounter
        self.board_clear = 0 # last time we removed all objects from the gameboard

        # encounter delay
        self.empty_delay = 1.5
        self.delay = 4.5

    def run_encounter(self, encounter_num):
        """
        Method to generate encounters from the JSON-file that structures the level
        Called depending on last time an encounter was triggered and the state of the active enemies
        :param encounter_num: the number of the encounter to be called, increases as we progress through the level(json)
        :return:
        """
        print("encounter being run")
        if self.game_over:
            self.scene.onreset()
            self.scene.scene_controller.scene_switch('start_menu', self.scene)
        elif encounter_num < len(self.encounters):
            encounter = self.encounters[str(encounter_num)]
            # check if message or encounter
            if encounter[0] == 'message':
                # yada yada
                print("creating next message")
                strings = list()
                for line in encounter:
                    if line != 'message':
                        line.encode()
                        strings.append(line)
                print(strings)
                self.scene.ui_handler.create_message_to_player(*strings)
            else:
                # it's an encounter -> spawn objects
                print("spawning next encounter")
                for obstacle in encounter:
                    if obstacle != "encounter":
                        amount = obstacle[0]
                        type = obstacle[1]
                        pattern = obstacle[2]
                        y_start = obstacle[3]
                        for x in range(amount):
                            self.generate_obstacle(type, pattern, y_start)
        else:
            # level over
            print ("Remaining Active GameObjects:" + str(self.scene.active_sprites.sprites()))
            if len(self.scene.active_sprites.sprites()) == 0:
                # you win, no more encounters left
                print("level finished, leaving....")
                self.game_over = True
                self.scene.ui_handler.create_message_to_player('Gewonnen!!!')

    def generate_obstacle(self, type, pattern, y_start = 'random'):
        """
        Method to spawn obstacles to the scene
        :param type: Currently available obstacles as String are 'obstacle' and 'enemy'
        :param pattern: Movement pattern as String, see Obstacle class
        :param y_start: y starting position, defaults to 'random', needs an int that's still on screen otherwise
        :return:
        """
        if type == "obstacle":
            new_obstacle = Obstacle(self.scene.gameboard, pattern)
            new_obstacle.add(self.scene.active_sprites)
            if y_start != 'random':
                new_obstacle.start_y = y_start
        elif type == "enemy":
            new_enemy = Enemy(self.scene.gameboard, pattern, self.scene.my_player, self.scene)
            new_enemy.set_color(self.scene.green)
            new_enemy.add(self.scene.active_sprites)
            if y_start != 'random':
                new_enemy.start_y = y_start




    def update(self):
        current_time = self.scene.time_handler.elapsed_time
        sprite_count = len(self.scene.active_sprites.sprites())
        if sprite_count == 0:
            self.board_clear = current_time
        if not self.endless:
            if self.current_encounter == 0:
                # we didnt start yet - get time, so we dont start immediately but give the player a few seconds
                if current_time >= self.empty_delay:
                    # start first encounter, increase counter, set timestamp
                    self.run_encounter(self.current_encounter)
                    self.current_encounter += 1
                    self.last_timestamp = current_time
            else:
                if sprite_count == 0 and current_time - self.board_clear > self.empty_delay:
                    # board is clear for a while, start next encounter, increase counter, set timestamp
                    self.run_encounter(self.current_encounter)
                    self.current_encounter +=1
                    self.last_timestamp = current_time
                elif current_time - self.last_timestamp > self.delay:
                    # it's been too long, start next encounter, increase counter, set timestamp
                    self.run_encounter(self.current_encounter)
                    self.current_encounter +=1
                    self.last_timestamp = current_time
