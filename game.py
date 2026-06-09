import pygame
import random
import os

# Initialize pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
PINK = (255, 182, 193)

# Screen settings
WIDTH = 900
HEIGHT = 600

gameWindow = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

# Create highscore file if it doesn't exist
if not os.path.exists("highscore.txt"):
    with open("highscore.txt", "w") as f:
        f.write("0")


def score_on_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, (x, y))


def plot_snake(window, color, snake_list, snake_size):
    for x, y in snake_list:
        pygame.draw.rect(window, color, [x, y, snake_size, snake_size])


def welcome():
    while True:
        gameWindow.fill(PINK)

        score_on_screen("Welcome to Snake Game", BLACK, 220, 240)
        score_on_screen("Press SPACE to Play", BLACK, 240, 300)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game()

        pygame.display.update()
        clock.tick(60)


def game():
    # Game variables
    snake_x = 100
    snake_y = 100

    velocity_x = 0
    velocity_y = 0

    snake_size = 20
    snake_length = 1

    speed = 8
    score = 0

    snake_list = []

    apple_x = random.randint(20, WIDTH - 50)
    apple_y = random.randint(20, HEIGHT - 50)

    with open("highscore.txt", "r") as f:
        highscore = int(f.read())

    game_over = False

    while True:

        if game_over:
            gameWindow.fill(WHITE)

            score_on_screen(
                "Game Over! Press ENTER to Restart",
                RED,
                60,
                250,
            )

            score_on_screen(
                f"Score: {score}  High Score: {highscore}",
                BLACK,
                180,
                320,
            )

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return game()

            pygame.display.update()
            clock.tick(60)
            continue

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    velocity_x = speed
                    velocity_y = 0

                elif event.key == pygame.K_LEFT:
                    velocity_x = -speed
                    velocity_y = 0

                elif event.key == pygame.K_UP:
                    velocity_y = -speed
                    velocity_x = 0

                elif event.key == pygame.K_DOWN:
                    velocity_y = speed
                    velocity_x = 0

        # Move snake
        snake_x += velocity_x
        snake_y += velocity_y

        # Eat food
        if abs(snake_x - apple_x) < 20 and abs(snake_y - apple_y) < 20:
            score += 10
            snake_length += 5

            apple_x = random.randint(20, WIDTH - 50)
            apple_y = random.randint(20, HEIGHT - 50)

            if score > highscore:
                highscore = score

                with open("highscore.txt", "w") as f:
                    f.write(str(highscore))

        # Draw screen
        gameWindow.fill(WHITE)

        score_on_screen(
            f"Score: {score}   High Score: {highscore}",
            RED,
            5,
            5,
        )

        pygame.draw.rect(
            gameWindow,
            RED,
            [apple_x, apple_y, snake_size, snake_size],
        )

        # Snake head
        head = [snake_x, snake_y]
        snake_list.append(head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        # Self collision
        if head in snake_list[:-1]:
            game_over = True

        # Wall collision
        if (
            snake_x < 0
            or snake_x > WIDTH - snake_size
            or snake_y < 0
            or snake_y > HEIGHT - snake_size
        ):
            game_over = True

        plot_snake(
            gameWindow,
            BLACK,
            snake_list,
            snake_size,
        )

        pygame.display.update()
        clock.tick(40)


welcome()