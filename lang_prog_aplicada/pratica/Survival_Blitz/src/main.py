import pygame
import sys
import config
from player import Player
from mob import Mob
from menu import Menu, GameOverMenu
from utils.sounds import init_sound
from utils.path import resource_path

def initialize_game():
    pygame.init()
    screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
    background = pygame.image.load(resource_path('assets/background.jpg')).convert()
    pygame.display.set_caption('Survival Blitz')
    clock = pygame.time.Clock()
    
    return screen, background, clock

def setup_game():
    all_sprites = pygame.sprite.Group()
    player = Player()
    all_sprites.add(player)

    bullets = pygame.sprite.Group()
    mobs = pygame.sprite.Group()

    spawn_timers = {
        'normal': pygame.time.get_ticks(),
        'fast': pygame.time.get_ticks(),
        'tank': pygame.time.get_ticks()
    }

    font = pygame.font.Font(None, 36)
    flagSpawnTimeDecrease = [False, False, False, False]
    next_session_time = config.MOB_SPAWN_SESSION['start_time_session']
    
    return all_sprites, player, bullets, mobs, spawn_timers, font, flagSpawnTimeDecrease, next_session_time

def game_loop(screen, background, clock):
    all_sprites, player, bullets, mobs, spawn_timers, font, flagSpawnTimeDecrease, next_session_time = setup_game()
    running = True
    start_time = pygame.time.get_ticks()
    
    while running:
        grass_texture = pygame.transform.scale(background, (150, 150))
        
        for x in range(0, config.WIDTH, grass_texture.get_width()):
            for y in range(0, config.HEIGHT, grass_texture.get_height()):
                screen.blit(grass_texture, (x, y))

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                player.shoot(bullets, all_sprites)
        
        elapsed_time = (pygame.time.get_ticks() - start_time) / 1000   #Em segundos
        
        time = int(elapsed_time)
        sec_time = time % 60
        min_time = time // 60
        if sec_time < 10:
            time_str = f'0{min_time}:0{sec_time}'            
        else:
            time_str = f'0{min_time}:{sec_time}'  
            
        total_time_sec = min_time * 60 + sec_time
            
        for index in range(len(flagSpawnTimeDecrease)):
            if total_time_sec >= next_session_time and not flagSpawnTimeDecrease[index]:
                decrease_spawn_time_mobs(config.MOB_SPAWN_TIME)
                update_time_for_next_session(index, flagSpawnTimeDecrease, next_session_time)
            
        if min_time >= 1:
            return True, time_str
        
        time_surface = font.render(time_str, True, config.WHITE)
        screen.blit(time_surface, (10, 10))
        
        for mob_type, spawn_time in config.MOB_SPAWN_TIME.items():
            if elapsed_time >= config.MOB_SPAWN_START[mob_type]:
                if pygame.time.get_ticks() - spawn_timers[mob_type] > spawn_time:
                    new_mob = Mob(mob_type)
                    mobs.add(new_mob)
                    all_sprites.add(new_mob)
                    spawn_timers[mob_type] = pygame.time.get_ticks()
        
        player.update()
        bullets.update()
        for mob in mobs:
            mob.update(player)
        for bullet in bullets:
            hit_mobs = pygame.sprite.spritecollide(bullet, mobs, False)
            if hit_mobs:
                for mob in hit_mobs:
                    mob.lose_health(1)
                bullet.kill()
                
        if pygame.sprite.spritecollide(player, mobs, False):
            return False, time_str
        
        all_sprites.draw(screen)
        pygame.display.flip()
        
        clock.tick(config.FPS)

def decrease_spawn_time_mobs(mobObj):
    for mob in mobObj:
        mobObj[mob] -= 500

def update_time_for_next_session(index, flagSpawnTimeDecrease, next_session_time):
    next_session_time += config.MOB_SPAWN_SESSION['time_between_sessions']
    flagSpawnTimeDecrease[index] = True

def main():
    screen, background, clock = initialize_game()
    menu = Menu(screen)
    
    while True:
        init_sound('menu_soundtrack')
        action = menu.run()
        if action == 'play':
            init_sound('survive_soundtrack')
            win, survival_time = game_loop(screen, background, clock)
            if not win:
                init_sound('game_over', repeat=1)
            else:
                init_sound('victory', repeat=1)
            game_over_menu = GameOverMenu(screen, win, survival_time)
            action = game_over_menu.run()
            if action == 'menu':
                init_sound('menu_soundtrack')
                continue

if __name__ == '__main__':
    main()