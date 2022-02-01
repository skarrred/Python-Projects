import winsound
import pygame
import colors
import os
pygame.font.init()
pygame.mixer.init()

# customize window
WIDTH, HEIGHT = 800, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Alien Wars")

# constant variables
FPS = 60
SPACESHIPS_WIDTH, SPACESHIPS_HEIGHT = 45, 40
VELOCITY = 4
MID_BORDER_WIDTH = 10
MID_BORDER_HEIGHT = HEIGHT
BULLET_VELOCITY = 7
MAX_BULLETS = 5
HEALTH_FONT = pygame.font.SysFont('comicsans', 70,)
WINNER_FONT = pygame.font.SysFont('Times New Roman', 90)

YELLOW_HEALTH_TEXT_POSITION = (  (100 +2), (190)  )
RED_HEALTH_TEXT_POSITION = (  (700 +5), (190)  )

MID_BORDER = pygame.Rect(WIDTH//2+MID_BORDER_WIDTH//2, 0, MID_BORDER_WIDTH, MID_BORDER_HEIGHT)

spaceship1_img = pygame.image.load(os.path.join('Assets', 'mainyellow.png'))
SPACESHIP1 = pygame.transform.rotate(pygame.transform.scale(spaceship1_img, (SPACESHIPS_WIDTH, SPACESHIPS_HEIGHT)), 270)

spaceship2_img = pygame.image.load(os.path.join('Assets', 'mainred.png'))
SPACESHIP2 = pygame.transform.rotate(pygame.transform.scale(spaceship2_img, (SPACESHIPS_WIDTH, SPACESHIPS_HEIGHT)), 90)

BACKG_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'space2.jpg')), (WIDTH, HEIGHT))

HIT_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'hit2.wav'))
HIT_SOUND.set_volume(0.5)
FIRE_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'pfire.wav'))
FIRE_SOUND.set_volume(0.5)
GAME_START_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'startsound.wav'))
GAME_START_SOUND.set_volume(1.0)
GAME_OVER_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'endsound.wav'))
GAME_OVER_SOUND.set_volume(0.5)

# custom events
YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

def yellow_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and ((yellow.x) - VELOCITY -5) > 0: # Yellow Left
        yellow.x -= VELOCITY
    if keys_pressed[pygame.K_d] and ((yellow.x + VELOCITY + SPACESHIPS_HEIGHT +5) < MID_BORDER.x): # Yellow Right
        yellow.x += VELOCITY
    if keys_pressed[pygame.K_w] and ((yellow.y -8) > 0): # Yellow Up
        yellow.y -= VELOCITY
    if keys_pressed[pygame.K_s] and ((yellow.y + SPACESHIPS_WIDTH +5) < HEIGHT): # Yellow Down
        yellow.y += VELOCITY

def red_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and ((red.x - VELOCITY -5) > MID_BORDER.x + MID_BORDER_WIDTH): # Red Left
        red.x -= VELOCITY
    if keys_pressed[pygame.K_RIGHT] and ((red.x - VELOCITY + SPACESHIPS_HEIGHT +15) < WIDTH): # Red Right
        red.x += VELOCITY
    if keys_pressed[pygame.K_UP] and ((red.y - VELOCITY -5) > 0): # Red Up
        red.y -= VELOCITY
    if keys_pressed[pygame.K_DOWN] and ((red.y +VELOCITY + SPACESHIPS_WIDTH +2) < HEIGHT): # Red Down
        red.y += VELOCITY

def draw_win(yellow, red, yellow_bullets, red_bullets, red_health_text, yellow_health_text):
    WIN.blit(BACKG_IMG, (0,0))
    pygame.draw.rect(WIN, colors.GREEN, MID_BORDER) # middle border
    WIN.blit(yellow_health_text, YELLOW_HEALTH_TEXT_POSITION) # yellow health
    WIN.blit(red_health_text, RED_HEALTH_TEXT_POSITION) # red health
    WIN.blit(SPACESHIP1, (yellow.x, yellow.y)) # spaceship1
    WIN.blit(SPACESHIP2, (red.x, red.y)) # spaceship2

    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, colors.YELLOW, bullet)

    for bullet in red_bullets:
        pygame.draw.rect(WIN, colors.RED, bullet)

    pygame.display.update()

def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VELOCITY # moves the bullet
        if red.colliderect(bullet): # check for collision with enemy
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x -= BULLET_VELOCITY # moves the bullet
        if yellow.colliderect(bullet): # check for collision with enemy
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)

def declare_winner(text):
    declare_text = WINNER_FONT.render(text, True, colors.MAGENTA, colors.YELLOW)
    WIN.blit(declare_text, (WIDTH/2 - declare_text.get_width()/2, HEIGHT/2 - declare_text.get_height()/2))
    pygame.display.update()
    # GAME_OVER_SOUND.play()
    pygame.time.delay(4000)

def main():
    GAME_START_SOUND.play()
    yellow = pygame.Rect(100, 210, SPACESHIPS_WIDTH, SPACESHIPS_HEIGHT) # create rectangle for spaceship1
    red = pygame.Rect(700, 210, SPACESHIPS_WIDTH, SPACESHIPS_HEIGHT) # create rectangle for spaceship2

    yellow_bullets = []
    red_bullets = []
    yellow_health = 5
    red_health = 5

    clock = pygame.time.Clock()
    running = True
    while running: # main loop
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # close button functionality
                running = False
                pygame.quit()

            # check if the player wants to shoot
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect((yellow.x + SPACESHIPS_HEIGHT), (yellow.y + SPACESHIPS_WIDTH//2), 14, 5)
                    yellow_bullets.append(bullet)
                    FIRE_SOUND.play()

                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect((red.x), (red.y + SPACESHIPS_WIDTH//2), 14, 5)
                    red_bullets.append(bullet)
                    FIRE_SOUND.play()

            # check if player is hit
            if event.type == RED_HIT:
                red_health -= 1
                HIT_SOUND.play()

            if event.type == YELLOW_HIT:
                yellow_health -= 1
                HIT_SOUND.play()


        red_health_text = HEALTH_FONT.render(str(red_health), True, colors.GRAY)
        yellow_health_text = HEALTH_FONT.render(str(yellow_health), True, colors.GRAY)

        # check and declare winner
        winner_text = ""
        if red_health <= 0:
            winner_text = "Yellow Won!"
        
        if yellow_health <= 0:
            winner_text = "Red Won!"

        if winner_text != "":
            GAME_OVER_SOUND.play()
            declare_winner(winner_text)
            break

        # spaceship movement functionality
        keys_pressed = pygame.key.get_pressed()
        yellow_movement(keys_pressed, yellow)
        red_movement(keys_pressed, red)
        
        handle_bullets(yellow_bullets, red_bullets, yellow, red)

        draw_win(yellow, red, yellow_bullets, red_bullets, red_health_text, yellow_health_text)


    main()

if __name__ == "__main__":
    main()