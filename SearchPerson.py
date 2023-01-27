import argparse
import pyautogui
import cv2
import numpy as np
import pyscreenshot as ImageGrab
import CheckGi
# python SearchPerson.py --window window.png --hi hi.png


def Search():
    # ищем смайлик Привет на экране
    # window - область экрана
    # hi - смайлик Привет!
    ap = argparse.ArgumentParser()
    ap.add_argument("-p",
                    "--window",
                    required=True,
                    help="Path to the window image")
    ap.add_argument("-w", "--hi", required=True, help="Path to the hi image")
    args = vars(ap.parse_args())

    # Когда в чате нашли Привет, ищем смайлик Привет!
    # делаем скрин области экрана
    window = np.array(ImageGrab.grab(bbox=(350, 115, 960, 430)))  # home
    # window = pyautogui.screenshot()
    hi = cv2.imread(args["hi"])  # образец смайлика Привет
    (hiHeight, hiWidth) = hi.shape[:2]

    # ищем смайлик на скрине области экрана
    result = cv2.matchTemplate(window, hi, cv2.TM_CCOEFF)
    (_, _, minLoc, maxLoc) = cv2.minMaxLoc(result)

    # получаем область вокруг смайлика
    topLeft = maxLoc  # верхний левый угол
    # правый нижний угол:
    botRight = (topLeft[0] + hiWidth, topLeft[1] + hiHeight)
    topXY = topLeft
    botXY = botRight
    roi = window[topLeft[1]:botRight[1], topLeft[0]:botRight[0]]
    mask = np.zeros(window.shape, dtype="uint8")
    window = cv2.addWeighted(window, 0.55, mask, 0.70, 0)
    window[topLeft[1]:botRight[1], topLeft[0]:botRight[0]] = roi

    # получаем координаты смайлика Привет и перемещаем туда курсор
    if topXY[0] < 660:
        pyautogui.moveTo(topXY[0] + int(390), botXY[1] + int(150))
        CheckGi.target()
    elif topXY[0] >= 660:
        pyautogui.moveTo(topXY[0] + int(375), botXY[1] + int(150))
        CheckGi.target()
