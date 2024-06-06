import api
import game
import utils

def main():
    letter_count, difficulty, language = utils.get_game_settings()
    word = api.get_word_from_api(letter_count, difficulty, language)
    
    hangman_game = game.HangmanGame(word)
    hangman_game.play()

if __name__ == "__main__":
    main()
