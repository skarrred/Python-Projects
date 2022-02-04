import pygame
from main import HEIGHT, WIDTH
import os

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