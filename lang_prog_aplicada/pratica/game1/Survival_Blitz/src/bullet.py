import pygame
import config

# class Bullet(pygame.sprite.Sprite):
#     def __init__(self, x, y):
#         super().__init__()
#         self.image = pygame.Surface((5, 10))
#         self.image.fill((255, 255, 0))
#         self.rect = self.image.get_rect(center=(x, y))
#         self.speed = config.BULLET_SPEED
    
#     def update(self):
#         self.rect.y -= self.speed
#         if self.rect.bottom < 0:
#             self.kill()
            
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, target_x, target_y):
        super().__init__()
        self.image = pygame.Surface((5, 5))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect(center=(x, y))

        # Calcula a direção do tiro
        direction = pygame.math.Vector2(target_x - x, target_y - y)
        if direction.length() > 0:
            direction = direction.normalize()

        self.velocity = direction * config.BULLET_SPEED

    def update(self):
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y

        # Remove a bala se sair da tela
        if not (0 <= self.rect.x <= config.WIDTH and 0 <= self.rect.y <= config.HEIGHT):
            self.kill()
