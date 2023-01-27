import os
import time
import cv2
import numpy as np
import pyscreenshot as ImageGrab
import pytesseract
import mouse
from win32api import keybd_event
import win32con


pytes = pytesseract.pytesseract
pytes.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR/tesseract'
time.sleep(1)
# берем персонажа в таргет с зажатой клавишей f = 0x46


def target():
    # берем в таргет
    keybd_event(0x46, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
    time.sleep(1)
    mouse.press(button='left')
    time.sleep(1)
    mouse.press(button='right')
    time.sleep(1)
    mouse.release(button='left')
    time.sleep(1)
    mouse.release(button='right')
    # проверка ги
    # получаем изображение таргета
    # делаем скрин области с названием ги и ником
    screen = np.array(ImageGrab.grab(bbox=(620, 595, 763, 640)))
    filename = 'image.png'
    cv2.imwrite(filename, screen)
    image = cv2.imread('Image.png')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255,
                           cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    # распознаем текст со скриншота
    text = pytesseract.image_to_string(thresh, lang='eng', config='--psm 6')
    # если текст не Привет! ничего не делаем, продолжаем ждать
    index = text.find("Привет")
    os.remove(filename)
    # Проверяем та ли эта гильдия
    # (если гильдий много, то можно создать список и проверять на включение)
    index = text.find('Hydra')
    index2 = text.find('Nosferatus')
    if index == -1 and index2 == -1:
        keybd_event(0x0D, 0, 0, 0)
        time.sleep(0.5)
        keybd_event(0x6D, 0, 0, 0)
        time.sleep(0.5)
        keybd_event(0x0D, 0, 0, 0)
        # Снимаем таргет
        mouse.press(button='left')
        time.sleep(1)
        mouse.release(button='left')
        time.sleep(1)
        keybd_event(0x46, 0, win32con.KEYEVENTF_KEYUP, 0)
        # ищем дальше
        # то есть ждем опять текста и смайлки привет
    else:
        # Баффаем
        keybd_event(0x51, 0, 0, 0)
        time.sleep(20)  # установить время ожидания = время баффа + 1 сек
        # Снимаем таргет
        keybd_event(0x65, 0, 0, 0)
        mouse.press(button='left')
        time.sleep(1)
        mouse.release(button='left')
        time.sleep(1)
        keybd_event(0x46, 0, win32con.KEYEVENTF_KEYUP, 0)
        # нажать смайлик 5(чтобы пролистался текст Привет)
        # pyautogui.press("0x30")
    cv2.destroyAllWindows()


target()
