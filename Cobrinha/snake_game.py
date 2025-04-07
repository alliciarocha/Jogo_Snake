import pygame
import random

GRID_SIZE = 20
SNAKE_COLOR = (255, 255, 255)
APPLE_COLOR = (255, 0, 0)
SCREEN_COLOR = (0, 0, 0)
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SPEED = 10

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

def get_LEFT():
    return LEFT

def on_grid_random():
    x = random.randint(0, (SCREEN_WIDTH // GRID_SIZE) - 1) * GRID_SIZE
    y = random.randint(0, (SCREEN_HEIGHT // GRID_SIZE) - 1) * GRID_SIZE
    return (x, y)

def collision(c1, c2):
    return c1 == c2

def check_collision(snake):
    x, y = snake[0]
    return (
        x < 0 or x >= SCREEN_WIDTH or
        y < 0 or y >= SCREEN_HEIGHT or
        snake[0] in snake[1:]
    )

def move_snake(snake, direction):
    for i in range(len(snake) - 1, 0, -1):
        snake[i] = snake[i - 1]

    x, y = snake[0]
    if direction == UP:
        y -= GRID_SIZE
    elif direction == DOWN:
        y += GRID_SIZE
    elif direction == LEFT:
        x -= GRID_SIZE
    elif direction == RIGHT:
        x += GRID_SIZE
    snake[0] = (x, y)

def handle_input(direction):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and direction != DOWN:
        return UP
    if keys[pygame.K_DOWN] and direction != UP:
        return DOWN
    if keys[pygame.K_LEFT] and direction != RIGHT:
        return LEFT
    if keys[pygame.K_RIGHT] and direction != LEFT:
        return RIGHT
    return direction

def draw_game(surface, snake, apple_pos, score, get_font):
    game_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_surface.fill(SCREEN_COLOR)

    font = get_font(36)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    game_surface.blit(score_text, (10, 10))

    snake_skin = pygame.Surface((GRID_SIZE, GRID_SIZE))
    snake_skin.fill(SNAKE_COLOR)

    apple = pygame.Surface((GRID_SIZE, GRID_SIZE))
    apple.fill(APPLE_COLOR)
    game_surface.blit(apple, apple_pos)

    for pos in snake:
        game_surface.blit(snake_skin, pos)

    surface.blit(game_surface, (0, 0))
