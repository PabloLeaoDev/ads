import pygame
import sys
import config

class Button:
    def __init__(self, x, y, width, height, text, color, hover_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.is_hovered = False
        self.font = pygame.font.Font(None, 36)
        
    def draw(self, surface):
        color = self.hover_color if self.is_hovered else self.color
        pygame.draw.rect(surface, color, self.rect, border_radius=10)
        pygame.draw.rect(surface, config.WHITE, self.rect, 2, border_radius=10)
        
        text_surface = self.font.render(self.text, True, config.WHITE)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)
        
    def check_hover(self, pos):
        self.is_hovered = self.rect.collidepoint(pos)
        return self.is_hovered
        
    def is_clicked(self, pos, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            return self.rect.collidepoint(pos)
        return False

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.buttons = [
            Button(config.WIDTH//2 - 100, config.HEIGHT//2 + 60, 200, 50, 'Jogar', (0, 100, 0), (0, 150, 0)),
            Button(config.WIDTH//2 - 100, config.HEIGHT//2 + 120, 200, 50, 'Sair', (100, 0, 0), (150, 0, 0))
        ]
        self.title_font = pygame.font.Font(None, 72)
        self.instructions_font = pygame.font.Font(None, 24)
        self.background = pygame.Surface((config.WIDTH, config.HEIGHT))
        self.background.fill((20, 20, 40))
        
    def run(self):
        running = True
        while running:
            mouse_pos = pygame.mouse.get_pos()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                for button in self.buttons:
                    if button.is_clicked(mouse_pos, event):
                        if button.text == 'Jogar':
                            return 'play'
                        elif button.text == 'Sair':
                            pygame.quit()
                            sys.exit()
            
            self.screen.blit(self.background, (0, 0))
            
            title_surface = self.title_font.render('Survival Blitz', True, config.WHITE)
            title_rect = title_surface.get_rect(center=(config.WIDTH//2, config.HEIGHT//4))
            self.screen.blit(title_surface, title_rect)
            
            instructions = [
                'Sobreviva por 1 minuto contra hordas de zumbis!',
                'WASD ou Setas: Movimentação',
                'Mouse: Atirar na direção do cursor',
                'Zumbis: Verde (Normal), Vermelho (Rápido), Roxo (Tanque)'
            ]
            
            for i, line in enumerate(instructions):
                text_surface = self.instructions_font.render(line, True, config.WHITE)
                text_rect = text_surface.get_rect(center=(config.WIDTH//2, config.HEIGHT//3 + i*30))
                self.screen.blit(text_surface, text_rect)
            
            for button in self.buttons:
                button.check_hover(mouse_pos)
                button.draw(self.screen)
            
            pygame.display.flip()
            pygame.time.Clock().tick(config.FPS)

class GameOverMenu:
    def __init__(self, screen, win=False, survival_time='00:00'):
        self.screen = screen
        self.win = win
        self.survival_time = survival_time
        self.buttons = [
            Button(config.WIDTH//2 - 100, config.HEIGHT//2 + 50, 200, 50, 'Menu', (0, 0, 100), (0, 0, 150)),
            Button(config.WIDTH//2 - 100, config.HEIGHT//2 + 110, 200, 50, 'Sair', (100, 0, 0), (150, 0, 0))
        ]
        self.title_font = pygame.font.Font(None, 72)
        self.result_font = pygame.font.Font(None, 48)
        self.background = pygame.Surface((config.WIDTH, config.HEIGHT))
        self.background.fill((20, 20, 40))
        
    def run(self):
        running = True
        while running:
            mouse_pos = pygame.mouse.get_pos()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                for button in self.buttons:
                    if button.is_clicked(mouse_pos, event):
                        if button.text == 'Menu':
                            return 'menu'
                        elif button.text == 'Sair':
                            pygame.quit()
                            sys.exit()
            
            self.screen.blit(self.background, (0, 0))
            
            title = 'Vitória!' if self.win else 'Game Over'
            title_surface = self.title_font.render(title, True, (0, 255, 0) if self.win else (255, 0, 0))
            title_rect = title_surface.get_rect(center=(config.WIDTH//2, config.HEIGHT//4))
            self.screen.blit(title_surface, title_rect)
            
            time_text = f'Tempo: {self.survival_time}'
            time_surface = self.result_font.render(time_text, True, config.WHITE)
            time_rect = time_surface.get_rect(center=(config.WIDTH//2, config.HEIGHT//2))
            self.screen.blit(time_surface, time_rect)
            
            for button in self.buttons:
                button.check_hover(mouse_pos)
                button.draw(self.screen)
            
            pygame.display.flip()
            pygame.time.Clock().tick(config.FPS)