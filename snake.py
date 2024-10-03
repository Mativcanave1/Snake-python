import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
APPLE = (255, 255, 0)
BACK_GROUND = (50, 153, 213)

dis_width = 600
dis_height = 400

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def our_snake(snake_block, snake_list, color):
    for x in snake_list:
        pygame.draw.rect(dis, color, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

def gameLoop():
    game_over = False
    game_close = False

    x1, y1 = dis_width / 4, dis_height / 2
    x1_change, y1_change = 0, 0
    snake_List1 = []
    Length_of_snake1 = 1

    x2, y2 = dis_width * 3 / 4, dis_height / 2
    x2_change, y2_change = 0, 0
    snake_List2 = []
    Length_of_snake2 = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    foodx2 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody2 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    player1_alive = True
    player2_alive = True

    while not game_over:
        while game_close:
            dis.fill(BACK_GROUND)
            message("You Lost! Press C-Play Again or Q-Quit", red)
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
                if player1_alive:
                    if event.key == pygame.K_LEFT and x1_change == 0:
                        x1_change = -snake_block
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT and x1_change == 0:
                        x1_change = snake_block
                        y1_change = 0
                    elif event.key == pygame.K_UP and y1_change == 0:
                        y1_change = -snake_block
                        x1_change = 0
                    elif event.key == pygame.K_DOWN and y1_change == 0: 
                        y1_change = snake_block
                        x1_change = 0

                if player2_alive:
                    if event.key == pygame.K_a and x2_change == 0:
                        x2_change = -snake_block
                        y2_change = 0
                    elif event.key == pygame.K_d and x2_change == 0:
                        x2_change = snake_block
                        y2_change = 0
                    elif event.key == pygame.K_w and y2_change == 0:
                        y2_change = -snake_block
                        x2_change = 0
                    elif event.key == pygame.K_s and y2_change == 0: 
                        y2_change = snake_block
                        x2_change = 0

        if player1_alive:
            if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
                player1_alive = False
            if [x1, y1] in snake_List1[:-1] or [x1, y1] in snake_List2:
                player1_alive = False
        else:
            x1 = -1
            y1 = -1
            snake_List1 = []

        if player2_alive:
            if x2 >= dis_width or x2 < 0 or y2 >= dis_height or y2 < 0:
                player2_alive = False
            if [x2, y2] in snake_List2[:-1] or [x2, y2] in snake_List1:
                player2_alive = False
        else:
            x2 = -1
            y2 = -1
            snake_List2 = []

        if not player1_alive and not player2_alive:
            game_close = True

        if player1_alive:
            x1 += x1_change
            y1 += y1_change
            snake_Head1 = [x1, y1]
            snake_List1.append(snake_Head1)
            if len(snake_List1) > Length_of_snake1:
                del snake_List1[0]

        if player2_alive:
            x2 += x2_change
            y2 += y2_change
            snake_Head2 = [x2, y2]
            snake_List2.append(snake_Head2)
            if len(snake_List2) > Length_of_snake2:
                del snake_List2[0]

        dis.fill(BACK_GROUND)
        pygame.draw.rect(dis, APPLE, [foodx, foody, snake_block, snake_block])
        pygame.draw.rect(dis, APPLE, [foodx2, foody2, snake_block, snake_block])

        if player1_alive:
            our_snake(snake_block, snake_List1, black)


        if player2_alive:
            our_snake(snake_block, snake_List2, red)

        pygame.display.update()

        if player1_alive:
            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                Length_of_snake1 += 1
            if x1 == foodx2 and y1 == foody2:
                foodx2 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                foody2 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                Length_of_snake1 += 1

        if player2_alive:
            if x2 == foodx and y2 == foody:
                foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                Length_of_snake2 += 1
            if x2 == foodx2 and y2 == foody2:
                foodx2 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                foody2 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                Length_of_snake2 += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
