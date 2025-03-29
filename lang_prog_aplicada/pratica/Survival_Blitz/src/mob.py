import random
import pygame
import config

class Mob(pygame.sprite.Sprite):
    def __init__(self, mob_type):
        super().__init__()
        self.type = mob_type
        self.speed = 2 if mob_type == 'normal' else (4 if mob_type == 'fast' else 1)
        self.health = 2 if mob_type == 'normal' else (1 if mob_type == 'fast' else 5)
        self.width = 60
        self.height = 60
        self.image = pygame.Surface((self.width, self.height))
        
        if mob_type == 'normal':
            self.image = pygame.image.load('src/assets/mob_normal.png').convert_alpha()
        elif mob_type == 'fast':
            self.image = pygame.image.load('src/assets/mob_fast.png').convert_alpha()
            self.width = 45
            self.height = 45
        elif mob_type == 'tank':
            self.width = 80
            self.height = 80
            self.image = pygame.image.load('src/assets/mob_tank.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

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
        
    def lose_health(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.kill()