from pygame import *
from random import randint

dx=6
rand=randint(1,2)
dy=randint(1,3)
window = display.set_mode((800,600))
display.set_caption('ping pong')
background = transform.scale(image.load("background.png"),(800,600))
class GameSprite(sprite.Sprite):
    def __init__(self,player_image, player_x, player_y, player_speed,width,height):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(width,height))
        self.speed=player_speed
        self.rect=self.image.get_rect()
        self.rect.x=player_x
        self.rect.y=player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Wall(sprite.Sprite):
    def __init__(self,width,height,color_1,color_2,color_3,x_cor,y_cor):
        super().__init__()
        self.width=width
        self.height=height
        self.color1=color_1
        self.color2=color_2
        self.color3=color_3
        self.image=Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect=self.image.get_rect()
        self.rect.x=x_cor
        self.rect.y=y_cor
    def draw_wall(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
#class Area():
#   def __init__(self,x=0,y=0,width=10,height=10,color=None):
#       self.rect=get.rect(x,y,width,height)
#   def collidepoint(self,x,y):
#       return self.rect.collidepoint(x,y)
#   def colliderect(self,rect):
#       return self.rect.colliderect(rect)

ball=GameSprite('ball.png',400,300,dx,50,50)
player1=Wall(10,200,47,79,79,10,200)
player2=Wall(10,200,47,79,79,780,200)
clock = time.Clock()
FPS=60

game=True
while game:
    if rand == 1:
        ball.rect.x+=dx
    if rand == 2:
        ball.rect.x-=dx
    ball.rect.y+=dy
    window.blit(background,(0,0))
    ball.reset()
    player1.draw_wall()
    player2.draw_wall()
    keys_pressed = key.get_pressed()
    clock.tick(FPS)
    for e in event.get():
        if e.type == QUIT:
            game = False
    if sprite.collide_rect(ball,player1):
        ball.speed=randint(2,10)
        dx *= -1
        i=randint(1,2)
        if i == 1:
            dy*=-1
        else:
            dy=dy
    if sprite.collide_rect(ball,player2):
        ball.speed=randint(2,10)
        dx *= -1
        i=randint(1,2)
        if i == 1:
            dy*=-1
        else:
            dy=dy
    if keys_pressed[K_w]:
        player1.rect.y-=10
    if keys_pressed[K_s]:
        player1.rect.y+=10
    if keys_pressed[K_DOWN]:
        player2.rect.y+=10
    if keys_pressed[K_UP]:
        player2.rect.y-=10
    if player1.rect.y>=0:
        player1.rect.y-=10
    if player1.rect.y<=400:
        player1.rect.y+=10
    if player2.rect.y>=0:
        player2.rect.y-=10
    if player2.rect.y<=400:
        player2.rect.y+=10
    if ball.rect.y>=0:
        dy*=-1
    if ball.rect.y<=550:
        dy*=-1
    if ball.rect.x<=0:
        game=False
    if ball.rect.x>=750:
        game=False
    display.update()