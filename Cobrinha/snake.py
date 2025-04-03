import pygame
import random
from pygame.locals import *

pygame.init()

GAME_WIDTH = 600
GAME_HEIGHT = 600
GRID_SIZE = 10
SNAKE_COLOR = (255, 255, 255)
APPLE_COLOR = (255, 0, 0)
SCREEN_COLOR = (0, 0, 0)
SPEED = 10

SCREEN = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
pygame.display.set_caption('Jogo da Cobrinha')

score = 0

def on_grid_random():
    x = random.randint(0, (GAME_WIDTH // GRID_SIZE) - 1) * GRID_SIZE
    y = random.randint(0, (GAME_HEIGHT // GRID_SIZE) - 1) * GRID_SIZE
    return (x, y)

def collision(c1, c2):
    return c1[0] == c2[0] and c1[1] == c2[1]

def check_collision(snake):
    x, y = snake[0]

    if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT:
        return True
    
    if snake[0] in snake[1:]:
        return True

    return False  
def show_score():
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    SCREEN.blit(score_text, (10, 10))

def main():
    global score  

    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    snake = [(200, 200), (210, 200), (220, 200)]
    snake_skin = pygame.Surface((GRID_SIZE, GRID_SIZE))
    snake_skin.fill(SNAKE_COLOR)

    apple_pos = on_grid_random()
    apple = pygame.Surface((GRID_SIZE, GRID_SIZE))
    apple.fill(APPLE_COLOR)

    my_direction = LEFT
    clock = pygame.time.Clock()

    while True:
        clock.tick(SPEED)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()  

            if event.type == KEYDOWN:
                if event.key == K_UP and my_direction != DOWN:
                    my_direction = UP
                if event.key == K_DOWN and my_direction != UP:
                    my_direction = DOWN
                if event.key == K_LEFT and my_direction != RIGHT:
                    my_direction = LEFT
                if event.key == K_RIGHT and my_direction != LEFT:
                    my_direction = RIGHT

        if check_collision(snake):
            print(f"GAME OVER! Score final: {score}")
            pygame.quit()
            quit()

        if collision(snake[0], apple_pos):
            score += 1  
            apple_pos = on_grid_random()
            snake.append((0, 0))  

        for i in range(len(snake) - 1, 0, -1):
            snake[i] = snake[i - 1]

        if my_direction == UP:
            snake[0] = (snake[0][0], snake[0][1] - GRID_SIZE)
        if my_direction == DOWN:
            snake[0] = (snake[0][0], snake[0][1] + GRID_SIZE)
        if my_direction == RIGHT:
            snake[0] = (snake[0][0] + GRID_SIZE, snake[0][1])
        if my_direction == LEFT:
            snake[0] = (snake[0][0] - GRID_SIZE, snake[0][1])

        SCREEN.fill(SCREEN_COLOR)
        show_score()
        SCREEN.blit(apple, apple_pos)
        for pos in snake:
            SCREEN.blit(snake_skin, pos)

        pygame.display.update()

if __name__ == "__main__":
    main()