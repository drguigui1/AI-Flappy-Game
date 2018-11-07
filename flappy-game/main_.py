"""
Copyright :
 - Cesar Belley
 - Pierre Guillaume
"""

import pygame
from random import randint, uniform
import bird

white = (255, 255, 255)
green = (0, 255, 0)

size = 500, 766 
pygame.init()

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Flappy Bird")

nb_birds = 30
birds = []

for i in range(nb_birds):
	birds.append(bird.Bird(size[0] // 2 - 100, 250))

for i in range(nb_birds):
    birds[i].y += (size[1] / nb_birds) * i - 400

done = False # Player playing ?
clock = pygame.time.Clock()

### Pictures load
background = pygame.image.load("images/background_.png").convert_alpha()
background = pygame.transform.scale(background, (500, 766))

pipe_down = pygame.image.load("images/pipe.png").convert_alpha()
#pipe_down = pygame.transform.scale(pipe_down, (50,500))

pipe_up = pygame.transform.rotate(pipe_down, 180)
###

font = pygame.font.Font("font/ARCADE_N.TTF", 50)

def obstacles(xloc, ysize, space):
	"""
	Draw an obstacle
	"""
	screen.blit(pipe_up, (xloc, ysize - pipe_up.get_height()))
	screen.blit(pipe_down, (xloc, ysize + space))

def Score(score):
	"""
	Print the score
	"""
	text = font.render("Score : " + str(score), True, (50, 70, 150))
	screen.blit(text, ((size[0] - text.get_width()) // 2, 15))

#check if they are all dead
def dead_check():
    i = 0
    oneAlive = False
    while not oneAlive and i < len(birds):
        if birds[i].alive:
            oneAlive = True
        i += 1
    return i == len(birds)

def regenerate(birds):
    for i in range(0, len(birds) - 5):
        birds[i].copy_brain_with_mutation(birds[len(birds) - 1 - (i % 5)].brain)


ground = size[1] - 100

xloc = 700
ysize = randint(0, 350)
space = randint(180, 250)

obspeed = 2.5

background_x = 0

all_dead = False

nb_generations = 1000

for i in range(nb_generations):
    while not all_dead:

        screen.fill(white) # Background Color
        screen.blit(background, (-background_x, 0))
        screen.blit(background, (size[0] - background_x, 0))

        for event in pygame.event.get(): # For each event
            if event.type == pygame.QUIT:
                done = True
        
        if done:
            break

        ### Items drawings
        obstacles(xloc, ysize, space)
        for b in birds:
            screen.blit(b.skins[int(((90+b.y_speed*3)/180)*b.resolution)], (b.x, b.y))
        ###

        ### check if they are all dead
        all_dead = dead_check()
        ###

        ### Items movement
        for b in birds:
            b.move(xloc, ysize + space // 2)

        xloc -= obspeed # Obstacles
        ###

        if xloc < -90: # New obstacle
            xloc = 700
            space = randint(180, 250)
            ysize = randint(0, size[1] - space)

        ### Hit box check
        for b in birds:
            b.check_alive(ground, xloc, ysize, space)
        ###
        
        pygame.display.flip()
        clock.tick(60)
        background_x += 0.25
        background_x %= size[0]

    if done:
        break
    
    all_dead = False
    birds.sort(key = lambda bird : bird.score)
    for i in birds:
        print(i.score)
    regenerate(birds)
    for i in range(len(birds)):
        birds[i].y = (size[1] / nb_birds) * i -150
        birds[i].x = size[0] // 2 - 100
        birds[i].alive = True
        birds[i].y_speed = 0
        birds[i].score = 0
        birds[i].nb_jumps = 0

    xloc = 700
    ysize = randint(0, 300)
    space = randint(180, 250)

pygame.quit()

