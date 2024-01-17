import nltk
import random

from nltk.corpus import words

class WordGenerator():
    def __init__(self) -> None:
        pass

    def download_content(self):
        try:
            nltk.data.find('corpora/words.zip')
        except LookupError:
            nltk.download('words')

    def generate_word(self):
        word_list = words.words()
        return random.choice(word_list)