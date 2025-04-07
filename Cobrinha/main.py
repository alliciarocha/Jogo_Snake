import pygame, sys
import random
from pygame.locals import *
from button import Button
from snake_game import *

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jogo da Cobrinha")
BG = pygame.image.load("assets/Background.png")
GRID_SIZE = 20
SNAKE_COLOR = (255, 255, 255)
APPLE_COLOR = (255, 0, 0)
SCREEN_COLOR = (0, 0, 0)
SPEED = 10
score = 0

def get_font(size): 
    return pygame.font.Font("assets/font.ttf", size)

def on_grid_random():
    x = random.randint(0, (SCREEN_WIDTH // GRID_SIZE) - 1) * GRID_SIZE
    y = random.randint(0, (SCREEN_HEIGHT // GRID_SIZE) - 1) * GRID_SIZE
    return (x, y)

def collision(c1, c2):
    return c1[0] == c2[0] and c1[1] == c2[1]

def check_collision(snake):
    x, y = snake[0]
    if x < 0 or x >= SCREEN_WIDTH or y < 0 or y >= SCREEN_HEIGHT:
        return True
    if snake[0] in snake[1:]:
        return True
    return False

def show_score(surface):
    font = get_font(36)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    surface.blit(score_text, (10, 10))

def play():
    global score
    score = 0
    snake = [(200, 200), (220, 200), (240, 200)]
    apple_pos = on_grid_random()
    my_direction = get_LEFT()
    clock = pygame.time.Clock()

    while True:
        clock.tick(SPEED)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        my_direction = handle_input(my_direction)

        if check_collision(snake):
            print(f"GAME OVER! Score final: {score}")
            pygame.quit()
            quit()

        if collision(snake[0], apple_pos):
            score += 1
            apple_pos = on_grid_random()
            snake.append((0, 0))

        move_snake(snake, my_direction)

        SCREEN.fill("black")
        draw_game(SCREEN, snake, apple_pos, score, get_font)
        pygame.display.update()

def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("white")
        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)
        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                              text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), 
                             text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), 
                                text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), 
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        SCREEN.blit(MENU_TEXT, MENU_RECT)
        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()

def main():
    main_menu()

if __name__ == "__main__":
    main()