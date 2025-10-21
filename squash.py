import pygame

from player import Player

pygame.init()

WIDTH = 480
HEIGHT = 360
FPS = 60

window = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

player1 = Player((50,240),(20,70),(32,32,32))
while True:
    window.fill((255,255,255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    player1.render(window)
    pygame.display.update()
    clock.tick(FPS)