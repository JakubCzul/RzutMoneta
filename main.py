import random
import cv2


def orzelczyreszka():
    slownik = {0: 'reszka', 1: 'orzel'}
    wyborgracza = input('Podaj co losujesz (orzel czy reszka): ')
    co_wypadlo = random.randint(0, 1)
    if (slownik.get(co_wypadlo) == wyborgracza or slownik.get(co_wypadlo) == wyborgracza):
        img1 = cv2.imread('C:\\Users\\kubac\\Documents\\GitHub\\PythonRzutMoneta\\zdj\\wygrana.jpg')
        cv2.imshow('image1', img1)
        cv2.waitKey(0)

    elif (slownik.get(co_wypadlo) != wyborgracza or slownik.get(co_wypadlo) != wyborgracza):
        img0 = cv2.imread('C:\\Users\\kubac\\Documents\\GitHub\\PythonRzutMoneta\\zdj\\przegrana.jpg')
        cv2.imshow('image', img0)
        cv2.waitKey(0)


orzelczyreszka()
