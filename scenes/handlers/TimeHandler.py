import pygame

class TimeHandler():

    def __init__(self, scene, endless_mode_bool, time_limit = None):
        self.my_scene = scene
        if (time_limit != None):
            # the level is counting time down til boss fight for progress through level
            # we save our time-amount here so we can use it with elapsed time to see where we currently are
            # time given in seconds by scene
            self.time_limit = time_limit
        # True if we are in endless mode - else it's a normal level, so we count down the time til End-Fight
        self.endless = endless_mode_bool

        # get ticks from pygame to keep track of time elapsed
        self.start_time = pygame.time.get_ticks()
        print("We started on this tick: " + str(self.start_time))
        self.elapsed_time = 0

    def set_time_display(self, time_display):
        self.time_display = time_display

    def track_level_time(self):
        time_elapsed = pygame.time.get_ticks() - self.start_time
        print ("This is the elapsed time now: " + str(time_elapsed))
        return time_elapsed

    def update(self):
        self.elapsed_time = self.track_level_time()
        if (self.time_display):
            self.time_display.update_time_value(self.elapsed_time)
            self.time_display.update()
        print(self.elapsed_time)
