import random
import sys
import pygame


WIDTH=736
HEIGHT=414

pygame.init()
window=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("FlySpidey")
clock=pygame.time.Clock()

# spidey
spider_x=0
spider_y=100
spider_width=100
spider_height=150

# enemy
enemy1_width=60
enemy1_height=100
enemy_x=WIDTH
enemy_y=0

# SPIDER= "C:/Users/Vedant/PycharmProjects/PythonProject70/media/images/spider.png"
BACKGROUND="C:/Users/Vedant/PycharmProjects/PythonProject70/media/images/bg_city.jpg"
# ENEMY="C:/Users/Vedant/PycharmProjects/PythonProject70/media/images/enemy.png"
SOUND="C:/Users/Vedant/PycharmProjects/PythonProject70/media/sound/bg_sound.MP3"
GO_SOUND="C:/Users/Vedant/PycharmProjects/PythonProject70/media/sound/game_over.MP3"

spider = pygame.image.load("C:/Users/Vedant/PycharmProjects/PythonProject70/media/images/spider.png")
resized_image = pygame.transform.scale(spider, (spider_width, spider_height))

enemy=pygame.image.load("C:/Users/Vedant/PycharmProjects/PythonProject70/media/images/enemy.png")
resized_enemy = pygame.transform.scale(enemy, (enemy1_width, enemy1_height))


backgroundImage=pygame.image.load(BACKGROUND)

enemies=[]

velocity_x=-2
velocity_y=0

def move():
    spidey.y=velocity_y
    for enemy_2 in enemies:
        enemy_2.x+=velocity_x

    while len(enemies) > 0 and enemies[0].x < enemy1_width:
        enemies.pop(0)
# for spider
class Spider(pygame.Rect):
    def __init__(self,img):
        pygame.Rect.__init__(self,spider_x,spider_y,spider_width,spider_height)
        self.img=img

spidey=Spider(resized_image)

# for enemy
class Enemy(pygame.Rect):
    def __init__(self, img):
        pygame.Rect.__init__(self, enemy_x, enemy_y, enemy1_width, enemy1_height)
        self.img = img
        self.passed = False

def create_enemies():
    rand_y=random.randint(5,300)

    enemy_1=Enemy(resized_enemy)
    enemy_1.y = rand_y
    enemies.append(enemy_1)

    print(len(enemies))

create_enemies_timer=pygame.USEREVENT+0
pygame.time.set_timer(create_enemies_timer,1500)

def draw():
    window.blit(backgroundImage,(0,0))
    window.blit(spidey.img,spidey)

    for enemy_draw in enemies:
        window.blit(enemy_draw.img,enemy_draw)


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type==create_enemies_timer:
            create_enemies()

        if event.type==pygame.KEYDOWN:


    move()
    draw()
    pygame.display.update()
    clock.tick(60)