import pygame.mixer
from pygame import mixer

class SoundController:

    def __init__(self):
        pygame.mixer.init()
        self.currently_playing = None

        # effects loaded
        self.enemy_shot = pygame.mixer.Sound('assets/sounds/Shoot_00.mp3')
        self.exploding_enemy = pygame.mixer.Sound('assets/sounds/Explosion_04.mp3')
        self.bubble_shot = pygame.mixer.Sound('assets/sounds/pop.ogg')

        # music loaded
        self.title_music = pygame.mixer.Sound('assets/music/juhani_junkala_retro-game-music-pack_title_screen.ogg')
        self.tut_music = pygame.mixer.Sound('assets/music/juhani_junkala_retro-game-music-pack_ending.ogg')
        self.play_music = pygame.mixer.Sound('assets/music/juhani_junkala_retro-game-music-pack_level2.ogg')
        self.endless_music = pygame.mixer.Sound('assets/music/juhani_junkala_retro-game-music-pack_level3.ogg')

        self.sound = True
        self.music = True


    def play_sound(self, sound_file):
        """
        Method to trigger sound effects
        :param sound_file: String to name the desired effect
        :return:
        """
        if self.sound:
            if sound_file == 'enemy_shot':
                self.enemy_shot.play()
            elif sound_file == 'exploding_enemy':
                self.exploding_enemy.play()
            elif sound_file == 'bubble_shot':
                self.bubble_shot.play()

    def loop_music(self, music):
        """
        Method to loop music for the scene
        :param music_file:
        :return:
        """
        if self.music:
            if music == 0:
                self.title_music.play(-1, 0, 500)
                self.currently_playing = self.title_music
            elif music == 1:
                self.tut_music.play(-1, 0, 500)
                self.currently_playing = self.tut_music
            elif music == 2:
                self.play_music.play(-1, 0, 500)
                self.currently_playing = self.play_music
            elif music == 3:
                self.endless_music.play(-1, 0, 500)
                self.currently_playing = self.endless_music
            # elif music == 4:
            #     self.tut_music.play(99)
            #     self.currently_playing = self.tut_music
