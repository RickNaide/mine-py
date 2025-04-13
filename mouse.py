#test mouse lib 
import sys
import time      # Зависисмоти для работы проекты
from pynput.mouse import Button, Controller # Библиотека автоматизации действий клавиатуры установка.. в пакетнике pip install pyautogui
from pynput.keyboard import Controller as KeyboardController
import datetime
import pyautogui
import time
import math


def smooth_move_to(x, y, duration=1, steps=50):
    """
    Плавное перемещение курсора к координатам (x, y) за заданное время.
    
    :param x: Конечная координата X
    :param y: Конечная координата Y
    :param duration: Длительность перемещения в секундах (по умолчанию 0.5)
    :param steps: Количество шагов анимации (по умолчанию 50)
    """
    mouse = Controller()
    start_x, start_y = mouse.position
    
    for i in range(steps + 1):
        # Вычисляем прогресс от 0 до 1
        progress = i / steps
        
        # Применяем плавную кривую (например, квадратичную)
        # Можно использовать другие easing-функции для разного эффекта
        smooth_progress = progress ** 2  # Квадратичное замедление
        
        # Вычисляем промежуточные координаты
        current_x = start_x + (x - start_x) * smooth_progress
        current_y = start_y + (y - start_y) * smooth_progress
        
        # Перемещаем курсор
        mouse.position = (current_x, current_y)
        
        # Небольшая задержка для плавности
        time.sleep(duration / steps)


def move_rel(dx, dy, duration=2, steps=60):
    """
    Плавное перемещение курсора на заданное расстояние от текущего положения.
    
    :param dx: Смещение по оси X (в пикселях)
    :param dy: Смещение по оси Y (в пикселях)
    :param duration: Длительность перемещения в секундах (по умолчанию 1)
    :param steps: Количество шагов анимации (по умолчанию 50)
    """
    mouse = Controller()
    start_x, start_y = mouse.position
    target_x = start_x + dx
    target_y = start_y + dy
    
    for i in range(steps + 1):
        # Вычисляем прогресс от 0 до 1
        progress = i / steps
        
        # Применяем плавную кривую (квадратичное замедление)
        smooth_progress = progress ** 2
        
        # Вычисляем промежуточные координаты
        current_x = start_x + dx * smooth_progress
        current_y = start_y + dy * smooth_progress
        
        # Перемещаем курсор
        mouse.position = (current_x, current_y)
        
        # Небольшая задержка для плавности
        time.sleep(duration / steps)





def get_mouse_position():
    """Возвращает текущие координаты курсора мыши (x, y)."""
    mouse = Controller()
    return mouse.position


def AntiAfk():
	
	x, y = get_mouse_position()
	time.sleep(1)
	smooth_move_to(x-50, y-0)
	time.sleep(1)
	x, y = get_mouse_position()
	smooth_move_to(x+50, y+0)
	time.sleep(1)
	




























   
def main():
	while(True):	
		time.sleep(3)
		smooth_move_relative(-500, 0)
		time.sleep(2)
		smooth_move_relative(500, 0)
		time.sleep(2)
		smooth_move_relative(500,0)
		time.sleep(2)
		smooth_move_relative(-500,0)
		
	
	
	
	
	
	
    
# Пример использования:
if __name__ == "__main__":
	main()
