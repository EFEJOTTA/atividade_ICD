def get_user_guess():
    while True:
        guess = input("Adivinhe uma letra: ").strip().lower()
        if len(guess) == 1 and guess.isalpha():
            return guess
        else:
            print("Por favor, insira uma única letra.")
            

