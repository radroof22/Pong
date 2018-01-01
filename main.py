import pygame, time, sys
from pygame.locals import *

#Backend Setup
pygame.init()
WIN_WIDTH = 800
display_height = 600
display_width = 800
WIN_LENGTH = 600
gameDisplay = pygame.display.set_mode((WIN_WIDTH,WIN_LENGTH))
clock = pygame.time.Clock()

#colors
black = (0, 0, 0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
orange = (255,128,0)
pink = (255,51,153)
aqua = (0,255,255)
yellow = (255,255,0)
bright_yellow = (200,200,0)
bright_green = (0,200,0)
bright_blue = (0,0,200)

#TECHNICALS
X= 30
Y = 100
cir = [400,300]
traj = [1,0]
score = 0

def text_objects(text, font):
	textSurface = font.render(text, True, pink)
	return textSurface, textSurface.get_rect()

def message_display(text):
	largeText = pygame.font.SysFont("comicsansms", 115)
	TextSurf, TextRect = text_objects(text, largeText)
	TextRect.center = ((WIN_WIDTH / 2),(WIN_HEIGHT / 2) )
	gameDisplay.blit(TextSurf, TextRect)                                           
	
	pygame.display.update()

def game():
	global cir
	global traj
	global Y
	global X
	global score
	native = None
	
	while True:
		
		#Events
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit
				quit()
			if click[0] == 0:
				Y = mouse[1]

		#top side
		if cir[1]-4 <= 0:
			if native is 'right':
				traj = [-1,1]
				native = 'top'
			if native == 'paddle':
				traj = [1,1]
				native = 'top'
			else:
				traj = [-1,1]
				native = 'top'
			
		#right side
		elif cir[0] >= WIN_WIDTH:
			if native == 'top':
				traj = [1,-1]
				native = 'right'
			else:
				traj = [-1,-1]
				native = 'right'
				
		#bottom side
		elif cir[1] >= WIN_LENGTH:
			if native == 'right':
				traj = [-1,-1]
				native = 'down'
			if native == 'paddle':
				traj = [1,-1]
			if native == 'top':
				traj = [-1,-1]
				native = 'down'
			
		#paddle hit
		elif cir[1] < Y + 90 and cir[1] + 8 > Y and cir[0] < X + 10 and cir[0] + 8 > X:
			if Y < cir[1] and Y + 45 > cir[1]:
				traj = [1,-1]
				native = 'paddle'
			else:
				traj = [1, 1]
				native = 'paddle'
			score = int(score) + 1
			
		elif cir[0]+8 < 0:
			time.sleep(1)
			cir = [400,300]
			score = 0
		else: 
			pass
			
		#Movement	
		cir[0] = int(cir[0] + traj[0])
		cir[1] = int(cir[1] + traj[1])
		
		
		#Drawing
		gameDisplay.fill(black)
		pygame.draw.line(gameDisplay, white, (400,0), (400, WIN_LENGTH), 5)

		pygame.draw.rect(gameDisplay, white, (X,Y,10,90))
		pygame.draw.circle(gameDisplay, white, (cir[0],cir[1]), 8)

		#Draw Score
		largeText = pygame.font.SysFont("comicsansms", 80)
		TextSurf, TextRect = text_objects(str(score), largeText)
		TextRect.center = (150,(display_height / 2) - 50 )
		gameDisplay.blit(TextSurf, TextRect)
			
		pygame.display.update()
		
game()



