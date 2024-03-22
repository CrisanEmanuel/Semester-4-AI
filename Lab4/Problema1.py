"""
Sa se foloseasca un algoritm de clasificare a imaginilor (etapa de inferenta/testare) si sa se stabileasca
performanta acestui algoritm de clasificare binara (imagini cu biciclete vs. imagini fara biciclete).
"""
from io import BytesIO
from sklearn.metrics import accuracy_score, precision_score, recall_score

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials
import os


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


# evalueaza functia de detectare a bicicletelor
def evalClassification(realLabels, computedLabels, labelNames):
    acc = accuracy_score(realLabels, computedLabels)
    precision = precision_score(realLabels, computedLabels, average=None, labels=labelNames)
    recall = recall_score(realLabels, computedLabels, average=None, labels=labelNames)
    return acc, precision, recall


def detect_bicycle(image_path):
    # Specify the features we want to extract from the image (in this case, only objects)
    features = [VisualFeatureTypes.objects]

    # Perform object detection on the image
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()
    detected_objects = computervision_client.analyze_image_in_stream(BytesIO(image_data), visual_features=features)

    # Check if "bicycle" is in the list of detected objects
    for obj in detected_objects.objects:
        if 'bicycle' in obj.object_property:
            return True

    return False


# returneaza pathurile imaginilor din folderul dat ca parametru
def images_path(folder_path):
    image_extensions = ['.jpg']
    image_files = []

    for file in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, file)):
            if any(file.lower().endswith(ext) for ext in image_extensions):
                image_files.append(os.path.join(folder_path, file))

    return image_files


def problema1():
    img_path = images_path('images')

    real_labels = []
    for i in range(0, 20):
        if i < 10:
            real_labels.append(True)
        else:
            real_labels.append(False)

    computed_labels = []
    for img in img_path:
        if detect_bicycle(img):
            computed_labels.append(True)
        else:
            computed_labels.append(False)

    acc, precision, recall = evalClassification(real_labels, computed_labels, [True, False])
    print('acc: ', acc, ' precision: ', precision, ' recall: ', recall)
