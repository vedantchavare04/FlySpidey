from code import Quitter

import pygame


def welcome_screen(screenwidth, screenheight, game_image):
    plx=int(screenwidth/5)
    ply=int((screenheight-game_image['player'].get_height())/2)

    while True:
        for event in pygame.event.get():
            if event.type==Quit or
