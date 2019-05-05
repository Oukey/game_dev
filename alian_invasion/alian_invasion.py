# alean_invasion.py

import pygame

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    pygame.display.set_caption("Alian_Invasion")
    # Назначение цвета фона.
    # bg_color = (230, 230, 230)

    # Инициализирует игру и создает объект экрана.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

    # Создание корабля
    ship = Ship(screen)

    # запуск основного цикла
    while True:
        # Отслеживание событий клавиатуры мыши.
        gf.chec_events()  # Цикл событий из модуля game_functions.py


        # При каждом проходе цикла перерисовывается экран.
        screen.fill(ai_settings.bg_color)
        ship.blitme()  # прорисовка корабля при исполнении основного цикла
        # Отображение последнего прорисованного экрана.
        pygame.display.flip()


run_game()
