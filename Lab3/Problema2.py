import pytesseract
import cv2
from pytesseract import Output


# IoU metric
# cu cat IoU este mai mare, cu atat localizarea este mai buna
def bb_intersection_over_union(boxA, boxB):
    # determine the (x, y) - coordinates of the intersection rectangle
    xA = max(boxA[0], boxB[0])
    yA = max(boxA[1], boxB[1])
    xB = min(boxA[2], boxB[2])
    yB = min(boxA[3], boxB[3])
    # compute the area of intersection rectangle
    interArea = max(0, xB - xA + 1) * max(0, yB - yA + 1)
    # compute the area of both the prediction and ground-truth
    # rectangles
    boxAArea = (boxA[2] - boxA[0] + 1) * (boxA[3] - boxA[1] + 1)
    boxBArea = (boxB[2] - boxB[0] + 1) * (boxB[3] - boxB[1] + 1)
    # compute the intersection over union by taking the intersection
    # area and dividing it by the sum of prediction + ground-truth
    # areas - the interesection area
    iou = interArea / float(boxAArea + boxBArea - interArea)
    # return the intersection over union value
    return iou


def calculare_calitate_localizare_cu_IoU(image_path):
    coordonate_detectate = coordonate_cuvinte_din_text(image_path)
    coordonate_corecte = {"Pentru": (80, 76, 160, 90),
                          "LOCALIZARE!": (169, 74, 320, 95)}

    for cuvant in coordonate_detectate.keys():
        if cuvant in coordonate_corecte:
            coordonate_cuv_detectate = coordonate_detectate[cuvant]
            coordonate_cuv_corecte = coordonate_corecte[cuvant]
            iou = bb_intersection_over_union(coordonate_cuv_detectate, coordonate_cuv_corecte)

            print(f"IOU pentru cuvantul: {cuvant}: {iou}")
        else:
            print(f"Cuvantul {cuvant} nu a fost gasit.")


def coordonate_cuvinte_din_text(image_path):
    args = {"image": image_path,
            "min_conf": 0}
    images = cv2.imread(args["image"])
    rgb = cv2.cvtColor(images, cv2.COLOR_BGR2RGB)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    results = pytesseract.image_to_data(rgb, output_type=Output.DICT)
    cuvant_plus_coordonate = {}
    for i in range(0, len(results["text"])):

        # We can then extract the bounding box coordinates
        # of the text region from  the current result
        x1 = results["left"][i]
        y1 = results["top"][i]
        x2 = results["width"][i]
        y2 = results["height"][i]

        # We will also extract the OCR text itself along
        # with the confidence of the text localization
        text = results["text"][i]
        conf = int(results["conf"][i])

        # filter out weak confidence text localizations
        if conf > args["min_conf"]:
            cuvant_plus_coordonate[text] = (x1, y1, x1 + x2, y1 + y2)  # (stanga, sus, dreapta, jos)
    # for key, value in cuvant_plus_coordonate.items():
    #     print(f"{key}: {value}")
    return cuvant_plus_coordonate


def problema2():
    calculare_calitate_localizare_cu_IoU("images/pentruLocalizare.png")
