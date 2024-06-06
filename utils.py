def get_user_guess():
    while True:
        guess = input("Adivinhe uma letra: ").strip().lower()
        if len(guess) == 1 and guess.isalpha():
            return guess
        else:
            print("Por favor, insira uma única letra.")
            
def get_game_settings():
    while True:
        try:
            letter_count = int(input("Quantas letras na palavra? "))
            difficulty = input("Escolha a dificuldade (fácil, médio, difícil): ").strip().lower()
            language = input("Escolha o idioma (português, inglês, espanhol): ").strip().lower()
            if letter_count > 0 and difficulty in ["fácil", "médio", "difícil"] and language in ["português", "inglês", "espanhol"]:
                return letter_count, difficulty, language
        except ValueError:
            pass
        print("Entrada inválida. Tente novamente.")
