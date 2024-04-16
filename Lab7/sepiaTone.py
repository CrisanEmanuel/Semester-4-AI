import os
from PIL import Image

# takes an image path and applies sepia to the image
def sepia(image_path: str) -> Image:
    img = Image.open(image_path)
    width, height = img.size

    pixels = img.load()  # create the pixel map

    for py in range(height):
        for px in range(width):
            r, g, b = img.getpixel((px, py))

            tr = int(0.393 * r + 0.769 * g + 0.189 * b)
            tg = int(0.349 * r + 0.686 * g + 0.168 * b)
            tb = int(0.272 * r + 0.534 * g + 0.131 * b)

            if tr > 255:
                tr = 255

            if tg > 255:
                tg = 255

            if tb > 255:
                tb = 255

            pixels[px, py] = (tr, tg, tb)

    return img


# takes the input folder and applies sepia to all images in the folder
# saves the sepia images to the output folder
def apply_sepia_to_folder(input_folder: str, output_folder: str):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            input_image_path = os.path.join(input_folder, filename)
            sepia_image = sepia(input_image_path)
            output_image_path = os.path.join(output_folder, "sepia_" + filename)
            sepia_image.save(output_image_path)
