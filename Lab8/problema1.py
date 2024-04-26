import random
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction


def create_markov_chain(corpus, order=1):
    words = corpus.split()
    markov_chain = {}
    for i in range(len(words) - order):
        current_state = tuple(words[i:i+order])
        next_word = words[i+order]
        if current_state not in markov_chain:
            markov_chain[current_state] = []
        markov_chain[current_state].append(next_word)
    return markov_chain

def generate_text(markov_chain, length=50):
    current_state = random.choice(list(markov_chain.keys()))
    text = list(current_state)

    for _ in range(length):
        next_word = random.choice(markov_chain[current_state])
        text.append(next_word)
        current_state = tuple(text[-len(current_state):])

    return ' '.join(text)

def run1a():
    # Citim corpusul din fișier
    with open("data/corpus_complet.txt", "r", encoding="utf-8") as file:
        corpus = file.read()

    # Creăm lanțul Markov
    markov_chain = create_markov_chain(corpus, order=1)

    # Generăm un text folosind lanțul Markov
    generated_text = generate_text(markov_chain, length=200)

    words = generated_text.split()
    for i in range(0, len(words), 8):
        print(' '.join(words[i:i+8]))

    # Calculăm scorul BLEU
    with open("data/lucefarul.txt", "r", encoding="utf-8") as file:
        reference_text = file.read()

    reference_poem = reference_text.split()
    generated_poem = generated_text.split()
    smoothie = SmoothingFunction().method4
    bleu_score = sentence_bleu([reference_poem], generated_poem, smoothing_function=smoothie)
    print(f"BLEU Score: {bleu_score}")
