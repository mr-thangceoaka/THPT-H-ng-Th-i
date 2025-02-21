import pygame
from random import randint

pygame.init()
score=0
font=pygame.font.SysFont('sans ',20)
widh=400
high=600
screen=pygame.display.set_mode((widh,high)) 
pygame.display.set_caption('Flapy bird')
running = True
green=(0,200,0)
blue=(0,0,225)
clock=pygame.time.Clock()
tube_wihd=50
red=(255,0,0)
black=(0,0,0)

tube1x=300
tube2x=tube1x+200
tube3x=tube2x+200

tube1_high=randint(100,400)
tube2_high=randint(100,400)
tube3_high=randint(100,400)
tube1_pass=False
tube2_pass=False
tube3_pass=False

BIRD_X=50
BIRD_WIDH=30
BIRD_HIGH=30
bird_y=400
birddropvelocity=0
garavity=0.5


pause=False
tubegap=150
tubevelocity=3

backgroud_image=pygame.image.load("C:\\Users\\MSI-PC\\Downloads\\python\\demon\\bkgr.png")
bird_image=pygame.image.load(r'C:\Users\MSI-PC\Downloads\python\demon\Screenshot 2025-02-21 222250.png')
bird_image=pygame.transform.scale(bird_image,(BIRD_WIDH,BIRD_HIGH))
while running:
    clock.tick(60)
    screen.fill(green)
    screen.blit(backgroud_image,(0,0))
  #draw tube
    tube1_rect=pygame.draw.rect(screen,blue,(tube1x,0,tube_wihd,tube1_high))
    tube2_rect=pygame.draw.rect(screen,blue,(tube2x,0,tube_wihd,tube2_high))
    tube3_rect=pygame.draw.rect(screen,blue,(tube3x,0,tube_wihd,tube3_high))
    
    tube_1_inv=pygame.draw.rect(screen,blue,(tube1x,tube1_high+tubegap,tube_wihd,high-tube1_high-tubegap))
    tube_2_inv=pygame.draw.rect(screen,blue,(tube2x,tube2_high+tubegap,tube_wihd,high-tube2_high-tubegap))
    tube_3_inv=pygame.draw.rect(screen,blue,(tube3x,tube3_high+tubegap,tube_wihd,high-tube3_high-tubegap))
   #draw bird
    bird_rect=screen.blit(bird_image,(BIRD_X,bird_y))
#bird fall
    bird_y+=birddropvelocity
    birddropvelocity+=garavity
    
    tube1x=tube1x-tubevelocity
    tube2x=tube2x-tubevelocity
    tube3x=tube3x-tubevelocity
    if tube1x < -tube_wihd:
        tube1x=550
        tube1_high=randint(100,400)
        tube1_pass=False
    if tube2x <-tube_wihd:
        tube2x=550
        tube2_high=randint(100,400)
        tube2_pass=False
    if tube3x <-tube_wihd:
         tube3x=550    
         tube3_high=randint(100,400)
         tube3_pass=False
     #update score
    if tube1x+50<=BIRD_X and tube1_pass==False:
        score+=1
        tube1_pass=True
    if tube3x+50<=BIRD_X and tube3_pass==False:
        score+=1
        tube3_pass=True
    if tube2x+50<=BIRD_X and tube2_pass==False:
        score+=1
        tube2_pass=True
    score_txt=font.render("score"+str(score),True,black)
    screen.blit(score_txt,(5,5))
    
     #check collive
    for tube in [tube1_rect,tube2_rect,tube3_rect,tube_1_inv,tube_2_inv,tube_3_inv]:
         if bird_rect.colliderect(tube) or bird_y>=600:
             tubevelocity=0
             birddropvelocity=0
             gameover=font.render("game over, score"+str(score),True,black)
             coutinue=font.render("press space to cotinue",True,black)
             screen.blit(coutinue,(200,450))
             screen.blit(gameover,(200,300))
             pause=True
             
         
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                if pause:
                    bird_y=400
                    tubevelocity=3
                    tube1x=300
                    tube2x=tube1x+150
                    tube3x=tube2x+150
                    score=0
                    pause=False
                birddropvelocity=0
                birddropvelocity -= 10
                
    pygame.display.flip()        
