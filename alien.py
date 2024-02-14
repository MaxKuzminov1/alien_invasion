import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Класс, представляющий одного пришельца."""

    def __init__(self, ai_game):
        """"Инициализирует пришельца и задает его начальную позицию."""

        self.screen = ai_game.screen
        self.setting = ai_game.settings
        pygame.sprite.Sprite.__init__(self)

        # Загрузка изображения пришельца и назначение атрибута rect
        self.image = pygame.image.load('file_game/PNG/Enemies/enemyBlack1.png')
        self.rect = self.image.get_rect()

        # Каждый новый пришелец появляется в левом верхнем углу экрана.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Сохранение точной горизонтальной позиции пришельца.
        self.x = float(self.rect.x)

    def update(self):
        """Перемещает пришельца вправо и влево."""
        self.x += (self.setting.alien_speed * self.setting.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """Возвращает True, если пришелец находится у края экрана."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
