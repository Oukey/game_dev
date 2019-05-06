# game_functions.py

import sys

import pygame

def check_keydown_events(event, ship):
    '''Реагирует на нажатие клавиш.'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
        
        
def check_keyup_events(event, ship):
    '''Реагирует на отпускание клавишь'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

        
def chec_events(ship):
    '''Обрабатывает нажатия клавишь и события мыши.'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settimgs, screen, ship):
    '''Обновяет изображения на экране и отображает новый экран.'''
    # При каждом проходе цикла перерисовывает экран.
    screen.fill(ai_settings.bg_color)
    ship.blitme()  # прорисовка корабля при исполнении основного цикла

    # Отображение последнего прорисованного экрана.
    pygame.display.flip()
