import pygame
import math
import config
            
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, target_x, target_y):
        super().__init__()
        self.width = 15
        self.height = self.width / 1.82
        self.original_image = pygame.image.load('src/assets/shot.png').convert_alpha()
        self.original_image = pygame.transform.scale(self.original_image, (self.width, self.height))
        self.image = self.original_image  
        self.rect = self.image.get_rect(center=(x, y))

        direction = pygame.math.Vector2(target_x - x, target_y - y)
        if direction.length() > 0:
            direction = direction.normalize()

        self.velocity = direction * config.BULLET_SPEED

    def update(self):
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y
        
        mouse_x, mouse_y = pygame.mouse.get_pos() 
        
        dx = mouse_x - self.rect.centerx
        dy = mouse_y - self.rect.centery

        angle = math.degrees(math.atan2(-dy, dx))

        self.image = pygame.transform.rotate(self.original_image, angle)

        self.rect = self.image.get_rect(center=self.rect.center)

        if not (0 <= self.rect.x <= config.WIDTH and 0 <= self.rect.y <= config.HEIGHT):
            self.kill()