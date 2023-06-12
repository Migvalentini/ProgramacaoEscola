import pygame
import random

# Inicialização do Pygame
pygame.init()

# Definição das cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Configurações da janela do jogo
WIDTH = 800
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo Simples")

# Classe do jogador
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5

# Classe dos inimigos
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(HEIGHT - self.rect.height)

    def update(self):
        self.rect.y += 3
        if self.rect.top > HEIGHT:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)

# Criação do grupo de sprites
all_sprites = pygame.sprite.Group()

# Criação do jogador
player = Player()
all_sprites.add(player)

# Criação dos inimigos
enemies = pygame.sprite.Group()
for _ in range(10):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)

# Loop principal do jogo
running = True
clock = pygame.time.Clock()

while running:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False

   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False
      elif event.type == pygame.KEYDOWN:
         if event.key == pygame.K_ESCAPE:
            running = False

   all_sprites.update()

   # Verifica se o jogador colide com os inimigos
   hits = pygame.sprite.spritecollide(player, enemies, False)
   if hits:
      running = False

   window.fill(WHITE)
   all_sprites.draw(window)
   pygame.display.flip()
   clock.tick(60)

# Finalização do Pygame
pygame.quit()
