import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Zombie Simulation")
clock = pygame.time.Clock()


class Human:
    def __init__(self):
        # Start at a random spot, moving in a random direction
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        self.dx = random.uniform(-2, 2)
        self.dy = random.uniform(-2, 2)

    def update(self):
        # Move a little each frame
        self.x += self.dx
        self.y += self.dy
        # Bounce off the edges of the screen
        if self.x < 0 or self.x > WIDTH:
            self.dx = -self.dx
        if self.y < 0 or self.y > HEIGHT:
            self.dy = -self.dy

    def draw(self):
        pygame.draw.circle(screen, (0, 200, 255), (int(self.x), int(self.y)), 6)


humans = [Human() for _ in range(20)]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # UPDATE: every human moves
    for h in humans:
        h.update()

    # DRAW: every human is drawn
    screen.fill((30, 30, 30))
    for h in humans:
        h.draw()
    pygame.display.flip()

    clock.tick(60)

pygame.quit()