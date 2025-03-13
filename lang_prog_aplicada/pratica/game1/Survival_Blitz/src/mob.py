import random
import pygame
import config

class Mob(pygame.sprite.Sprite):
    def __init__(self, mob_type):
        super().__init__()
        self.type = mob_type
        self.speed = 2 if mob_type == "normal" else (4 if mob_type == "fast" else 1)
        self.health = 3 if mob_type == "normal" else (1 if mob_type == "fast" else 5)
        self.image = pygame.Surface((30, 30))
        self.image.fill((255, 0, 0) if mob_type == "normal" else (0, 255, 0) if mob_type == "fast" else (128, 0, 128))
        
        # Garante que o spawn não seja perto do jogador
        while True:
            self.rect = self.image.get_rect(
                topleft=(random.randint(0, config.WIDTH - 30), random.randint(0, config.HEIGHT - 30))
            )
            if abs(self.rect.x - config.WIDTH // 2) > config.SAFE_SPAWN_DISTANCE or abs(self.rect.y - config.HEIGHT // 2) > config.SAFE_SPAWN_DISTANCE:
                break
    
    def update(self, player):
        direction = pygame.math.Vector2(player.rect.center) - pygame.math.Vector2(self.rect.center)
        if direction.length() > 0:
            direction = direction.normalize()
        self.rect.x += direction.x * self.speed
        self.rect.y += direction.y * self.speed
