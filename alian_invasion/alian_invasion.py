# alean_invasion.py

import pygame

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    pygame.display.set_caption("Alian_Invasion")

    # Инициализирует игру и создает объект экрана.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

    # Создание корабля
    ship = Ship(ai_settings, screen)

    # запуск основного цикла
    while True:
        # Отслеживание событий клавиатуры мыши.
        gf.chec_events(ship)  # Цикл событий из модуля game_functions.py
        ship.update()
        gf.update_screen(ai_settings, screen, ship)


run_game()
