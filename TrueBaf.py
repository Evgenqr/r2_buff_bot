import pytesseract
import cv2
import sys
import numpy as np
import pyscreenshot as ImageGrab
import SearchPerson

pytes = pytesseract.pytesseract
pytes.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR/tesseract'


def statrbuff():
    # распознаем текст обычного чата и ждем когда будет текст Привет!
    while (True):
        filename = 'image.png'
        # получаем скрин области экрана
        # screen = np.array(ImageGrab.grab(bbox=(10, 588, 295, 605)))  # work
        screen = np.array(ImageGrab.grab(bbox=(10, 532, 220, 550)))  # home
        cv2.imwrite(filename, screen)
        image = cv2.imread('Image.png')
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        thresh = cv2.threshold(gray, 0, 255,
                               cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        # распознаем текст со скриншота
        data = pytesseract.image_to_string(thresh,
                                           lang='rus',
                                           config='--psm 6')
        print(data)
        # если текст не Привет! ничего не делаем, продолжаем ждать
        index = data.find("Привет")
        if index == -1:  # False
            pass
        else:  # True
            # вызываем функцию поиска персонажа (делаем скрин и
            # ищем смайл Привет!
            sys.argv = [
                sys.argv[0], "--window", "window.png", "--hi", "hi.png"
            ]

            SearchPerson.Search()
        # cv2.destroyAllWindows()


statrbuff()
