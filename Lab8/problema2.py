import markovify
from datasets import load_dataset
from textblob import TextBlob

def run2ab():
    # Load the dataset
    dataset = load_dataset("biglam/gutenberg-poetry-corpus")
    # Access the data
    poetry_data = dataset['train']
    # Combine all poems into one string
    all_poems = " ".join(poem['line'] for poem in poetry_data)
    # Cream un model Markov
    text_model = markovify.Text(all_poems)

    # Generăm o strofă de poezie
    generated_poem = ''
    for _ in range(4):  # Presupunând că o strofă are 4 versuri
        line = text_model.make_sentence()
        print(line)
        generated_poem += line + '\n'

    print()
    # Calculam emotia poeziei
    blop = TextBlob(generated_poem)
    sentiment = blop.sentiment
    print(f"Sentiment: {sentiment}")

