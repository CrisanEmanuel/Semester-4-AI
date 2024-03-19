from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from msrest.authentication import CognitiveServicesCredentials
import os
import time
from scipy.spatial.distance import hamming
import Levenshtein

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


# returneaza un array cu fiecare linie de text
def recunoastere_text(image_path):
    img = open(image_path, "rb")
    read_response = computervision_client.read_in_stream(
        image=img,
        raw=True
    )
    operation_id = read_response.headers['Operation-Location'].split('/')[-1]
    while True:
        read_result = computervision_client.get_read_result(operation_id)
        if read_result.status not in ['notStarted', 'running']:
            break
        time.sleep(1)

    result = []
    if read_result.status == OperationStatusCodes.succeeded:
        for text_result in read_result.analyze_result.read_results:
            for line in text_result.lines:
                result.append(line.text)
    return result


# Hamming distance
def problema1a_Hamming_Distance(image_path, correct_text):
    array_de_cuvinte_corecte = correct_text.split()
    array_de_text = recunoastere_text(image_path)
    array_de_cuvinte = []
    for linie in array_de_text:
        cuvinte = linie.split()
        for cuv in cuvinte:
            array_de_cuvinte.append(cuv)

    try:
        distance = hamming(array_de_cuvinte, array_de_cuvinte_corecte) * len(array_de_cuvinte_corecte)
        print(f"Hamming distance: {distance}")
        print("Textul a fost recunoscut in proportie de: ", (1 - distance / len(array_de_cuvinte_corecte)) * 100, "%")
    except ValueError as e:
        print(e)


# Levenshtein distance
def problema1b_Levenshtein_Distance(image_path, correct_text):
    recognized_text = recunoastere_text(image_path)
    recognized_text = " ".join(recognized_text)
    distance = Levenshtein.distance(correct_text, recognized_text)
    print(f"Levenshtein distance: {distance}")
    print("Textul a fost recunoscut in proportie de: ", (1 - distance / len(correct_text)) * 100, "%")


# word error rate
def problema1b_WER_Metric(image_path, correct_text):
    correct_words = correct_text.split()
    recognized_text = recunoastere_text(image_path)
    recognized_words = []
    for line in recognized_text:
        words = line.split()
        for word in words:
            recognized_words.append(word)

    # Calculează numărul de substituții, ștergeri și inserții
    S = sum(1 for i, j in zip(correct_words, recognized_words) if i != j)
    D = abs(len(correct_words) - len(recognized_words))
    I = abs(len(recognized_words) - len(correct_words))

    # Calculează Word Error Rate
    WER = (S + D + I) / len(correct_words)
    print("Word Error Rate: ", WER)
    print("Textul a fost recunoscut in proportie de: ", (1 - WER) * 100, "%")


# character error rate
def problema1b_CER_Metric(image_path, correct_text):
    correct_chars = correct_text.replace(" ", "")
    recognized_text = recunoastere_text(image_path)
    recognized_chars = ""
    for linie in recognized_text:
        recognized_chars += linie.replace(" ", "")

    # Calculează numărul de substituții, ștergeri și inserții
    S = sum(1 for i, j in zip(correct_chars, recognized_chars) if i != j)
    D = abs(len(correct_chars) - len(recognized_chars))
    I = abs(len(recognized_chars) - len(correct_chars))

    # Calculează Character Error Rate
    CER = (S + D + I) / len(correct_chars)
    print("Character Error Rate: ", CER)
    print("Textul a fost recunoscut in proportie de: ", (1 - CER) * 100, "%")


def problema1():
    problema1a_Hamming_Distance("images/hammingDistance.png", "The Hamming distance between two "
                                                              "vectors is simply the sum of corresponding elements "
                                                              "that differ between the vectors.")
    problema1b_Levenshtein_Distance("images/test2.png", "Succes in rezolvarea tEMELOR la "
                                                        "LABORAtoarele de Inteligenta Artificiala!")
    problema1b_WER_Metric("images/test4.png", "Exemplu cu scris de tipar. Optical character "
                                              "recognition scris de mana ocr test")
    problema1b_CER_Metric("images/test4.png", "Exemplu cu scris de tipar. Optical character "
                                              "recognition scris de mana ocr test")
