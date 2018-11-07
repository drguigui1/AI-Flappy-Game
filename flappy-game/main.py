"""
Copyright :
 - Cesar Belley
 - Pierre Guillaume
"""

import pygame
from random import randint
white = (255, 255, 255)
green = (0, 255, 0)


pygame.init()

size = 500, 766 

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Flappy Bird")

done = False # Player playing ?
clock = pygame.time.Clock()

### Pictures load
background = pygame.image.load("images/background_.png").convert_alpha()
background = pygame.transform.scale(background, (500, 766))

bird_ = pygame.image.load("images/bird.png")

pipe_down = pygame.image.load("images/pipe.png").convert_alpha()
#pipe_down = pygame.transform.scale(pipe_down, (50,500))

pipe_up = pygame.transform.rotate(pipe_down, 180)
###

font = pygame.font.Font("font/ARCADE_N.TTF", 50)

def bird(x, y, y_speed):
	"""
	Paste Bird at (x, y)
	"""
	screen.blit(pygame.transform.rotate(bird_, -y_speed * 3), (x, y))

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

x = size[0] // 2 - 100
y = 250
y_speed = 0
score = 0

ground = size[1] - 100

xloc = 700
ysize = randint(0, 350)
space = randint(180, 250)

obspeed = 2.5

background_x = 0

while not done:
	
	screen.fill(white) # Background Color
	screen.blit(background, (-background_x, 0))
	screen.blit(background, (size[0] - background_x, 0))

	for event in pygame.event.get(): # For each event
		if event.type == pygame.QUIT:
			done = True

		if event.type == pygame.KEYDOWN: 
			if event.key == pygame.K_SPACE:
				y_speed = -6.5 # Bird flying high

	### Items drawings
	obstacles(xloc, ysize, space)
	bird(x, y, y_speed)
	Score(score)
	###

	### Items movement
	y += y_speed # Bird
	xloc -= obspeed # Obstacles
	###

	if xloc < -90: # New obstacle
		xloc = 700
		space = randint(180, 250)
		ysize = randint(0, size[1] - space)

	### Hit box check
	if y >= ground: #
		done = True
		y_speed, obspeed = 0, 0

	if xloc + 130 >= x + 65 >= xloc:
		if y + 5 < ysize or y + 50 > ysize + space:
			done = True
			y_speed, obspeed = 0, 0
	###

	if x > xloc and x < xloc + 3:
		# Score info
		score += 1

	pygame.display.flip()
	clock.tick(60)
	background_x += 0.25
	background_x %= size[0]

	# Gravity
	y_speed += 0.2

pygame.quit()
