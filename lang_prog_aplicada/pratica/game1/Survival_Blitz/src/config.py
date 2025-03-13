# config.py - Configurações do jogo
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PLAYER_SPEED = 5
BULLET_SPEED = 10
BULLET_DELAY = 300  # Delay entre tiros (ms)
MOB_SPAWN_TIME = {  # Tempo de spawn para cada tipo de mob (ms)
    "normal": 1500,
    "fast": 2000,
    "tank": 3000 
}
MOB_SPAWN_START = {  # Tempo para iniciar o spawn de cada tipo de mob (s)
    "normal": 0,
    "fast": 10,
    "tank": 20
}
SAFE_SPAWN_DISTANCE = 300  # Distância segura para spawn de mobs em relação ao jogador