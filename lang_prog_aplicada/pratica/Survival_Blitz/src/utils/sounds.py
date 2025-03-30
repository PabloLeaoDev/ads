import pygame

def init_sound(music: str, volume = 0.5, repeat = -1, effect = False):
    pygame.mixer.init()
    if not effect:
        pygame.mixer.music.load(f'assets/sounds/{music}.mp3')
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(repeat)
    else:
        gunshot_sound = pygame.mixer.Sound(f'assets/sounds/{music}.mp3')
        gunshot_sound.set_volume(0.2)
        gunshot_sound.play()