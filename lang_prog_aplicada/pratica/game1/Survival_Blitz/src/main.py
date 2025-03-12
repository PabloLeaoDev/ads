import pygame
import sys

# Inicializando o Pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Survival Blitz")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# FPS (Frames por segundo)
FPS = 60
clock = pygame.time.Clock()

# Classe do jogador
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill((0, 128, 255))
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] or keys[pygame.K_UP]:  # Cima
            self.rect.y -= self.speed
        if keys[pygame.K_s]:  # Baixo
            self.rect.y += self.speed
        if keys[pygame.K_a]:  # Esquerda
            self.rect.x -= self.speed
        if keys[pygame.K_d]:  # Direita
            self.rect.x += self.speed

        # Limites da tela
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

# Grupos de sprites
player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Loop principal do jogo
def game_loop():
    running = True
    while running:
        screen.fill(BLACK)  # Fundo preto

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Atualizando as entidades
        all_sprites.update()

        # Desenhando as entidades
        all_sprites.draw(screen)

        # Atualizar a tela e manter o FPS
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

# Iniciar o jogo
if __name__ == "__main__":
    game_loop()
