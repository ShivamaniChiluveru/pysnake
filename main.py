import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 600, 400
screen = pygame.display.set_mode((width, height))

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (213, 50, 80)
green = (0, 255, 0)

# Snake settings
snake_block = 10
snake_speed = 5
clock = pygame.time.Clock()

# Fonts
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


def your_score(score):
    value = score_font.render("Your Score: " + str(score), True, white)
    screen.blit(value, [0, 0])


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, green, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [width / 6, height / 3])


def gameLoop():
    game_over = False
    game_close = False

    # Initial position of snake
    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    # Egg positions
    egg_positions = []
    num_eggs = 3  # Number of eggs

    for _ in range(num_eggs):
        egg_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
        egg_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
        egg_positions.append((egg_x, egg_y))

    while not game_over:

        while game_close:
            screen.fill(black)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            your_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        screen.fill(black)

        for egg_pos in egg_positions:
            pygame.draw.rect(
                screen, red,
                [egg_pos[0], egg_pos[1], snake_block, snake_block])

        our_snake(snake_block, snake_list)
        your_score(length_of_snake - 1)

        pygame.display.update()

        # Check if snake has eaten any eggs
        for egg_pos in egg_positions:
            if x1 == egg_pos[0] and y1 == egg_pos[1]:
                length_of_snake += 1
                egg_positions.remove(egg_pos)
                # Add a new egg
                new_egg_x = round(
                    random.randrange(0, width - snake_block) / 10.0) * 10.0
                new_egg_y = round(
                    random.randrange(0, height - snake_block) / 10.0) * 10.0
                egg_positions.append((new_egg_x, new_egg_y))

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()
