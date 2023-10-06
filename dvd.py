import pygame
import random

class Ball:
    def __init__(self, screen_width, screen_height, radius=15, speed=(200, 200)):
        self.radius = radius
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.speed = pygame.Vector2(speed)
        self.position = pygame.Vector2(random.randint(radius, screen_width - radius), random.randint(radius, screen_height - radius))
        self.color = pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def update(self, dt):
        self.position += self.speed * dt

        if self.position.y >= self.screen_height - self.radius or self.position.y <= self.radius:
            self.speed.y = -self.speed.y
        if self.position.x >= self.screen_width - self.radius or self.position.x <= self.radius:
            self.speed.x = -self.speed.x

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.position.x), int(self.position.y)), self.radius)

# pygame setup
pygame.init()
screen_width, screen_height = 720, 576
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True
dt = 0

balls = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Add a new ball where the user clicked
            x, y = event.pos
            new_ball = Ball(screen_width, screen_height, speed=(random.randint(100, 300), random.randint(100, 300)))
            new_ball.position = pygame.Vector2(x, y)
            balls.append(new_ball)

    screen.fill("green")

    for ball in balls:
        ball.update(dt)
        ball.draw(screen)

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
