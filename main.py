import pygame
import random
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Zombie Simulation")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 28)
big_font = pygame.font.SysFont(None, 60)

# Simulation settings
NUM_HUMANS = 20
NUM_ZOMBIES = 3
FIGHT_CHANCE = 0.4  # 40% chance a human kills the zombie instead of being infected


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


def new_game():
    humans = [Human() for _ in range(NUM_HUMANS)]
    zombies = [Zombie() for _ in range(NUM_ZOMBIES)]
    return humans, zombies


humans, zombies = new_game()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Press R to restart
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            humans, zombies = new_game()

    # UPDATE: movement
    for h in humans:
        h.update()
    for z in zombies:
        z.update(humans)

    # UPDATE: fights
    new_zombies = []
    dead_zombies = []
    for z in zombies:
        for h in humans[:]:
            if math.hypot(h.x - z.x, h.y - z.y) < 13:
                if random.random() < FIGHT_CHANCE:
                    # Human wins: the zombie is destroyed
                    dead_zombies.append(z)
                    break
                else:
                    # Zombie wins: the human becomes a zombie
                    humans.remove(h)
                    new_zombies.append(Zombie(h.x, h.y))
    for z in dead_zombies:
        zombies.remove(z)
    zombies.extend(new_zombies)

    # DRAW
    screen.fill((30, 30, 30))
    for h in humans:
        h.draw()
    for z in zombies:
        z.draw()

    counter = font.render(f"Humans: {len(humans)}   Zombies: {len(zombies)}", True, (255, 255, 255))
    screen.blit(counter, (10, 10))

    # Show who won
    message = None
    if len(zombies) == 0:
        message = "Humans survived!"
    elif len(humans) == 0:
        message = "Zombies took over!"
    if message:
        text = big_font.render(message, True, (255, 255, 255))
        screen.blit(text, text.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
        hint = font.render("Press R to restart", True, (200, 200, 200))
        screen.blit(hint, hint.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50)))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()