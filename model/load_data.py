import numpy as np
import os
import cv2
size = 128

def load_data():
    hotdog = len(os.listdir('./hotdog'))
    nothotdog = len(os.listdir('./nothotdog'))
    datasetx = np.ndarray((hotdog+nothotdog, size, size, 3))
    datasety = np.ndarray((hotdog+nothotdog, 1))
    i = 0
    for img in os.listdir('./hotdog'):
        mat = cv2.imread('./hotdog/'+img)
        datasetx[i] = mat
        datasety[i] = 1
        i+=1
    for img in os.listdir('./nothotdog'):
        mat = cv2.imread('./nothotdog/'+img)
        datasetx[i] = mat
        datasety[i] = 0
        i += 1
    return datasetx, datasety
