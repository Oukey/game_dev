# alean_invasion.py

import sys

import pygame


def run_game():
    # Инициализирует игру и создает объект экрана.
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))

    # запуск основного цикла
    while True:
        # Отслеживание событий клавиатуры мыши.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # Отображение последнего прорисованного экрана.
        pygame.display.flip()


run_game()
