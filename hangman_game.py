from curses.ascii import isalpha
import random

def get_work():
    """
    Toma y guarda una palabra aleatoria del archivo data.txt
    
    retorna una palabra en mayuscula y sin espacios.
    """
    with open('./files/data.txt', 'r', encoding='utf-8') as f:
        DATA = [i for i in f ]
    word = random.choice(DATA)
    return word.upper().strip()
    


# def hangman_game(word):
   

def run():
    print("""

                                                       HANGMAN GAME 

    Welcome to the hangman game. 

    You have to guess the word to win  

    Good look !!!!!   😆😆😆

    """)
    word = get_work()
    print(word)
    print(len(word))
    # hangman_game(word)
    # while input('Want to play again Y/N: ').upper() == 'Y':
    #      word = get_work()
    #      hangman_game(word)


if __name__ == '__main__':
    run()
