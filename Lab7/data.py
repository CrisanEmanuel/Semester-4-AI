import os
import cv2
import numpy as np
from sklearn.preprocessing import StandardScaler


def load_images_from_folder(folder):
    imgs = []
    labels = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename))
        if img is not None:
            img = cv2.resize(img, (100, 100))  # Redimensionăm imaginile la aceeași dimensiune
            img = img / 255.0  # Normalizăm valorile pixelilor la intervalul [0, 1]
            imgs.append(img)
            if "sepia" in filename:
                labels.append(1)  # 1 pentru imagini cu filtru sepia
            else:
                labels.append(0)  # 0 pentru imagini fără filtru sepia
    return imgs, labels

