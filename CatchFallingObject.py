import pygame
import random

pygame.init()

#screen dimensions

WIDTH = 600
HEIGHT = 400


#Colors
WHITE = (255,255,255)
YELLOW = (255,255,0)
RED = (255,0,0)
BLACK = (0,0,0)

#create screen
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Catch the falling object")

clock = pygame.time.Clock()

player_width = 100
player_height = 20
player_x = (WIDTH - player_width) // 2
player_y = HEIGHT-player_height - 10

object_width = 60
object_height = 60
object_x = random.randint(0,WIDTH-object_width)
object_Y = -object_height
object_speed = 5

object_img = pygame.image.load('space.png')
object_img = pygame.transform.scale(object_img,(object_width,object_height))

score = 0
missed = 0
max_missed = 5

font = pygame.font.SysFont(None,36)

#Game loop
running = True
game_over = False

bg_img = pygame.image.load("bg3.jpg")
bg_img = pygame.transform.scale(bg_img,(WIDTH,HEIGHT))

