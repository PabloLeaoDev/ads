import pygame
import math
import config
from bullet import Bullet
from utils.sounds import init_sound
from utils.path import resource_path

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.original_image = pygame.image.load(resource_path('assets/player.png')).convert_alpha() 
        self.original_image = pygame.transform.scale(self.original_image, (60, 60)) 
        self.image = self.original_image 
        self.rect = self.image.get_rect(center=(config.WIDTH // 2, config.HEIGHT // 2))
        self.speed = config.PLAYER_SPEED
        self.last_shot = pygame.time.get_ticks()
    
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.rect.y += self.speed
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        
        mouse_x, mouse_y = pygame.mouse.get_pos() 
        
        dx = mouse_x - self.rect.centerx
        dy = mouse_y - self.rect.centery

        angle = math.degrees(math.atan2(-dy, dx))  
        
        self.image = pygame.transform.rotate(self.original_image, angle)

        self.rect = self.image.get_rect(center=self.rect.center)

        self.rect.clamp_ip(pygame.Rect(0, 0, config.WIDTH, config.HEIGHT))
    
    def shoot(self, bullets_group, all_sprites):
        now = pygame.time.get_ticks()
        if now - self.last_shot > config.BULLET_DELAY:
            mouse_x, mouse_y = pygame.mouse.get_pos() 
            bullet = Bullet(self.rect.centerx, self.rect.centery, mouse_x, mouse_y)
            bullets_group.add(bullet)
            all_sprites.add(bullet)
            init_sound('gunshot', repeat=1, effect=True)
            self.last_shot = now
