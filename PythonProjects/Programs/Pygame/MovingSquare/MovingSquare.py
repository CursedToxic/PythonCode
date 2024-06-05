import pygame

pygame.init()
pygame.display.set_caption("Moving Square")
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
canvas = pygame.Surface((SCREEN_WIDTH,SCREEN_HEIGHT))
window = pygame.display.set_mode(((SCREEN_WIDTH,SCREEN_HEIGHT)))
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
TARGET_FPS = 60
running = True
x = 10
y = 10
FPS = 240
SPEED = 1
clock = pygame.time.Clock()

while running:
  for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
              running = False
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                x -= SPEED
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                x += SPEED
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                y -= SPEED
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                y += SPEED
  keys = pygame.key.get_pressed()
  if keys[pygame.K_LEFT]:
    x -= SPEED
  if keys[pygame.K_RIGHT]:
    x += SPEED
  if keys[pygame.K_UP]:
    y -= SPEED
  if keys[pygame.K_DOWN]:
    y += SPEED
  screen.fill((255, 255, 255))
  pygame.draw.rect(screen, (0, 0, 0), (x, y, 50, 50))
  clock.tick(FPS)
  pygame.display.flip()
pygame.quit()