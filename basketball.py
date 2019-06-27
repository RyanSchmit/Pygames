import pygame
import sys
import random

pygame.init()
# screen
screen_width = 1350
screen_height = 670
screen = pygame.display.set_mode((screen_width, screen_height))

# basketball hoop
hoop_pos = [500, 500]
hoop_width = 100
hoop_height = 100
basket = pygame.image.load("basketball hoop.png")
basket = pygame.transform.scale(basket, (hoop_width, hoop_height))

# basketball
radius_basketball = 15
orange = 255, 128, 0
basketball_pos = [random.randint(0, screen_width - radius_basketball), 20]
basketball_list = [basketball_pos]
speed_basketball = 20

# colors
white = 255, 255, 255

# clock
clock = pygame.time.Clock()
start = 900

# score
score = 0

# background
background_width = 1350
background_height = 670
background_pos = [0, 0]
background = pygame.image.load("Basketball court.jpg")
background = pygame.transform.scale(background, (background_width, background_height))


def timer(clock):
    font = pygame.font.SysFont("comicsans", 30, True)
    text = font.render("Timer: " + str(clock), 1, white)
    screen.blit(text, (10, 10))


def draw_basketball(basketball_list):
    for basketball_pos in basketball_list:
       pygame.draw.circle(screen, orange, (basketball_pos[0], basketball_pos[1]), radius_basketball)


def update_basketball_position(basketball_list):
    for idx, basketball_pos in enumerate(basketball_list):
        if basketball_pos[1] >= 0 and basketball_pos[1] < screen_height:
            basketball_pos[1] += speed_basketball
        else:
            basketball_list.pop(idx)


def collision_check(basketball_list, hoop_pos):
    for basketball_pos in basketball_list:
        if detect_collision(hoop_pos, basketball_pos):
            return True
        return False


def detect_collision(hoop_pos, basketball_pos):
    h_x = hoop_pos[0]
    h_y = hoop_pos[1]

    b_x = basketball_pos[0]
    b_y = basketball_pos[1]

    if (b_x >= h_x and b_x < (h_x + hoop_width)) or (h_x >= b_x and h_x < (b_x + radius_basketball)):
        if (b_y >= h_y and b_y < (h_y + hoop_width)) or (h_y >= b_y and h_y < (b_y + radius_basketball)):
            return True
    return False


def baskets_scored(score):
    font = pygame.font.SysFont("comicsans", 30, True)
    text = font.render("Score: " + str(score), 1, white)
    screen.blit(text, (1200, 10))


game_over = False
while not game_over:
    for event in pygame.event.get():
        screen.blit(background, (background_pos[0], background_pos[1]))
        # moving basketball hoop
        key = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            sys.exit()
        if key[pygame.K_LEFT]:
            hoop_pos[0] -= hoop_width-5
        if key[pygame.K_RIGHT]:
            hoop_pos[0] += hoop_width-5
    # clock
    start -= 1
    if start <= 0:
        game_over = True
    clock.tick(15)

    if basketball_pos[1] >= 0 and basketball_pos[1] < screen_height:
        basketball_pos[1] += 20
    else:
        basketball_pos[0] = random.randint(0, screen_width-radius_basketball)
        basketball_pos[1] = 0
    if collision_check(basketball_list, hoop_pos):
        score += 1
    baskets_scored(score)
    draw_basketball(basketball_list)
    # draw basketball hoop
    screen.blit(basket, (hoop_pos[0], hoop_pos[1]))
    pygame.display.flip()
    screen.blit(background, (background_pos[0], background_pos[1]))
    timer(clock)
    if game_over == True:
        print("Score: " + str(score))


