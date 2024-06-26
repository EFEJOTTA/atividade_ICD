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

    def make_guess(self, guess):
        if guess in self.guesses:
            print("Você já adivinhou essa letra.")
            return
        
        self.guesses.append(guess)
        
        if guess not in self.word:
            self.attempts_left -= 1
            print(f"Errado! Tentativas restantes: {self.attempts_left}")
        else:
            print("Correto!")

    def is_won(self):
        return all(letter in self.guesses for letter in self.word)

    def is_lost(self):
        return self.attempts_left <= 0

    def play(self):
        while not self.is_won() and not self.is_lost():
            self.display_word()
            guess = utils.get_user_guess()
            self.make_guess(guess)
        
        if self.is_won():
            print(f"Parabéns! Você acertou a palavra! A palavra era '{self.word}'.")
        else:
            print(f"Você errou a palavra! A palavra era '{self.word}'.")
