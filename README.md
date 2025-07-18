# Alien Invasion - Космический шутер для Windows

<img src="screenshot_game.png" alt="Game Screenshot" width="600"/> 

Проект представляет собой классический космический шутер, где игрок управляет кораблём, уничтожает волны пришельцев и защищает Землю. Написан на Python с использованием библиотеки PyGame.

**Важное замечание:** Данная версия игры разработана и протестирована исключительно для операционной системы Windows. На других операционных системах (Linux, macOS) игра может работать некорректно или не запускаться вовсе.

## 🚀 Установка и запуск

### 1. Установите PyGame
Откройте командную строку (CMD) и выполните:
```cmd
pip install pygame
```

### 2. Запустите игру
1. Скачайте архив с игрой и распакуйте его в любую папку
2. Откройте командную строку в папке с игрой:
   - Перейдите в папку с помощью `cd путь_к_папке`
3. Выполните команду:
```cmd
python alien_invasion.py
```

## 🎮 Управление в игре

| Клавиша       | Действие                     |
|---------------|------------------------------|
| **← →**       | Движение корабля влево/вправо|
| **Пробел**    | Стрельба                     |
| **P**         | Пауза/продолжение игры       |
| **Q**         | Выход из игры                |
| **ESC**       | Выход в главное меню         |

## 🧩 Структура проекта

```
alien-invasion/
├── alien_invasion.py      # Основной файл игры
├── settings.py            # Настройки игры
├── ship.py                # Класс корабля игрока
├── bullet.py              # Класс снарядов
├── alien.py               # Класс пришельцев
├── game_stats.py          # Статистика игры
├── button.py              # Класс кнопок интерфейса
├── scoreboard.py          # Панель счета и рекордов
├── game_functions.py      # Вспомогательные функции
├── screenshot.png         # Скриншот игры
└── README.md              # Этот файл
```

## 🛠 Технический стек

- Python 3.10+
- PyGame 2.5+
- Windows API для определения разрешения экрана

<div align="center">
  <h3>Наслаждайтесь игрой и защищайте Землю от инопланетного вторжения! 👾🚀</h3>
</div>