# settirns.py

import pygame

class Settings():
    '''Класс для хранения всех настроек игры Alian Invasion'''

    def __init__(self):
        '''Инициализирует настройки игры'''
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (50, 140, 180)
        
        # настройки корабля
        self.ship_speed_factor = 1.5
        
        # Параметры пули
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3  # max количество пуль
