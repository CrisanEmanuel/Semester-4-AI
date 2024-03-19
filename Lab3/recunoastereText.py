from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from msrest.authentication import CognitiveServicesCredentials
import os
from PIL import Image
import time
import cv2
from pytesseract import pytesseract, Output
import pytesseract

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


# exemplul de pe github de la profa
def recunoastere_text(image_path):
    img = open(image_path, "rb")
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
    print()


# character, left, bottom, right, top, page
# So for each character you get the character, followed by its bounding box characters, followed by the 0-based page number.
def coordonate_pentru_fiecare_litera_din_text(image_path):
    imge = Image.open(image_path)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    data = pytesseract.image_to_boxes(imge)
    print(data)


def localizare_text_cu_confidence_level(image_path):
    args = {"image": image_path,
            "min_conf": 0}

    images = cv2.imread(args["image"])
    rgb = cv2.cvtColor(images, cv2.COLOR_BGR2RGB)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    results = pytesseract.image_to_data(rgb, output_type=Output.DICT)

    # Then loop over each of the individual text
    # localizations
    for i in range(0, len(results["text"])):

        # We can then extract the bounding box coordinates
        # of the text region from  the current result
        x = results["left"][i]
        y = results["top"][i]
        w = results["width"][i]
        h = results["height"][i]

        # We will also extract the OCR text itself along
        # with the confidence of the text localization
        text = results["text"][i]
        conf = int(results["conf"][i])

        characters = list(text)

        characters_confidence = [conf] * len(
            characters)  # Assuming the confidence is the same for all characters in a word

        for char, char_conf in zip(characters, characters_confidence):
            print(f"Character: {char}, Confidence: {char_conf}")

        # filter out weak confidence text localizations
        if conf > args["min_conf"]:
            # We will display the confidence and text to
            # our terminal
            print("Confidence: {}".format(conf))
            print("Text: {}".format(text))
            print("")

            # We then strip out non-ASCII text,so we can
            # draw the text on the image We will be using
            # OpenCV, then draw a bounding box around the
            # text along with the text itself
            text = "".join(text).strip()
            cv2.rectangle(images,
                          (x, y),
                          (x + w, y + h),
                          (0, 76, 153), 2)
            cv2.putText(images,
                        text,
                        (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1.2, (0, 153, 76), 3)

            # After all, we will show the output image
    cv2.imshow("Image", images)
    cv2.waitKey(0)


def test():
    # recunoastere_text("images/test3.png")
    localizare_text_cu_confidence_level("images/test4.png")
