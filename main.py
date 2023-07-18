# Importing Modules
import pygame, sys, random, time, os
# General Setups
os.environ['SDL_VIDEO_CENTERED'] = "1"
pygame.font.init()
pygame.mixer.init()
pygame.init()
info = pygame.display.Info()
clock = pygame.time.Clock()

# Speed
ball_speed_x = 10 * random.choice((1, -1))
ball_speed_y = 10 * random.choice((1, -1))
player_speed = 15
opponent_speed = 15

# Sounds
HIT_SOUND =  pygame.mixer.Sound(
    os.path.join("boing.mp3"))
GAMEOVER_SOUND =  pygame.mixer.Sound(
    os.path.join("over.mp3"))
# fonts
HEALTH_FONT = pygame.font.SysFont("comicsans", 40)
WINNER_FONT = pygame.font.SysFont("comicsans", 40)
# Colors
BG_COLOR = pygame.Color("grey12")
LIGHT_GREY = (200, 200, 200)
BLUE = (72, 52, 250)
RED = (250, 52, 59)

# Display settings
FPS = 60
WIDTH, HEIGHT = info.current_w, info.current_h

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Pong")

# scores
opponent_score = 0
player_score = 0
# Game rectangles
ball = pygame.Rect(WIDTH/2 - 15, HEIGHT/2-15, 30, 30)
player = pygame.Rect(WIDTH -20, HEIGHT/2 - 70, 10, 140 )
opponent = pygame.Rect(10, HEIGHT/2 - 70 , 10, 140)
player_hitbox = player.inflate(50, 50)
opponent_hitbox = opponent.inflate(50 ,50)

run = True
while run:
    keys_pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()

    ball_speed = int(ball_speed_y) 
    SCREEN.fill(BG_COLOR)
    pygame.draw.rect(SCREEN, BLUE, player)
    pygame.draw.rect(SCREEN, RED, opponent)
    pygame.draw.ellipse(SCREEN, LIGHT_GREY, ball)
    pygame.draw.aaline(SCREEN, LIGHT_GREY, (WIDTH/2, 0),(WIDTH/2, HEIGHT))
    player_score_text = HEALTH_FONT.render("Score :"+ str(opponent_score), 1, RED)
    opponent_score_text = HEALTH_FONT.render("Score:" + str(player_score), 1, BLUE   )
    ball_speed_text = HEALTH_FONT.render("Ball Speed:" + str(ball_speed), 1, LIGHT_GREY   )
    SCREEN.blit(opponent_score_text, (WIDTH - opponent_score_text.get_width() - 10, 10))
    SCREEN.blit(player_score_text, (10, 10))
    SCREEN.blit(ball_speed_text, (WIDTH / 2 - ball_speed_text.get_width() / 2, 10))


    if keys_pressed[pygame.K_w] and opponent.top >= 0: # on a pressed move left
        opponent.y -= player_speed
        opponent_hitbox.y -= player_speed
    if keys_pressed[pygame.K_s] and opponent.bottom <= HEIGHT: # on a pressed move left
        opponent.y += player_speed
        opponent_hitbox.y += player_speed

    if keys_pressed[pygame.K_UP] and player.top >= 0: # on a pressed move left
        player.y -= player_speed
        player_hitbox.y -= player_speed
    if keys_pressed[pygame.K_DOWN] and player.bottom <= HEIGHT: # on a pressed move left
        player.y += player_speed
        player_hitbox.y += player_speed
    if keys_pressed[pygame.K_ESCAPE]:
        pygame.quit()

    # Ball Movement
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1
    if ball.left < 0 :
        player_score += 1
        ball.center = (WIDTH/2, HEIGHT/2)
        player_speed = 10
        ball_speed_x = 10
        ball_speed_y = 10
        ball_speed_y *= random.choice((1, -1))
        ball_speed_x *= random.choice((1, -1))

    if ball.right > WIDTH:
        opponent_score += 1
        ball.center = (WIDTH/2, HEIGHT/2)
        player_speed = 10
        ball_speed_x = 10
        ball_speed_y = 10
        ball_speed_y *= random.choice((1, -1))
        ball_speed_x *= random.choice((1, -1))

    if ball.colliderect(player_hitbox) or ball.colliderect(opponent_hitbox):
        HIT_SOUND.play()
        if ball_speed_x < 0:
            ball_speed_x -= 1
        else:
            ball_speed_x += 1
        if ball_speed_y < 0:
            ball_speed_y -= 1
        else:
            ball_speed_y += 1
        ball_speed_x *= -1
        player_speed += 0.5

    pygame.display.flip()
    clock.tick(FPS)
