"""
Pentru imaginile care contin biciclete:
    a. sa se localizeze automat bicicletele in aceste imagini si sa se evidentieze chenarele care incadreaza bicicletele
    b. sa se eticheteze (fara ajutorul algoritmilor de AI) aceste imagini cu chenare care sa incadreze cat mai exact
     bicicletele. Care task dureaza mai mult (cel de la punctul a sau cel de la punctul b)?
    c. sa se determine performanta algoritmului de la punctul a avand in vedere etichetarile realizate la punctul b
     (se vor folosi cel putin 2 metrici).
"""
import timeit

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes

from msrest.authentication import CognitiveServicesCredentials
import os
import matplotlib.pyplot as plt
import cv2

'''
Authenticate
Authenticates your credentials and creates a client.
'''
subscription_key = os.environ["VISION_KEY"]
endpoint = os.environ["VISION_ENDPOINT"]
computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))
'''
END - Authenticate
'''


# returneaza pathurile imaginilor care contin 'bike' in denumire din folderul dat ca parametru
def images_path(folder_path):
    image_extensions = ['.jpg']
    image_files = []

    for file in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, file)):
            if any(file.lower().endswith(ext) for ext in image_extensions):
                # Verificăm dacă numele fișierului se potrivește cu șablonul "bikeNN.jpg"
                if file.lower().startswith("bike") and len(file) == 10 and file[4:6].isdigit() and 1 <= int(
                        file[4:6]) <= 10:
                    image_files.append(os.path.join(folder_path, file))

    return image_files


# imaginile bike06.jpg si bike08.jpg nu sunt gasite de API
def problema2a(images_folder):
    img_paths = images_path(images_folder)
    # automatically identify the object location for each image
    for img_path in img_paths:
        img = open(img_path, "rb")
        result = computervision_client.analyze_image_in_stream(img, visual_features=[VisualFeatureTypes.objects])
        for ob in result.objects:
            if ob.object_property == 'bicycle':
                bike_bb = [ob.rectangle.x, ob.rectangle.y, ob.rectangle.x + ob.rectangle.w,
                           ob.rectangle.y + ob.rectangle.h]
                img = plt.imread(img_path)
                fig, ax = plt.subplots()
                ax.imshow(img)
                ax.add_patch(plt.Rectangle(xy=(bike_bb[0], bike_bb[1]), width=bike_bb[2] - bike_bb[0],
                                           height=bike_bb[3] - bike_bb[1], color='green', linewidth=4,
                                           fill=False))
                ax.axis('off')  # Hide axes
                plt.show()


# problema 2a doar ca nu afiseaza imaginile, e pentru a compara timpul de rulare cu problema 2b
# detecteaza apoi incadreaza si returneaza coordonatele dreptunghiului pentru a fi folosite la problema 2c
# imaginile bike06.jpg si bike08.jpg nu sunt gasite de API
def problema2aAUX(images_folder):
    img_paths = images_path(images_folder)
    coordonate_dreptunghiuri = []
    for img_path in img_paths:
        img = open(img_path, "rb")
        result = computervision_client.analyze_image_in_stream(img, visual_features=[VisualFeatureTypes.objects])
        for ob in result.objects:
            if ob.object_property == 'bicycle':
                bike_bb = [ob.rectangle.x, ob.rectangle.y, ob.rectangle.x + ob.rectangle.w,
                           ob.rectangle.y + ob.rectangle.h]
                coordonate_dreptunghiuri.append([ob.rectangle.x, ob.rectangle.y, ob.rectangle.x + ob.rectangle.w,
                                                 ob.rectangle.y + ob.rectangle.h])
                img = plt.imread(img_path)
                fig, ax = plt.subplots()
                ax.imshow(img)
                ax.add_patch(plt.Rectangle(xy=(bike_bb[0], bike_bb[1]), width=bike_bb[2] - bike_bb[0],
                                           height=bike_bb[3] - bike_bb[1], color='green', linewidth=4,
                                           fill=False))
    return coordonate_dreptunghiuri


def problema2b(images_folder):
    img_paths = images_path(images_folder)
    for img_path in img_paths:
        image = cv2.imread(img_path)

        # Convert the image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Apply Gaussian blur to reduce noise
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)

        # Apply Canny Edge Detection
        edges = cv2.Canny(blurred, 50, 150)

        # Find contours in the edges image
        contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Iterate through contours and find the largest one (assuming it represents the bicycle)
        biggest = sorted(contours, key=cv2.contourArea, reverse=True)[0]
        x, y, w, h = cv2.boundingRect(biggest)

        # Draw a rectangle around the largest contour (representing the bicycle)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Display the image with the detected bicycle
        cv2.imshow("Detected Bicycle", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


# problema 2b doar ca nu afiseaza imaginile, e pentru a compara timpul de rulare cu problema 2a
# detecteaza apoi incadreaza si returneaza coordonatele dreptunghiului pentru a fi folosite la problema 2c
def problema2bAUX(images_folder):
    img_paths = images_path(images_folder)
    coordonate_dreptunghiuri = []
    for img_path in img_paths:
        image = cv2.imread(img_path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        edges = cv2.Canny(blurred, 50, 150)
        contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        biggest = sorted(contours, key=cv2.contourArea, reverse=True)[0]
        x, y, w, h = cv2.boundingRect(biggest)
        coordonate_dreptunghiuri.append([x, y, x + w, y + h])
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return coordonate_dreptunghiuri


def calculate_iou(box1, box2):
    # Extrage coordonatele extremelor dreptunghiului 1
    x1_tl, y1_tl, x1_br, y1_br = box1
    # Extrage coordonatele extremelor dreptunghiului 2
    x2_tl, y2_tl, x2_br, y2_br = box2

    # Calculează coordonatele punctului de intersectare între cele două dreptunghiuri
    x_left = max(x1_tl, x2_tl)
    y_top = max(y1_tl, y2_tl)
    x_right = min(x1_br, x2_br)
    y_bottom = min(y1_br, y2_br)

    # Calculează aria de intersectare
    intersection_area = max(0, x_right - x_left) * max(0, y_bottom - y_top)

    # Calculează aria de suprapunere
    box1_area = (x1_br - x1_tl) * (y1_br - y1_tl)
    box2_area = (x2_br - x2_tl) * (y2_br - y2_tl)
    iou = intersection_area / float(box1_area + box2_area - intersection_area)

    return iou


def average_precision(boxes1, boxes2, threshold):
    """
        boxes1 și boxes2 reprezintă coordonatele dreptunghiurilor calculate de fiecare funcție pentru localizarea imaginii.
    Funcția average_precision calculează precizia medie pe baza IoU (Intersection over Union) între dreptunghiurile
    calculate de cele două funcții, folosind un anumit threshold pentru a decide când două dreptunghiuri sunt considerate
    a fi aceeași. Precizia medie este calculată ca raportul dintre suma IoU-urilor și numărul total de dreptunghiuri
    calculate de prima funcție.
    :param boxes1: coordonatele dreptunghiurilor calculate de prima funcție
    :param boxes2: coordonatele dreptunghiurilor calculate de a doua funcție
    :param threshold: valoarea minimă a IoU-ului pentru a considera că două dreptunghiuri sunt aceleași
    :return: precizia medie
    """
    total_iou = 0
    for box1 in boxes1:
        max_iou = 0
        for box2 in boxes2:
            iou = calculate_iou(box1, box2)
            if iou > max_iou:
                max_iou = iou
        if max_iou >= threshold:
            total_iou += max_iou

    avg_precision = total_iou / len(boxes1)
    return avg_precision


def problema2c(folder_path, threshold):
    coordonate_dreptunghiuri_2a = problema2aAUX(folder_path)
    coordonate_dreptunghiuri_2b = problema2bAUX(folder_path)

    # eliminam coordonatele pentru imaginile care nu sunt gasite de API
    coordonate_dreptunghiuri_2b.pop(5)
    coordonate_dreptunghiuri_2b.pop(7)

    # iou mare => suprapunere mare => detectie buna (iou este intr-un interval [0, 1])
    for i in range(len(coordonate_dreptunghiuri_2b)):
        print("IoU pentru imaginea ", i + 1, " este: ",
              calculate_iou(coordonate_dreptunghiuri_2a[i], coordonate_dreptunghiuri_2b[i]))

    avrg_precision = average_precision(coordonate_dreptunghiuri_2a, coordonate_dreptunghiuri_2b, threshold)
    print("Precizia medie este: ", avrg_precision)


def comparareTimpIntre2aSi2b():
    timp_1 = timeit.timeit("problema2aAUX('images')", globals=globals(), number=1)
    timp_2 = timeit.timeit("problema2bAUX('images')", globals=globals(), number=1)
    print("Timpul pentru 2a este (cu AI): ", timp_1)
    print("Timpul pentru 2b este (fara AI): ", timp_2)


def problema2():
    problema2a('images')
    # problema2b('images')
    # problema2c('images', 0.5)
    # comparareTimpIntre2aSi2b()
