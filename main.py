import pygame
import random

pygame.init()

white=(255,255,255)
black=(0,0,0)
green=(0,255,0)
red=(255,0,0)
orange=(255,160,0)
yellow=(255,255,0)
width= 450
height= 300

score=0
player_x= 50
player_y= 200
y_change=0
gravity=1
x_change=0
obstacles=[300,450,600]
obstacles_speed=2
active=False


screen=pygame.display.set_mode([width,height])
pygame.display.set_caption('Saifs Adventure')
background= black
#background=pygame.image.load('background_game.png')
#background = pygame.transform.scale(background,(width,height))
fps= 60
font=pygame.font.Font('freesansbold.ttf',16)
timer=pygame.time.Clock()

running=True
while running:
    timer.tick(fps)
    screen.fill(background)
    score_text=font.render(f'Score: {score}',True,white,black)
    screen.blit(score_text,(160,250))
    '''
    screen.fill(0,0,0)
    screen.blit(background,(0,0))
    '''
    floor=pygame.draw.rect(screen,white,[0,220,width,5])
    player=pygame.draw.rect(screen,green,[player_x,player_y,20,20])
    obstacles0=pygame.draw.rect(screen,red,[obstacles[0],200,20,20])
    obstacles1 = pygame.draw.rect(screen, orange, [obstacles[1], 200, 20, 20])
    obstacles2 = pygame.draw.rect(screen, yellow, [obstacles[2], 200, 20, 20])

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN and not active:
            if event.key == pygame.K_SPACE:
                obstacles = [300, 450, 600]
                player_x=50
                score=0
                active = True
        if event.type==pygame.KEYDOWN and active:
            if event.key == pygame.K_SPACE and y_change==0:
                y_change=18
            if event.key== pygame.K_RIGHT:
                x_change=2
            if event.key== pygame.K_LEFT:
                x_change=-2
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_RIGHT:
                x_change=0
            if event.key==pygame.K_LEFT:
                x_change=0
    for i in range(len(obstacles)):
        if active:
            obstacles[i]-=obstacles_speed
            if obstacles[i]<-20:
                obstacles[i]=random.randint(470,570)
                score+=1
            if player.colliderect(obstacles0) or player.colliderect(obstacles1) or player.colliderect(obstacles2):
                active=False
    if 0<=player_x<=430:
        player_x+=x_change
    if player_x<0:
        player_x=0
    if player_x>430:
        player_x=430
    if y_change>0 or player_y<200:
        player_y-=y_change
        y_change-=gravity
    if player_y>200:
        player_y=200
    if player_y==200 and y_change <0:
        y_change=0

    pygame.display.flip()
pygame.quit()
