import pygame
import random

pygame.init()

width = 600
height = 600
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Flappy Bird")

white = 255,255,255
blue = 135,206,250
green = 0,255,0

font = pygame.font.SysFont(None,40)
big_font = pygame.font.SysFont(None,60)

#bird setting
bird_x = 100
bird_y = 300
bird_width = 60
bird_height = 45
bird_movement = 0
gravity = 0.4

bird_img = pygame.image.load("dude.png")
bird_img = pygame.transform.scale(bird_img,(bird_width,bird_height))

#pipe settings
pipe_width = 60
pipe_gap = 150
pipe_x = width
pipe_height = random.randint(100,400)

#score
score = 0

clock = pygame.time.Clock()
game_active = False
running = True
bg_img = pygame.image.load("bgg.png")  
bg_img = pygame.transform.scale(bg_img, (width, height)) 

def calculate_gravity(tick_speed):
    gravity = max(0,1.5 - tick_speed * 0.02)
    return gravity


while running:
    screen.blit(bg_img, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not game_active:
                    game_active = True
                    bird_y = 300
                    bird_movement = 0
                    pipe_x = width
                    score = 0
                    pipe_height = random.randint(100,400)
                bird_movement = -6
    if game_active:
        current_gravity = calculate_gravity(clock.get_fps() or 40)
        bird_movement += current_gravity
        bird_y += bird_movement
        #pipe movement
        pipe_x -= 5
        if pipe_x + pipe_width < 0:
            pipe_x = width
            pipe_height = random.randint(100,400)
            score += 2
        screen.blit(bird_img,(bird_x,bird_y))

        pygame.draw.rect(screen,green,(pipe_x,0,pipe_width,pipe_height))
        pygame.draw.rect(screen,green,(pipe_x,pipe_height+pipe_gap,pipe_width,height))
        #collision with top and bottom
        
        if bird_y < 0 or bird_y + bird_height > height:
            game_active = False
        
        if pipe_x < bird_x + bird_width and pipe_x + pipe_width > bird_x:
            if bird_y < pipe_height or bird_y + bird_height > pipe_height + pipe_gap:
                game_active = False

        #score display
        score_text = font.render(f"Score: {score}",True,white)
        screen.blit(score_text,(10,10))
    else:
        if score == 0:
            msg = "Press SPACE to start"
        else:
            msg = f"Game Over! Score: {score}"
        text = big_font.render(msg,True,white)
        screen.blit(text,(40,height//2 - 30))
    
    pygame.display.update()
    clock.tick(40)

pygame.quit()


        