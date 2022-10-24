
import numpy as np
import os
from imageio import imread, imsave
from matplotlib import pyplot as plt
from skimage.color import rgb2gray, rgba2rgb
import cv2 as cv

# Принимает путь к изображению
# Возвращает изображение
# Функция, которая считывает и возвращает изображение
def get_image(path):
    image = imread(path)

    return image

# Принимает путь к папке, где лежат изображения
# Возвращает массив изображений 
# Функция, которая считывает из папки изображения
def get_all_images(path):
    images = []
    paths = os.listdir(path)

    for i in paths:
        image_path = os.path.join(path, i)
        image = imread(image_path)
        images.append(image)
        
    return images

def convert_to_BW(image):
    image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    return image_gray

def convert_to_trashold(image, intensity):
    ret, thresh = cv.threshold(image, intensity, 255, cv.THRESH_BINARY)

    return thresh


def find_contours(thresh):
    contours, hierarchy = cv.findContours(image=thresh, mode=cv.RETR_TREE, method=cv.CHAIN_APPROX_NONE)
    
    return contours                        
