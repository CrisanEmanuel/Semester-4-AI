"""
Sa se normalizeze informatiile de la problema 1 si 2 folosind diferite metode de normalizare astfel:
    problema 1 - salariul, bonusul, echipa
    problema 2 - valorile pixelilor din imagini
    problema 3 - numarul de aparitii a cuvintelor la nivelul unei propozitii.
"""
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from PIL import Image
from collections import Counter
from nltk import sent_tokenize, word_tokenize


def normalizare_salarii():
    df = pd.read_csv('data/employees.csv')

    # Extract the 'Salary' column as a numpy array
    salaries = df['Salary'].values

    min_salary = np.min(salaries)
    max_salary = np.max(salaries)
    normalized_salaries = (salaries - min_salary) / (max_salary - min_salary)

    # Replace the 'Salary' column in the DataFrame with normalized salaries
    df['Salary'] = normalized_salaries

    plt.hist(normalized_salaries, bins=20, color='#5D6D7E', edgecolor='black')
    plt.title('Normalized Salary Distribution')
    plt.xlabel('Normalized Salary')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()


def normalizare_bonusuri():
    df = pd.read_csv('data/employees.csv')

    # Extract the 'Bonus %' column as a numpy array
    bonuses = df['Bonus %'].values

    # Min-max scaling to normalize bonuses between 0 and 1
    min_bonus = np.min(bonuses)
    max_bonus = np.max(bonuses)
    normalized_bonuses = (bonuses - min_bonus) / (max_bonus - min_bonus)

    # Replace the 'Bonus %' column in the DataFrame with normalized bonuses
    df['Bonus %'] = normalized_bonuses

    plt.hist(normalized_bonuses, bins=20, color='#DC7633', edgecolor='black')
    plt.title('Normalized Bonus Distribution')
    plt.xlabel('Normalized Bonus')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()


def normalizare_echipa():
    # Load the CSV file into a DataFrame
    df = pd.read_csv('data/employees.csv')

    # Perform one-hot encoding on the 'Team' column
    team_encoded = pd.get_dummies(df['Team'])

    # Calculate the sum of each team membership
    team_counts = team_encoded.sum()

    # Min-max scaling to normalize team membership counts between 0 and 1
    min_count = np.min(team_counts)
    max_count = np.max(team_counts)
    normalized_counts = (team_counts - min_count) / (max_count - min_count)

    # Plot a bar chart for normalized team membership counts
    normalized_counts.plot(kind='bar', color='#117A65', edgecolor='black')
    plt.title('Normalized Team Membership Distribution')
    plt.xlabel('Team')
    plt.ylabel('Normalized Frequency')
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.grid(True)
    plt.show()


def normalizare_pixeli(image_paths):
    # Initialize an empty list to store normalized pixel values
    normalized_pixel_values = []

    # Loop through each image path
    for path in image_paths:
        # Read the image
        image = Image.open(path)
        # Convert image to numpy array
        image_array = np.array(image)
        # Normalize pixel values between 0 and 1
        normalized_array = image_array / 255.0
        # Flatten the 3D array to 1D
        flattened_array = normalized_array.flatten()
        # Append normalized pixel values to the list
        normalized_pixel_values.extend(flattened_array)

    # Plot the histogram
    plt.hist(normalized_pixel_values, bins=20, color='#F5CBA7', edgecolor='black')
    plt.title('Normalized Pixel Value Distribution')
    plt.xlabel('Normalized Pixel Value')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()


def normalizare_aparitii_cuvinte(text):
    propozitii = sent_tokenize(text, language='english')
    cuvinte = [word for sent in propozitii for word in word_tokenize(sent, language='english')]

    # Count occurrences of each word
    cuvinte_counts = Counter(cuvinte)

    # Calculate the minimum and maximum word counts
    min_count = min(cuvinte_counts.values())
    max_count = max(cuvinte_counts.values())

    # Min-max scaling to normalize word counts between 0 and 1
    normalized_counts = [(count - min_count) / (max_count - min_count) for count in cuvinte_counts.values()]

    # Plot the histogram2
    plt.hist(normalized_counts, bins=20, color='#5F6A6A', edgecolor='black')
    plt.title('Normalized Word Count Distribution')
    plt.xlabel('Normalized Word Count')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()


def problema4():
    normalizare_salarii()
    normalizare_bonusuri()
    normalizare_echipa()
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
    normalizare_pixeli(cale_imagini)
    with open('data/texts.txt', 'r', encoding='utf-8') as file:
        text = file.read()
        normalizare_aparitii_cuvinte(text)
