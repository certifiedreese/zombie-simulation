import pygame
import random
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Zombie Simulation")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 28)


class Human:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        self.dx = random.uniform(-2, 2)
        self.dy = random.uniform(-2, 2)

    def update(self):
        self.x += self.dx
        self.y += self.dy
        if self.x < 0 or self.x > WIDTH:
            self.dx = -self.dx
        if self.y < 0 or self.y > HEIGHT:
            self.dy = -self.dy

    def draw(self):
        pygame.draw.circle(screen, (0, 200, 255), (int(self.x), int(self.y)), 6)


class Zombie:
    def __init__(self, x=None, y=None):
        # If no position is given, start somewhere random
        self.x = x if x is not None else random.randint(0, WIDTH)
        self.y = y if y is not None else random.randint(0, HEIGHT)
        self.speed = 1.5

    def update(self, humans):
        closest = None
        closest_dist = float("inf")
        for h in humans:
            d = math.hypot(h.x - self.x, h.y - self.y)
            if d < closest_dist:
                closest = h
                closest_dist = d

        if closest is not None and closest_dist > 0:
            dx = closest.x - self.x
            dy = closest.y - self.y
            self.x += dx / closest_dist * self.speed
            self.y += dy / closest_dist * self.speed

    def draw(self):
        pygame.draw.circle(screen, (80, 220, 80), (int(self.x), int(self.y)), 7)


humans = [Human() for _ in range(20)]
zombies = [Zombie() for _ in range(3)]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # UPDATE: movement
    for h in humans:
        h.update()
    for z in zombies:
        z.update(humans)

    # UPDATE: infection
    new_zombies = []
    for z in zombies:
        for h in humans[:]:
            if math.hypot(h.x - z.x, h.y - z.y) < 13:
                humans.remove(h)
                new_zombies.append(Zombie(h.x, h.y))
    zombies.extend(new_zombies)

    # DRAW
    screen.fill((30, 30, 30))
    for h in humans:
        h.draw()
    for z in zombies:
        z.draw()

    counter = font.render(f"Humans: {len(humans)}   Zombies: {len(zombies)}", True, (255, 255, 255))
    screen.blit(counter, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()