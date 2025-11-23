import random
import sys
import pygame
from pygame.locals import *

FPS=32
SCREENWIDTH=600
SCREENHEIGHT=340
SCREEN=pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
GROUNDY=SCREENHEIGHT*0.8
GAME_IMAGE={}
GAME_SOUND={}

# SPIDER= "C:/Users/Vedant/PycharmProjects/PythonProject70/media/images/spider.png"
BACKGROUND="C:/Users/Vedant/PycharmProjects/PythonProject70/media/images/city.jpg"
ENEMY="C:/Users/Vedant/PycharmProjects/PythonProject70/media/images/enemy.png"
SOUND="C:/Users/Vedant/PycharmProjects/PythonProject70/media/sound/bg_sound.MP3"

spider = pygame.image.load("C:/Users/Vedant/PycharmProjects/PythonProject70/media/images/spider.png")
resized_image = pygame.transform.scale(spider, (100, 150))

# def main_game():
#     # your main game loop here
#     while True:
#         for event in pygame.event.get():
#             if event.type == QUIT:
#                 pygame.quit()
#                 sys.exit()
#         # update game, draw, etc.
#         pygame.display.update()
#         FPSCLOCK.tick(FPS)

def welcome_screen():
    plx = int(SCREENWIDTH / -20)
    ply = int((SCREENHEIGHT - GAME_IMAGE['spider'].get_height()) / 2)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
                pygame.quit()
                sys.exit()

            elif event.type==KEYDOWN and (event.key==K_SPACE or event.key==K_UP or event.key == K_DOWN):
                sys.exit()
            else:
                SCREEN.blit(GAME_IMAGE['background'],(0,0))
                SCREEN.blit(GAME_IMAGE['spider'], (plx, ply))
                pygame.display.update()
                FPSCLOCK.tick(FPS)


if __name__ == '__main__':
    pygame.init()
    FPSCLOCK=pygame.time.Clock()
    pygame.display.set_caption("FlySpidey")
    GAME_IMAGE['message']=pygame.image.load(BACKGROUND).convert_alpha()
    GAME_SOUND['die']=pygame.mixer.Sound(SOUND)
    GAME_IMAGE['background'] = pygame.image.load(BACKGROUND).convert()
    GAME_IMAGE['enemy']=pygame.image.load(ENEMY).convert_alpha()
    GAME_IMAGE['spider'] =resized_image.convert_alpha()

    while True:
        welcome_screen()