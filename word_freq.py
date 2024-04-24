#I will use spaCy for stop word removal
import spacy
from collections import Counter
file = open("/word_frequency/random_paragraphs.txt")

text=file.read()

nlp = spacy.load("en_core_web_sm")

stop_words = nlp.Defaults.stop_words
filtered = [word for word in text.split() if word.lower() not in stop_words]

result= Counter(" ".join(filtered).split())
for word, freq in result.items():
    print(f"{word}: {freq}")


