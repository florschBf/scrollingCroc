import pygame


class TimeHandler:
    """
    class to handle the time spend in the scene - used to track level progress
    """

    def __init__(self, scene, endless_mode_bool, time_limit=None):
        self.my_scene = scene
        if time_limit is not None:
            # the level is counting time down til boss fight for progress through level
            # we save our time-amount here so we can use it with elapsed time to see where we currently are
            # time given in seconds by scene - deprecated, not using it like this
            self.time_limit = time_limit
            print("tutorial time limit: " + str(self.time_limit))
        # True if we are in endless mode - else it's a normal level, so we count down the time til End-Fight
        self.endless = endless_mode_bool

        # get ticks from pygame to keep track of time elapsed
        self.start_time = pygame.time.get_ticks()
        print("We started on this tick: " + str(self.start_time))
        self.elapsed_time = 0

        # save time we spend outside of this scene, so we can subtract it later
        self.pause_point = 0
        self.resume_point = 0
        self.elapsed_elsewhere = 0

        # set in scene if display wanted
        self.time_display = None

    def set_time_display(self, time_display):
        print("setting time_display to display time on")
        self.time_display = time_display
        print(self.time_display)

    def pause_time(self):
        """
        Method triggers when we leave the scene to keep time count synced with actual playtime
        :return:
        """
        self.pause_point = pygame.time.get_ticks()

    def resume_time(self):
        """
        Method triggers when we resume the scene to keep time count synced with actual playtime
        :return:
        """
        self.resume_point = pygame.time.get_ticks()
        self.elapsed_elsewhere += self.resume_point - self.pause_point

    def track_level_time(self):
        time_elapsed = (pygame.time.get_ticks() - self.elapsed_elsewhere) / 1000
        if self.endless:
            return time_elapsed
        else:
            return self.time_limit - time_elapsed

    def update(self):
        self.elapsed_time = self.track_level_time()
        if self.time_display is not None:
            self.time_display.update_time_value(self.track_level_time())
            self.time_display.update()
