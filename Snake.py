import pygame
import random
import os
pygame.init()
pygame.mixer.init()
screen_width = 900
screen_height = 600
bimg = pygame.image.load("SBag.jpg")
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake by Manmohan")
pygame.transform.scale(bimg, (screen_width, screen_height)).convert_alpha()
pygame.display.update()
font = pygame.font.SysFont(None, 55)
clock = pygame.time.Clock()
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
green = (0, 100, 0)
wel_col = (50, 150, .40)
def Welcome_screen():
    exit_game = False
    while not exit_game:
        screen.fill(wel_col)
        text_screen("Welcome to Snakes", black, 260, 230)
        text_screen("Press Space Bar To Play", black, 220, 290)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()
        pygame.display.update()
def text_screen(text, color, x, y):
    screen_text= font.render(text, True, color)
    screen.blit(screen_text, [x, y])
def plot_snake(gamescr, color, snake_list, snake_size, Snake_size):
    for x,y in snake_list:
        pygame.draw.rect(screen, black, [y, x, snake_size, snake_size])
def gameloop():
    pygame.mixer.music.load("bgm.mp3")
    pygame.mixer.music.play()
    exit_game = False
    game_over = False
    snake_x = 10
    snake_y = 40
    snake_size = 20
    fps = 30
    velocity_x = 0
    velocity_y = 0
    ini_vel = 10
    food_x = random.randint(1, screen_width)
    food_y = random.randint(1, screen_height)
    food_size = 20
    score = 0
    snake_len = 1
    if not os.path.exists("mk.dll"):
        with open("mk.dll", "w") as f:
            f.write("0")
    snake_list = []
    with open("mk.dll", "r") as f:
        higScore = f.read()
    while not exit_game:
        if game_over:
            with open("mk.dll", "w") as f:
                f.write(str(higScore))
            screen.fill(white)
            text_screen(f"SCORE: {score}       HighScore: {higScore}", green, 220, 200)
            text_screen("Game Over, Press enter to continue", red, 125, 275)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                       velocity_y = -ini_vel
                       velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = ini_vel
                        velocity_x = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -ini_vel
                        velocity_y = 0
                    if event.key == pygame.K_RIGHT:
                        velocity_x = ini_vel
                        velocity_y = 0
                    if event.key == pygame.K_BACKSPACE:
                        score+=5
            if abs(snake_x - food_x)<6 and abs(snake_y - food_y)<6:
                score += 10
                food_x = random.randint(1, screen_width-5)
                food_y = random.randint(1, screen_height-5)
                snake_len+=5
            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over=True
                pygame.mixer.music.load("Explosion.wav")
                pygame.mixer.music.play()
            snake_y += velocity_y
            snake_x += velocity_x
            screen.fill(white)
            screen.blit(bimg, (0, 0))
            text_screen(f"SCORE: {score}       HighScore: {str(higScore)}", green, 5, 5)
            pygame.draw.rect(screen, red, [food_x, food_y, food_size, food_size])
            head = []
            head.append(snake_y)
            head.append(snake_x)
            snake_list.append(head)
            if score > int(higScore):
                higScore = score
            if head in snake_list[:-2]:
                game_over= True
            if len(snake_list)>snake_len:
                del snake_list[0]
            plot_snake(screen, black, snake_list, snake_size, snake_size)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()
Welcome_screen()