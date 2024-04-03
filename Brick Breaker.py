import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BRICK_WIDTH = 80
BRICK_HEIGHT = 30
PADDLE_WIDTH = 120
PADDLE_HEIGHT = 15
BALL_RADIUS = 10

# Game variables
score = 0
bricks = []
for i in range(8):
    for j in range(10):
        brick = pygame.Rect(j * BRICK_WIDTH + 5, i * BRICK_HEIGHT + 50, BRICK_WIDTH - 5, BRICK_HEIGHT - 5)
        bricks.append(brick)
paddle = pygame.Rect(WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT - PADDLE_HEIGHT - 10, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2 - BALL_RADIUS, HEIGHT // 2 - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)
ball_speed_x = 5 * random.choice((1, -1))
ball_speed_y = -5

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Brick Breaker")
clock = pygame.time.Clock()

# Functions
def draw_bricks():
    for brick in bricks:
        pygame.draw.rect(screen, WHITE, brick)

def draw_paddle():
    pygame.draw.rect(screen, WHITE, paddle)

def draw_ball():
    pygame.draw.circle(screen, WHITE, (ball.x + BALL_RADIUS, ball.y + BALL_RADIUS), BALL_RADIUS)

def move_ball():
    global ball_speed_x, ball_speed_y, score
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed_x *= -1
    if ball.top <= 0:
        ball_speed_y *= -1
    if ball.colliderect(paddle):
        ball_speed_y *= -1
    if ball.bottom >= HEIGHT:
        score = 0
        reset_ball()
    for brick in bricks:
        if ball.colliderect(brick):
            bricks.remove(brick)
            ball_speed_y *= -1
            score += 10
            break

def reset_ball():
    global ball_speed_x, ball_speed_y
    ball.center = (WIDTH // 2, HEIGHT // 2)
    ball_speed_x *= random.choice((1, -1))
    ball_speed_y = -5

# Main game loop
running = True
while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.x -= 7
    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.x += 7

    move_ball()

    # Draw everything
    draw_bricks()
    draw_paddle()
    draw_ball()

    # Score
    font = pygame.font.Font(None, 36)
    text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
