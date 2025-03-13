import pygame
import config
from bullet import Bullet

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill((0, 128, 255))
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
        
        self.rect.clamp_ip(pygame.Rect(0, 0, config.WIDTH, config.HEIGHT))

    # def shoot(self, bullets_group, all_sprites):
    #     now = pygame.time.get_ticks()
    #     if now - self.last_shot > config.BULLET_DELAY:
    #         bullet = Bullet(self.rect.centerx, self.rect.top)
    #         bullets_group.add(bullet)
    #         all_sprites.add(bullet)
    #         self.last_shot = now
    
    def shoot(self, bullets_group, all_sprites):
        now = pygame.time.get_ticks()
        if now - self.last_shot > config.BULLET_DELAY:
            mouse_x, mouse_y = pygame.mouse.get_pos()  # Captura a posição do mouse
            bullet = Bullet(self.rect.centerx, self.rect.centery, mouse_x, mouse_y)
            bullets_group.add(bullet)
            all_sprites.add(bullet)
            self.last_shot = now
