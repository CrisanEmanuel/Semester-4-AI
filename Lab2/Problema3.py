"""
  Se da un fisier care contine un text (format din mai multe propozitii) in limba romana -
a se vedea fisierul ”data/texts.txt”. Se cere sa se determine si sa se vizualizeze:
    1) numarul de propozitii din text;
    2) numarul de cuvinte din text
    3) numarul de cuvinte diferite din text
    4) cel mai scurt si cel mai lung cuvant (cuvinte)
    5) textul fara diacritice
    6) sinonimele celui mai lung cuvant din text
"""
import re
from nltk.corpus import wordnet


def numar_propozitii(text):
    propozitii = re.split(r'(?<=[.!?])(?:\s|\n)+', text)
    return len(propozitii)


def numa_cuvinte(text):
    cuvinte = re.findall(r'\b\w+\b', text)
    return len(cuvinte)


def numar_cuvinte_diferite(text):
    cuvinte = re.findall(r'\b\w+\b', text)
    return len(set(cuvinte))


def cel_mai_scurt_cuvant(text):
    cuvinte = re.findall(r'\b\w+\b', text)
    return min(cuvinte, key=len)


def cel_mai_lung_cuvant(text):
    cuvinte = re.findall(r'\b\w+\b', text)
    return max(cuvinte, key=len)


def text_fara_diacritice(text):
    text = text.replace('ă', 'a')
    text = text.replace('â', 'a')
    text = text.replace('î', 'i')
    text = text.replace('ș', 's')
    text = text.replace('ț', 't')
    return text


def sinonimele_celui_mai_lung_cuvant(cuvant):
    sinonime = set()
    for synset in wordnet.synsets(cuvant):
        for lemma in synset.lemmas():
            sinonime.add(lemma.name())
    return list(sinonime)


def problema3():
    print("Problema 3")
    with open('data/texts.txt', 'r', encoding='utf-8') as file:
        text = file.read()
        print(f"Numarul de propozitii din text este: {numar_propozitii(text)}")
        print(f"Numarul de cuvinte din text este: {numa_cuvinte(text)}")
        print(f"Numarul de cuvinte diferite din text este: {numar_cuvinte_diferite(text)}")
        print(f"Cel mai scurt cuvant din text este: {cel_mai_scurt_cuvant(text)}")
        print(f"Cel mai lung cuvant din text este: {cel_mai_lung_cuvant(text)}")
        print()
        print(f"Textul fara diacritice este:\n{text_fara_diacritice(text)}")
        print()
        print(f"Sinonimele celui mai lung cuvant din text sunt: {sinonimele_celui_mai_lung_cuvant(cel_mai_lung_cuvant(text))}")
