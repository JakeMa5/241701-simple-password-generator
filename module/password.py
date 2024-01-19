
import random

class Password:
    def __init__(self, word_generator) -> None:
        self.word_generator = word_generator

    def generate(self) -> str:
        words = self.get_words()
        number = self.get_number()
        return str(str(words) + str(number))

    def get_words(self) -> str:
        word1 = self.word_generator.generate_word().capitalize()
        word2 = self.word_generator.generate_word().capitalize()
        return str(str(word1) + str(word2))
    
    def get_number(self) -> int:
        return random.randint(10, 99)