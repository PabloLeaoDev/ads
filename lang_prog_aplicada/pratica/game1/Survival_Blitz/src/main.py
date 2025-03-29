import pygame
import sys
import config
from player import Player
from mob import Mob
from menu import Menu, GameOverMenu

def initialize_game():
    pygame.init()
    screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
    pygame.display.set_caption('Survival Blitz')
    clock = pygame.time.Clock()
    return screen, clock

def setup_game():
    # Grupos de sprites
    all_sprites = pygame.sprite.Group()
    player = Player()
    all_sprites.add(player)

    bullets = pygame.sprite.Group()
    mobs = pygame.sprite.Group()

    # Controle de tempo para spawn de mobs
    spawn_timers = {
        "normal": pygame.time.get_ticks(),
        "fast": pygame.time.get_ticks(),
        "tank": pygame.time.get_ticks()
    }

    # Criar uma fonte para o texto
    font = pygame.font.Font(None, 36)
    flagSpawnTimeDecrease = [False, False, False, False]
    next_session_time = config.MOB_SPAWN_SESSION['start_time_session']
    
    return all_sprites, player, bullets, mobs, spawn_timers, font, flagSpawnTimeDecrease, next_session_time

def game_loop(screen, clock):
    all_sprites, player, bullets, mobs, spawn_timers, font, flagSpawnTimeDecrease, next_session_time = setup_game()
    running = True
    start_time = pygame.time.get_ticks()
    
    while running:
        screen.fill(config.BLACK)
        
        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                player.shoot(bullets, all_sprites)
        
        # Atualiza o tempo de jogo
        elapsed_time = (pygame.time.get_ticks() - start_time) / 1000  # Em segundos
        
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
            
        if min_time >= 3:
            # Player wins the game
            return True, time_str
        
        # Renderizar o texto do cronômetro
        time_surface = font.render(time_str, True, config.WHITE)
        screen.blit(time_surface, (10, 10))
        
        # Lógica de spawn de mobs
        for mob_type, spawn_time in config.MOB_SPAWN_TIME.items():
            if elapsed_time >= config.MOB_SPAWN_START[mob_type]:
                if pygame.time.get_ticks() - spawn_timers[mob_type] > spawn_time:
                    new_mob = Mob(mob_type)
                    mobs.add(new_mob)
                    all_sprites.add(new_mob)
                    spawn_timers[mob_type] = pygame.time.get_ticks()
        
        # Atualizações
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
                
        # Checar colisão entre mobs e jogador
        if pygame.sprite.spritecollide(player, mobs, False):
            return False, time_str
        
        # Desenho na tela
        all_sprites.draw(screen)
        pygame.display.flip()
        
        # Controle de FPS
        clock.tick(config.FPS)

def decrease_spawn_time_mobs(mobObj):
    for mob in mobObj:
        mobObj[mob] -= 500

def update_time_for_next_session(index, flagSpawnTimeDecrease, next_session_time):
    next_session_time += config.MOB_SPAWN_SESSION['time_between_sessions']
    flagSpawnTimeDecrease[index] = True

def main():
    screen, clock = initialize_game()
    menu = Menu(screen)
    
    while True:
        action = menu.run()
        if action == "play":
            win, survival_time = game_loop(screen, clock)
            game_over_menu = GameOverMenu(screen, win, survival_time)
            action = game_over_menu.run()
            if action == "menu":
                continue

if __name__ == "__main__":
    main()