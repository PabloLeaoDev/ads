import pygame
import sys
import config
from player import Player
from mob import Mob

# Inicializando o Pygame
pygame.init()
screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
pygame.display.set_caption('Survival Blitz')
clock = pygame.time.Clock()

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

# Loop principal do jogo
def game_loop():
    running = True
    start_time = pygame.time.get_ticks()
    
    while running:
        screen.fill(config.BLACK)
        
        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                player.shoot(bullets, all_sprites)
        
        # Atualiza o tempo de jogo
        elapsed_time = (pygame.time.get_ticks() - start_time) / 1000  # Em segundos
        
        # Lógica de spawn de mobs
        for mob_type, spawn_time in config.MOB_SPAWN_TIME.items():
            if elapsed_time >= config.MOB_SPAWN_START[mob_type]:
                if pygame.time.get_ticks() - spawn_timers[mob_type] > spawn_time:
                    new_mob = Mob(mob_type)
                    mobs.add(new_mob)
                    all_sprites.add(new_mob)
                    spawn_timers[mob_type] = pygame.time.get_ticks()
        
        # Atualizações
        player.update()  # Atualiza o jogador
        bullets.update()  # Atualiza as balas
        for mob in mobs:
            mob.update(player)  # passsa o jogador como argumento para os mobs
        
        # Checar colisões (balas x mobs)
        for bullet in bullets:
            hit_mobs = pygame.sprite.spritecollide(bullet, mobs, False)
            if hit_mobs:
                for mob in mobs:
                    mob.lose_health(1)
                bullet.kill()
                
        # Checar colisão entre mobs e jogador
        if pygame.sprite.spritecollide(player, mobs, False):
            running = False  # Jogador morre e o jogo termina
        
        # Desenho na tela
        all_sprites.draw(screen)
        pygame.display.flip()
        
        # Controle de FPS
        clock.tick(config.FPS)
    
    pygame.quit()
    sys.exit()

# Iniciar o jogo
if __name__ == "__main__":
    game_loop()