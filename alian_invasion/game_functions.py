# game_functions.py

import sys

import pygame


def chec_events():
    '''Обрабатывает нажатия клавишь и события мыши.'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(ai_settimgs, screen, ship):
    '''Обновяет изображения на экране и отображает новый экран.'''
    # При каждом проходе цикла перерисовывает экран.
    screen.fill(ai_settings.bg_color)
    ship.blitme()  # прорисовка корабля при исполнении основного цикла

    # Отображение последнего прорисованного экрана.
    pygame.display.flip()
