import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Zombie Simulation")
clock = pygame.time.Clock()

running = True
while running:
    # 1. INPUT: check what the player did
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2. UPDATE: move things (nothing yet)

    # 3. DRAW: paint the screen
    screen.fill((30, 30, 30))
    pygame.draw.circle(screen, (0, 200, 255), (400, 300), 6)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
