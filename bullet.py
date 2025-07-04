import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Класс для управления снарядами, выпущенными кораблем."""
    def __init__(self, ai_game):
        """Создает объект снарядов в текущей позиции корабля."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings


        # Создание снаряда в позиции (0,0) и назначение правильной позиции.
        self.image = pygame.image.load('file_game/PNG/Lasers/laserRed05.png')
        self.rect = self.image.get_rect()
        self.rect.midtop = ai_game.ship.rect.midtop

        # Позиция снаряда хранится в вещественном формате.
        self.y = float(self.rect.y)

    def update(self):
        """Перемещает снаряд вверх по экрану."""
        # Обновление позиции снаряда в вещественном формате.
        self.y -= self.settings.bullet_speed
        # Обновление позиции прямоугольник
        self.rect.y = self.y

    def draw_bullet(self):
        """Вывод снаряда на экран."""
        self.screen.blit(self.image, self.rect)