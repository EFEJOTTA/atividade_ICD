import utils

class Jogo_da_forca:
    def __init__(self, word):
        self.word = word
        self.guesses = []
        self.max_attempts = 6
        self.attempts_left = self.max_attempts

