import pygame.image
from ctypes  import *


class Settings ():
    """Класс для хранения всех настроек игры Alien Invasion."""
    def __init__(self):
        """Инициализируем настройки игры."""

        self.bg_color = (0, 191, 255)

        # Настройки корабля
        self.ship_speed = 5
        self.ship_limit = 3
        # Параметры снаряда
        self.bullet_speed = 120
        self.bullet_allowed = 100

        # Настройки пришельцев
        self.alien_speed = 3.0
        self.fleet_drop_speed = 100
        # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = 1

        # размеры экрана
        self.screen_width = windll.user32.GetSystemMetrics(0)
        self.screen_heidht = windll.user32.GetSystemMetrics(1)