# alien_invasion.py

import pygame
from pygame.sprite import Group

from settings import Settings
from scoreboard import Scoreboard
from game_stats import GameStats
from button import Button
from ship import Ship
import game_functions as gf


def run_game():
    pygame.display.set_caption("Alian_Invasion")

    # Создание ключевых объектов
    # Инициализирует игру и создает объект экрана
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

    # Создание кнопки Play
    play_button = Button(ai_settings, screen, 'Play')

    # Создание корабля, группы пуль и группы пришельцев
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # Создание флота пришельцев
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Создание экземпляра для хранения игровой статистики
    stats = GameStats(ai_settings)

    # Создание экземпляров GameStats и Scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # запуск основного цикла
    while True:
        # Отслеживание событий клавиатуры мыши
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        # if stats.game_active:
        ship.update()  # обновление позиции корабля
        gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)  # обновление позиций выпущенных пуль
        gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)  # обновление экрана


run_game()  # запуск игрового цикла
