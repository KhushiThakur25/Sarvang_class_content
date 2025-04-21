import pygame

import sys

#initialize pygame

pygame.init()

#set up display
width, height = 600,400

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("This is our first pygame window.")

#set up color
#rgb = red,green,blue...

blue = (0,0,255)
white = (255,255,255)
red  = (255,0,0)


#game loop
running = True

while running:
    screen.fill(red)
    pygame.draw.circle(screen,blue,(300,200),50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

pygame.quit()
sys.exit()
    