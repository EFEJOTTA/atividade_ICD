import utils

class Jogo_da_forca:
    def __init__(self, word):
        self.word = word
        self.guesses = []
        self.max_attempts = 6
        self.attempts_left = self.max_attempts

    def display_word(self):
        display = ''.join([letter if letter in self.guesses else '_' for letter in self.word])
        print(f"Palavra: {display}")


