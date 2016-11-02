import sys, pygame
pygame.init()
pygame.display.set_caption('Privacy Con')

size = width, height = 640, 480
black = 0, 0, 0
screen = pygame.display.set_mode(size)

images = []
for x in range(1, 10):
	images.append(pygame.image.load(str(x) + ".png"))
frame = 0
current = 0
chose = False
yes = False
no = False

def render():
	screen.fill(black)
	if current < 9:
		screen.blit(images[current], (0, 0))
	else:
		if chose == False:
			screen.blit(pygame.image.load("10.png"), (0, 0))
			screen.blit(pygame.image.load("yes.png"), (20, 215))
			screen.blit(pygame.image.load("no.png"), (520, 215))
		if yes == True:
			screen.blit(pygame.image.load("11.png"), (0, 0))
		if no == True:
			screen.blit(pygame.image.load("12.png"), (0, 0))
	pygame.display.flip()

def getCollision(x, y, w, h):
	return (pygame.mouse.get_pos()[0] > x and pygame.mouse.get_pos()[0] < x + w and pygame.mouse.get_pos()[1] > y and pygame.mouse.get_pos()[1] < y + h)

def update():
	print current
	global frame
	global current
	frame += 1
	if(frame % 1000 == 0 and current < 10):
		current += 1
	elif(frame % 1000 == 0 and current == 8):
		current += 1
	if(current == 9):
		current += 1
		chose = True
		if pygame.mouse.get_pressed[0] == True:
			if getCollision(20, 215, 100, 50):
				yes = True
			elif getCollision(520, 215, 100, 50):
				no = True

while 1:
	render()
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				print "hey"
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_SPACE:
				print "hey"
	update()