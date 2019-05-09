# alean_invasion.py

import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    pygame.display.set_caption("Alian_Invasion")
    
    # Создание ключевых объектов
    # Инициализирует игру и создает объект экрана
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

    # Создание корабля, группы пуль и группы пришельцев
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    
    # Создание флота пришельцев
    gf.create_fleet(ai_settings, screen, aliens)

    # запуск основного цикла
    while True:
        # Отслеживание событий клавиатуры мыши.
        gf.chec_events(ai_settings, screen, ship, bullets)  # Цикл событий из модуля game_functions.py
        ship.update()  # обновление позиции корабля
        gf.update_bullets(bullets)  # обновление позиций выпущенных пуль
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()  # запуск игрового цикла
