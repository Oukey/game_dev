# ship.py

import pygame


class Ship():

    def __init__(self, ai_settings, screen):
        '''Инициализирует корабль и задает его начаьную позицию'''
        self.screen = screen
        self.ai_settings = ai_settings

        # Загрузка изображения корабля и получение прямоугольника.
        self.image = pygame.image.load('images/ship_0.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Каждый повый корабль появляется у нижнего края экрана.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # Сохранение вещественной координаты центра коробля
        self.center = float(self.rect.centerx)
        
        # Флаги перемещения
        self.moving_right = False  # перемещение вправо
        self.moving_left = False  # перемещение влево
        
    def update(self):
        '''Обновляет позицию коробля с учетом флагов.'''
        # Обновляется атрибут center, не rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        # Обновление атритуба rect на основании self.center.
        self.rect.centerx = self.center        

    def blitme(self):
        '''Рисует корабль в текущей позиции.'''
        self.screen.blit(self.image, self.rect)
