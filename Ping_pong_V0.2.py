#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is a two player ping pong game 
#By S Giridharan 
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
import pygame,sys,random
pygame.init()
#Display
WIDTH,HEIGHT=855,600
display=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Ping Pong")
font=pygame.font.SysFont("Arial",40,bold=True)

#balls
ball_pos=pygame.math.Vector2(427,300) #it can also be a list that has the number 440 and 250 
ball=pygame.Rect((ball_pos.x,ball_pos.y,50,50)) #x,y,width,height
ball_velocity=pygame.math.Vector2(2,2) #it can also be a list (dx,dy)

#paddles
paddle1_pos=pygame.math.Vector2(5,0)#it can also be a list
paddle2_pos=pygame.math.Vector2(800,0)#it can also be a list
paddle1=pygame.Rect(paddle1_pos.x,paddle1_pos.y,50,100)
paddle2=pygame.Rect(paddle2_pos.x,paddle2_pos.y,50,100)
paddle_vel=pygame.math.Vector2(4,-4)

#player points
score1=0
score2=0

clock=pygame.time.Clock()
def score_system():
    global score1,score2

    if ball.left < 0:
        score1=score1+1
        ball_respawn()
    if ball.right > 857:
        score2=score2+1
        ball_respawn()
    #print(score2,score1)

def ball_respawn():
    pygame.time.delay(500)
    ball.x=WIDTH//2
    ball.y=HEIGHT//2
    ball_velocity.x=random.choice([-2,2])
    ball_velocity.y=random.choice([-2,2])

def draw_text(texts,x,y,color=(225,225,225)):
    lines=texts.split("\n")
    for i,text in enumerate(lines):
        text_surface=font.render(text,True,color) #render text 
        display.blit(text_surface,(x,y+i*40)) #draw the font on the surface

"""def collision(ball_x,ball_y,paddle,ball_width):
    paddle_center_x=paddle.x + paddle.width/2
    paddle_center_y=paddle.y + paddle.height/2
    distance = math.sqrt((ball_x-paddle_center_x)**2 + (ball_y-paddle_center_y)**2)
    if distance <= (ball_width/2) + paddle.width/2:
        return True #collision is detected 

def collision(paddle):
    clostestX=max(paddle.left,min(ball.x,paddle.x+ball.width))
    clostestY=max(paddle.top,min(ball.y,paddle.y+ball.height))
    distance=math.sqrt((ball.x-clostestX)**2 + (ball.y-clostestY)**2)
    if distance <= ball.width:
        return True """

def Main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        display.fill((0,0,0))  
        #Ball movement
        ball.x+=ball_velocity.x
        ball.y-=ball_velocity.y
        #Balls collision 
        if ball.colliderect(paddle2) or ball.colliderect(paddle1):
            ball_velocity.x*=-1
            score_system()
        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_velocity.y*=-1 

        score_system()

        #player movement
        keys = pygame.key.get_pressed()#gets the current key pressed instant
        #player1 movement
        if keys[pygame.K_w] and paddle1.top > 0:
            paddle1.y-=paddle_vel.x
        if keys[pygame.K_s] and paddle1.bottom < 600:
            paddle1.y+=paddle_vel.x
        #player2 movement
        if keys[pygame.K_UP] and paddle2.top > 0:
            #print("a")
            paddle2.y-=paddle_vel.x
        if keys[pygame.K_DOWN] and paddle2.bottom < 600:
            paddle2.y+=paddle_vel.x

        draw_text(f"Score\nPlayer1:{score1}\nplayer2:{score2}",100,20,(225,225,225))
        pygame.draw.ellipse(display,pygame.Color("red"),ball)
        pygame.draw.rect(display,pygame.Color("yellow"),paddle1)
        pygame.draw.rect(display,pygame.Color("blue"),paddle2)
        pygame.display.update()
        clock.tick(45)
            
if __name__ == "__main__":
    Main()