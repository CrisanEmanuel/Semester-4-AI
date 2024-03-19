import io
from PIL import Image
import cv2
import os
import time

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from msrest.authentication import CognitiveServicesCredentials

subscription_key = os.environ["VISION_KEY"]
endpoint = os.environ["VISION_ENDPOINT"]
computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))


# 1) Adaptabilitate la condițiile de iluminare
# 2) Reduzerea efectelor nedorite ale iluminării neuniforme
# 3) Îmbunătățirea contrastului textului
# 4) Separarea textului de fundal: prin aplicarea unei binarizări adaptative, se pot evidenția mai bine contururile
# textului față de fundalul imaginii, facilitând astfel procesul de segmentare și recunoaștere a textului.
def binarizare_adaptiva(image):
    # Convertirea imaginii la tonuri de gri
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Aplicarea thresholding-ului adaptiv
    binary = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

    return binary


# Convertirea imaginii la tonuri de gri pentru a simplifica prelucrarea.
# Aplicarea filtrului bilateral pentru a elimina zgomotul din imagine și pentru a îmbunătăți claritatea contururilor textului.
# + redimensionarea imaginii pentru a reduce timpul de procesare.
def bilateral_filter(image, dimensiune_noua):
    # Redimensionare imagine
    image_resized = cv2.resize(image, dimensiune_noua, interpolation=cv2.INTER_AREA)

    # Convertirea imaginii la tonuri de gri
    gray = cv2.cvtColor(image_resized, cv2.COLOR_BGR2GRAY)

    # Aplicarea filtrului bilateral
    processed_image = cv2.bilateralFilter(gray, 9, 75, 75)

    return processed_image


def recunoastere_text_aux(img):
    read_response = computervision_client.read_in_stream(
        image=img,
        mode="Printed",
        raw=True
    )
    operation_id = read_response.headers['Operation-Location'].split('/')[-1]
    while True:
        read_result = computervision_client.get_read_result(operation_id)
        if read_result.status not in ['notStarted', 'running']:
            break
        time.sleep(1)

    # Print the detected text, line by line
    result = []
    if read_result.status == OperationStatusCodes.succeeded:
        for text_result in read_result.analyze_result.read_results:
            for line in text_result.lines:
                print(line.text)
                result.append(line.text)


def recunoastere_text_din_imagine_preprocesata1(img_path):
    image = cv2.imread(img_path)

    # Aplicarea binarizării
    binary_adaptive = binarizare_adaptiva(image)

    img_pil = Image.fromarray(binary_adaptive)
    # Transformarea obiectului de imagine în flux de date
    image_stream = io.BytesIO()
    img_pil.save(image_stream, format='PNG')
    image_stream.seek(0)

    recunoastere_text_aux(image_stream)

    # # Afișarea imaginilor binare
    # cv2.imshow('Binary Adaptive', binary_adaptive)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


def recunoastere_text_din_imagine_preprocesata2(img_path):
    image = cv2.imread(img_path)

    # Aplicarea binarizării
    img_filtrata = bilateral_filter(image, (380, 380))

    img_pil = Image.fromarray(img_filtrata)
    # Transformarea obiectului de imagine în flux de date
    image_stream = io.BytesIO()
    img_pil.save(image_stream, format='PNG')
    image_stream.seek(0)

    recunoastere_text_aux(image_stream)


def recunoastere_text_simpla(img_path):
    img = open(img_path, "rb")
    read_response = computervision_client.read_in_stream(
        image=img,
        mode="Printed",
        raw=True
    )
    operation_id = read_response.headers['Operation-Location'].split('/')[-1]
    while True:
        read_result = computervision_client.get_read_result(operation_id)
        if read_result.status not in ['notStarted', 'running']:
            break
        time.sleep(1)

    if read_result.status == OperationStatusCodes.succeeded:
        for text_result in read_result.analyze_result.read_results:
            for line in text_result.lines:
                print(line.text)


def problema3():
    img_path = "images/test2.png"
    print("Recunoastererea textului din imaginea preprocesata (binarizare adaptiva):")
    recunoastere_text_din_imagine_preprocesata1(img_path)  # imaginea trebuie sa fie PNG
    print()
    print("Recunoasterea textului din imaginea simpla:")
    recunoastere_text_simpla(img_path)

    print("Recunoastererea textului din imaginea preprocesata (bilateral filter + resize):")
    recunoastere_text_din_imagine_preprocesata2(img_path)
    print()
    print("Recunoasterea textului din imaginea simpla:")
    recunoastere_text_simpla(img_path)
