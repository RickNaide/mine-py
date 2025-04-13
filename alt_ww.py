#alt ww.py


import sys
import time      # Зависисмоти для работы проекты
from pynput.mouse import Button, Controller # Библиотека автоматизации действий клавиатуры установка.. в пакетнике pip install pyautogui
from pynput.keyboard import Controller as KeyboardController
import datetime
import pyautogui
from mouse import move_rel
#localtime = datetime.datetime.now()



global pause
global task_i
global axe_i
global load
global task

load = 0
pause = 1


mouse = Controller() # - создание контроля
keyboard = KeyboardController() # - создание вирт клавы

#----------------------------------------Методы работы--------------------------------------------------------------
class Player:
	def AntiAfk():
		
		# Анти-Афк подъем на 10 пикселей вправо (в pyautogui move(10,0) — это движение вправо)
		move_rel(10, 0)  # pynput.move() не поддерживает duration, поэтому задержка имитируется time.sleep()
		time.sleep(0.5)  # Задержка для имитации плавности
		
		time.sleep(1)  # Пауза между движениями
		
		# Анти-Афк опускание на 10 пикселей влево (в pyautogui move(-10,0) — это движение влево)
		move_rel(-10, 0)
		time.sleep(0.5)  # Задержка для имитации плавности
		
	def Change_Axe():
		time.sleep(8)
		
		# Перемещение влево (-550 по X)
		move_rel(-200, 0)
		time.sleep(1.5)  # Имитация duration=1.5
		
		keyboard.press('l')  # Нажатие клавиши 'l'
		keyboard.release('l')  # Отпускание (pynput требует явного release)
		time.sleep(1)
		
		# --- Кнопка сортировки ---
		mouse.position = (791, 215)  # Аналог moveTo
		time.sleep(1)
		mouse.click(Button.left, 1)  # ЛКМ, 1 клик
		time.sleep(1)
		
		# --- Перетаскивание сломанного топора в сундук ---
		mouse.position = (494, 605)  # 1 слот инвентаря
		mouse.click(Button.left, 1)
		time.sleep(1)
		
		mouse.position = (782, 424)  # Слот для сломанного топора
		mouse.click(Button.left, 1)
		time.sleep(1)
		
		# --- Взаимодействие с инвентарем ---
		mouse.position = (497, 243)
		mouse.click(Button.left, 1)
		
		mouse.position = (494, 605)
		mouse.click(Button.left, 1)
		
		# --- Закрытие интерфейса ---
		pyautogui.press('Esc')
		time.sleep(1)            
		load = 0
		
		# Возвращение мыши в исходное положение (+550 по X)
		move_rel(200, 0)
		time.sleep(1.5)

	def ExchangeSell():
		global task

		time.sleep(2)
		# Поворот к бирже и ее открытие
		move_rel(0, 75)
		time.sleep(2)  # duration=1
		keyboard.press('l')
		keyboard.release('l')

		# Блок 1 (496, 495)
		time.sleep(0.5)
		mouse.position = (496, 495)
		time.sleep(0.5)  # duration=1
		mouse.click(Button.left)
		mouse.click(Button.right)
		time.sleep(0.5)
		mouse.position = (518, 350)
		time.sleep(0.5)  # duration=1
		mouse.click(Button.left)
		mouse.position = (741, 431)
		time.sleep(0.5)  # duration=1
		mouse.click(Button.left)

		# Блок 2 (531, 495)
		time.sleep(0.5)
		mouse.position = (531, 495)
		time.sleep(0.5)
		mouse.click(Button.left)
		mouse.click(Button.right)
		time.sleep(0.5)
		mouse.position = (518, 350)
		time.sleep(0.5)
		mouse.click(Button.left)
		mouse.position = (740, 431)
		time.sleep(0.5)
		mouse.click(Button.left)

		# Блок 3 (567, 495)
		time.sleep(0.5)
		mouse.position = (567, 495)
		time.sleep(0.5)
		mouse.click(Button.left)
		mouse.click(Button.right)
		time.sleep(0.5)
		mouse.position = (518, 350)
		time.sleep(0.5)
		mouse.click(Button.left)
		mouse.position = (740, 431)
		time.sleep(0.5)
		mouse.click(Button.left)

		# Блок 4 (603, 495)
		time.sleep(0.5)
		mouse.position = (603, 495)
		time.sleep(0.5)
		mouse.click(Button.left)
		mouse.click(Button.right)
		time.sleep(0.5)
		mouse.position = (518, 350)
		time.sleep(0.5)
		mouse.click(Button.left)
		mouse.position = (740, 431)
		time.sleep(0.5)
		mouse.click(Button.left)

		# Блок 5 (641, 495)
		time.sleep(0.5)
		mouse.position = (641, 495)
		time.sleep(0.5)
		mouse.click(Button.left)
		mouse.click(Button.right)
		time.sleep(0.5)
		mouse.position = (518, 350)
		time.sleep(0.5)
		mouse.click(Button.left)
		mouse.position = (740, 431)
		time.sleep(0.5)
		mouse.click(Button.left)

		# Блок 6 (674, 495)
		time.sleep(0.5)
		mouse.position = (674, 495)
		time.sleep(0.5)
		mouse.click(Button.left)
		mouse.click(Button.right)
		time.sleep(0.5)
		mouse.position = (518, 350)
		time.sleep(0.5)
		mouse.click(Button.left)
		mouse.position = (740, 431)
		time.sleep(0.5)
		mouse.click(Button.left)

		# Блок 7 (711, 495)
		time.sleep(0.5)
		mouse.position = (711, 495)
		time.sleep(0.5)
		mouse.click(Button.left)
		mouse.click(Button.right)
		time.sleep(0.5)
		mouse.position = (518, 350)
		time.sleep(0.5)
		mouse.click(Button.left)
		mouse.position = (740, 431)
		time.sleep(0.5)
		mouse.click(Button.left)

		# Блок 8 (748, 495)
		time.sleep(0.5)
		mouse.position = (748, 495)
		time.sleep(0.5)
		mouse.click(Button.left)
		mouse.click(Button.right)
		time.sleep(0.5)
		mouse.position = (518, 350)
		time.sleep(0.5)
		mouse.click(Button.left)
		mouse.position = (740, 431)
		time.sleep(0.5)
		mouse.click(Button.left)

		# Блок 9 (781, 495)
		time.sleep(0.5)
		mouse.position = (781, 495)
		time.sleep(0.5)
		mouse.click(Button.left)
		mouse.click(Button.right)
		time.sleep(0.5)
		mouse.position = (518, 350)
		time.sleep(0.5)
		mouse.click(Button.left)
		mouse.position = (740, 431)
		time.sleep(0.5)
		mouse.click(Button.left)
	 #-----------------------------------------------------------
		 # Блок 10 (494, 534)
		time.sleep(0.5)
		mouse.position = (494, 534)
		time.sleep(0.5)
		mouse.click(Button.left)
		mouse.click(Button.right)
		time.sleep(0.5)
		mouse.position = (518, 350)
		time.sleep(0.5)
		mouse.click(Button.left)
		mouse.position = (740, 431)
		time.sleep(0.5)
		mouse.click(Button.left)
		
		# Блок 11 (534, 534)
		time.sleep(0.5)
		mouse.position = (534, 534)
		time.sleep(0.5)
		mouse.click(Button.left)
		mouse.click(Button.right)
		time.sleep(0.5)
		mouse.position = (518, 350)
		time.sleep(0.5)
		mouse.click(Button.left)
		mouse.position = (740, 431)
		time.sleep(0.5)
		mouse.click(Button.left)

		# Блок 12 (566, 532)
		time.sleep(0.5)    
		mouse.position = (566, 532)
		time.sleep(0.5)
		mouse.click(Button.left)
		mouse.click(Button.right)
		time.sleep(0.5)
		mouse.position = (518, 350)
		time.sleep(0.5)
		mouse.click(Button.left)
		mouse.position = (740, 431)
		time.sleep(0.5)
		mouse.click(Button.left)
		
		# Блок 13 (601, 532)
		time.sleep(0.5)
		mouse.position = (601, 532)
		time.sleep(0.5)
		mouse.click(Button.left)
		mouse.click(Button.right)
		time.sleep(0.5)
		mouse.position = (518, 350)
		time.sleep(0.5)
		mouse.click(Button.left)
		mouse.position = (740, 431)
		time.sleep(0.5)
		mouse.click(Button.left)
		
		# Блок 14 (641, 532)
		time.sleep(0.5)
		mouse.position = (641, 532)
		time.sleep(0.5)
		mouse.click(Button.left)
		mouse.click(Button.right)
		time.sleep(0.5)
		mouse.position = (518, 350)
		time.sleep(0.5)
		mouse.click(Button.left)
		mouse.position = (740, 431)
		time.sleep(0.5)
		mouse.click(Button.left)
		
		# Блок 15 (677, 532)
		time.sleep(0.5)
		mouse.position = (677, 532)
		time.sleep(0.5)
		mouse.click(Button.left)
		mouse.click(Button.right)
		time.sleep(0.5)
		mouse.position = (518, 350)
		time.sleep(0.5)
		mouse.click(Button.left)
		mouse.position = (740, 431)
		time.sleep(0.5)
		mouse.click(Button.left)
		
		# Блок 16 (711, 532)
		time.sleep(0.5)
		mouse.position = (711, 532)
		time.sleep(0.5)
		mouse.click(Button.left)
		mouse.click(Button.right)
		time.sleep(0.5)
		mouse.position = (518, 350)
		time.sleep(0.5)
		mouse.click(Button.left)
		mouse.position = (740, 431)
		time.sleep(0.5)
		mouse.click(Button.left)
		
		# Блок 17 (748, 532)
		time.sleep(0.5)
		mouse.position = (748, 532)
		time.sleep(0.5)
		mouse.click(Button.left)
		mouse.click(Button.right)
		time.sleep(0.5)
		mouse.position = (518, 350)
		time.sleep(0.5)
		mouse.click(Button.left)
		mouse.position = (740, 431)
		time.sleep(0.5)
		mouse.click(Button.left)
		
		# Блок 18 (784, 532)
		time.sleep(0.5)
		mouse.position = (784, 532)
		time.sleep(0.5)
		mouse.click(Button.left)
		mouse.click(Button.right)
		time.sleep(0.5)
		mouse.position = (518, 350)
		time.sleep(0.5)
		mouse.click(Button.left)
		mouse.position = (740, 431)
		time.sleep(0.5)
		mouse.click(Button.left)
	#----------------------------------------------------------------------
		# Блок 19 (496, 568)
		time.sleep(0.5)
		mouse.position = (496, 568)  # pyautogui.moveTo(496, 568, duration=1)
		time.sleep(0.5)
		mouse.click(Button.left, 1)  # pyautogui.click()
		mouse.click(Button.right, 1)  # pyautogui.click(button='right')
		time.sleep(0.5)
		mouse.position = (518, 350)  # pyautogui.moveTo(518, 350, duration=1)
		time.sleep(0.5)
		mouse.click(Button.left, 1)  # pyautogui.click()
		mouse.position = (740, 431)  # pyautogui.moveTo(740, 431, duration=1)
		time.sleep(0.5)
		mouse.click(Button.left, 1)  # pyautogui.click()

		# Блок 20 (532, 568) 
		time.sleep(0.5)
		mouse.position = (532, 568)  # pyautogui.moveTo(532, 568, duration=1)
		time.sleep(0.5)
		mouse.click(Button.left, 1)
		mouse.click(Button.right, 1)
		time.sleep(0.5)
		mouse.position = (518, 350)
		time.sleep(0.5)
		mouse.click(Button.left, 1)
		mouse.position = (740, 431)
		time.sleep(0.5)
		mouse.click(Button.left, 1)
		
		# Блок 21 (565, 568)
		time.sleep(0.5)
		mouse.position = (565, 568)  # pyautogui.moveTo(565, 568, duration=1)
		time.sleep(0.5)
		mouse.click(Button.left, 1)
		mouse.click(Button.right, 1)
		time.sleep(0.5)
		mouse.position = (518, 350)
		time.sleep(0.5)
		mouse.click(Button.left, 1)
		mouse.position = (740, 431)
		time.sleep(0.5)
		mouse.click(Button.left, 1)

		# Блок 22 (607, 568)
		time.sleep(0.5)
		mouse.position = (607, 568)  # pyautogui.moveTo(607, 568, duration=1)
		time.sleep(0.5)
		mouse.click(Button.left, 1)
		mouse.click(Button.right, 1)
		time.sleep(0.5)
		mouse.position = (518, 350)
		time.sleep(0.5)
		mouse.click(Button.left, 1)
		mouse.position = (740, 431)
		time.sleep(0.5)
		mouse.click(Button.left, 1)

		# Блок 23 (639, 568)
		time.sleep(0.5)
		mouse.position = (639, 568)  # pyautogui.moveTo(639, 568, duration=1)
		time.sleep(0.5)
		mouse.click(Button.left, 1)
		mouse.click(Button.right, 1)
		time.sleep(0.5)
		mouse.position = (518, 350)
		time.sleep(0.5)
		mouse.click(Button.left, 1)
		mouse.position = (740, 431)
		time.sleep(0.5)
		mouse.click(Button.left, 1)
		
		# Блок 24 (674, 568)
		time.sleep(0.5)
		mouse.position = (674, 568)  # pyautogui.moveTo(674, 568, duration=1)
		time.sleep(0.5)
		mouse.click(Button.left, 1)
		mouse.click(Button.right, 1)
		time.sleep(0.5)
		mouse.position = (518, 350)
		time.sleep(0.5)
		mouse.click(Button.left, 1)
		mouse.position = (740, 431)
		time.sleep(0.5)
		mouse.click(Button.left, 1)
		
		# Блок 25 (711, 571) - особый Y=571
		time.sleep(0.5)
		mouse.position = (711, 568)  # pyautogui.moveTo(711, 571, duration=1)
		time.sleep(0.5)
		mouse.click(Button.left, 1)
		mouse.click(Button.right, 1)
		time.sleep(0.5)
		mouse.position = (518, 350)
		time.sleep(0.5)
		mouse.click(Button.left, 1)
		mouse.position = (740, 431)
		time.sleep(0.5)
		mouse.click(Button.left, 1)
		
		# Блок 26 (742, 588) - особый Y=588
		time.sleep(0.5)
		mouse.position = (742, 588)  # pyautogui.moveTo(742, 588, duration=1)
		time.sleep(0.5)
		mouse.click(Button.left, 1)
		mouse.click(Button.right, 1)
		time.sleep(0.5)
		mouse.position = (518, 350)
		time.sleep(1)
		mouse.click(Button.left, 1)
		mouse.position = (740, 431)
		time.sleep(0.5)
		mouse.click(Button.left, 1)
		
		# Блок 27 (786, 568)
		time.sleep(0.5)
		mouse.position = (786, 568)  # pyautogui.moveTo(786, 568, duration=1)
		time.sleep(0.5)
		mouse.click(Button.left, 1)
		mouse.click(Button.right, 1)
		time.sleep(0.5)
		mouse.position = (518, 350)
		time.sleep(0.5)
		mouse.click(Button.left, 1)
		mouse.position = (740, 431)
		time.sleep(0.5)
		mouse.click(Button.left, 1)
		time.sleep(0.5)

		# --- Закрытие интерфейса ---
		pyautogui.press('Esc')
		time.sleep(2)
		move_rel(0, -75)  # pyautogui.move(0, -115, duration=1)
		time.sleep(1)
		
	def Load_Inventory():
		time.sleep(2)  # Пауза
		
		# Поворот на нижний сборщик
		move_rel(0, -75)  # pyautogui.move(550, 0, duration=1)
		time.sleep(1)
		keyboard.press('l')  # pyautogui.press('l')
		keyboard.release('l')
		time.sleep(1)
		
		mouse.position = (792, 507)  # pyautogui.moveTo(792, 507, 1)
		time.sleep(1)
		mouse.click(Button.left, 1)  # pyautogui.click()
		time.sleep(1)
		
		# --- Закрытие интерфейса ---
		pyautogui.press('Esc')  # Зажимаем Esc
		time.sleep(3)            # Удерживаем 1 секунду

		# Поднятие до второго сборщика
		move_rel(0, -150)  # pyautogui.move(0, 150, duration=1)
		time.sleep(1)
		keyboard.press('l')
		keyboard.release('l')
		time.sleep(1)
		
		mouse.position = (792, 507)  # pyautogui.moveTo(792, 507, 1)
		time.sleep(1)
		mouse.click(Button.left, 1)
		time.sleep(1)
        
		# --- Закрытие интерфейса ---
		pyautogui.press('Esc')
		time.sleep(3)            # Удерживаем 1 секунду

		# Возврат в исходное положение
		move_rel(0, 225)  # pyautogui.move(0, -150, duration=1)
		time.sleep(1)
		
	def Start():
		global pause
		time.sleep(6)
		score = 0
		load = 0
		
		while(True):
			if score != 252:
				no_afk = Player.AntiAfk()

				keyboard.press('2') #Выбираем кокос
				keyboard.release('2')
				time.sleep(pause)
				keyboard.press('l') #ставим кокос в блок
				keyboard.release('l')
				time.sleep(pause)
				keyboard.press('3') #выбираем муку
				keyboard.release('3')
				time.sleep(pause)
				keyboard.press('l') #выращиваем кокос
				time.sleep(pause)
				keyboard.release('l')
				keyboard.press('1') #берем топор
				keyboard.release('1')
				mouse.press(Button.left)  # Нажать и удерживать левую кнопку мыши
				time.sleep(pause)
				mouse.release(Button.left)    # Отпустить левую кнопку мыши
				score = score + 1
				#------------------------------------------------------------------ 
				keyboard.press('4') #Выбираем кокос
				keyboard.release('4')
				time.sleep(pause)
				keyboard.press('l') #ставим кокос в блок
				keyboard.release('l')
				time.sleep(pause)
				keyboard.press('5') #выбираем муку
				keyboard.release('5')
				time.sleep(pause)
				keyboard.press('l') #выращиваем кокос
				time.sleep(pause)
				keyboard.release('l')
				keyboard.press('1') #берем топор
				keyboard.release('1')
				mouse.press(Button.left)  # Нажать и удерживать левую кнопку мыши
				time.sleep(pause)
				mouse.release(Button.left)    # Отпустить левую кнопку мыши
				score = score + 1
				#------------------------------------------------------------------ 
				keyboard.press('6') #Выбираем кокос
				keyboard.release('6')
				time.sleep(pause)
				keyboard.press('l') #ставим кокос в блок
				keyboard.release('l')
				time.sleep(pause)
				keyboard.press('7') #выбираем муку
				keyboard.release('7')
				time.sleep(pause)
				keyboard.press('l') #выращиваем кокос
				time.sleep(pause)
				keyboard.release('l')
				keyboard.press('1') #берем топор
				keyboard.release('1')
				mouse.press(Button.left)  # Нажать и удерживать левую кнопку мыши
				time.sleep(pause)
				mouse.release(Button.left)    # Отпустить левую кнопку мыши
				score = score + 1
					#-------------------------------------------------------------------
				keyboard.press('8') #Выбираем кокос
				keyboard.release('8')
				time.sleep(pause)
				keyboard.press('l') #ставим кокос в блок
				keyboard.release('l')
				time.sleep(pause)
				keyboard.press('9') #выбираем муку
				keyboard.release('9')
				time.sleep(pause)
				keyboard.press('l') #выращиваем кокос
				time.sleep(pause)
				keyboard.release('l')
				keyboard.press('1') #берем топор
				keyboard.release('1')
				mouse.press(Button.left)  # Нажать и удерживать левую кнопку мыши
				time.sleep(pause)
				mouse.release(Button.left)    # Отпустить левую кнопку мыши
				score = score + 1
			else:
				Player.ExchangeSell()
				print("Я продал ресы")
				time.sleep(1)
				Player.Load_Inventory()
				load = load + 1
				time.sleep(1)
				score = 0

				if load == 6:
					Player.Change_Axe()
				else:
					pass

#-RUN-
time.sleep(4)
Player.Start()
#time.sleep(4)
#Player.ExchangeSell()
#Test.cheak_cord()
#Player.Change_Axe()
#Player.Load_Inventory()
