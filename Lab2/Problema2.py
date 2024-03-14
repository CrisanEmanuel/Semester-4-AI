"""
Se dau mai multe imagini (salvate in folder-ul "data/images"). Se cere:
    1) sa se vizualizeze una din imagini
    2) daca imaginile nu aceeasi dimensiune, sa se redimensioneze toate la 128 x 128 pixeli si sa se vizualizeze imaginile intr-un cadru tabelar.
    3) sa se transforme imaginile in format gray-levels si sa se vizualizeze
    4) sa se blureze o imagine si sa se afiseze in format "before-after"
    5) sa se identifice muchiile intr-o imagine si sa se afiseze in format "before-after"
"""
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from PIL import Image, ImageFilter


def vizualizare_imagine():
    image_path = "data/images/BERT.png"
    img = mpimg.imread(image_path)
    plt.imshow(img)
    plt.axis('off')
    plt.show()


def redimensionare(cale_imagini):
    imagini_redimensionate = []
    for cale in cale_imagini:
        img = Image.open(cale)
        img = img.resize((128, 128))
        imagini_redimensionate.append(img)

    numar_imagini = len(cale_imagini)
    numar_randuri = int(np.ceil(numar_imagini / 3))
    numar_coloane = min(numar_imagini, 3)

    fig, axs = plt.subplots(numar_randuri, numar_coloane, figsize=(10, 10))

    for i, img in enumerate(imagini_redimensionate):
        rind = i // numar_coloane
        coloana = i % numar_coloane
        axs[rind, coloana].imshow(img)
        axs[rind, coloana].axis('off')

    for i in range(numar_imagini, numar_randuri * numar_coloane):
        rind = i // numar_coloane
        coloana = i % numar_coloane
        axs[rind, coloana].axis('off')

    plt.tight_layout()
    plt.show()


def convertire_gray_levels(cale_imagini):
    for cale in cale_imagini:
        img = Image.open(cale)
        img = img.convert('L')
        img.save(cale)
        print(f"Converted {cale} to grayscale")


def blur_and_display(image_path):
    blur_radius = 5
    original_image = Image.open(image_path)
    blurred_image = original_image.filter(ImageFilter.GaussianBlur(blur_radius))
    fig, axs = plt.subplots(1, 2, figsize=(10, 10))
    axs[0].imshow(original_image)
    axs[0].axis('off')
    axs[0].set_title('Original')
    axs[1].imshow(blurred_image)
    axs[1].axis('off')
    axs[1].set_title('Blurred')
    plt.show()


def muchii_si_afisare(image_path):
    original_image = Image.open(image_path)
    edges = original_image.filter(ImageFilter.FIND_EDGES)
    fig, axs = plt.subplots(1, 2, figsize=(10, 10))
    axs[0].imshow(original_image)
    axs[0].axis('off')
    axs[0].set_title('Original')
    axs[1].imshow(edges)
    axs[1].axis('off')
    axs[1].set_title('Edges')
    plt.show()


def problema2():
    print("Problema 2")
    vizualizare_imagine()
    cale_img1 = "data/images/BERT.png"
    cale_img2 = "data/images/chatGPT.png"
    cale_img3 = "data/images/diffusionModel.jpg"
    cale_img4 = "data/images/Karpaty.jpg"
    cale_img5 = "data/images/LeCun.jpg"
    cale_img6 = "data/images/Leskovec.jpg"
    cale_img7 = "data/images/Norvig.jpg"
    cale_img8 = "data/images/Russell.jpg"
    cale_img9 = "data/images/Turing.webp"
    cale_img10 = "data/images/YOLO.jpg"
    cale_img11 = "data/images/Altman.webp"
    cale_img12 = "data/images/Ng.webp"
    cale_imagini = [cale_img1, cale_img2, cale_img3, cale_img4, cale_img5, cale_img6, cale_img7, cale_img8, cale_img9,
                    cale_img10, cale_img11, cale_img12]
    redimensionare(cale_imagini)
    convertire_gray_levels(cale_imagini)
    blur_and_display(cale_img5)
    muchii_si_afisare(cale_img12)
