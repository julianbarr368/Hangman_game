import random
import os


def get_work():
    """
    Toma y guarda una palabra aleatoria del archivo data.txt
    
    retorna una palabra en mayuscula y sin espacios.
    """
    with open('./files/data.txt', 'r', encoding='utf-8') as f:
        DATA = [i for i in f ]
    word = random.choice(DATA)
    return word.upper().strip()


def hangman_game(word):
    chosen_word_list = [letter for letter in word] # se crea una lista de la palabra.
    chosen_word_list_underscore = [' _ '] * len(chosen_word_list) # se crea lista para mostrar despues como _ _ _ ...
    letter_index_dict = {}
    for idx, letter in enumerate(word):
        if not letter_index_dict.get(letter):
            letter_index_dict[letter] = []
        letter_index_dict[letter].append(idx) # Se crea un diccionario que contiene como llaves las letra de la palabra y como valor el indice.

    while True:
        os.system('clear')  
        print("""

                                                       HANGMAN GAME 

        Welcome to the hangman game. 

        You have to guess the word to win  

        Good look !!!!!   😆😆😆

        """)
        for element in chosen_word_list_underscore:
            print('word: ' element, end= '')  # sirve para imprimir los _ de forma horizontal
        print("\n")

        letter = input('Enter a letter: ').upper().strip()
        assert letter.isalpha(), 'you can only enter a letter, please (❁´◡`❁)'

        if letter in chosen_word_list:
            for idx in letter_index_dict[letter]:
                chosen_word_list_underscore[idx] = letter # Se remplaza la posicion de la letra si es correcta
        
        if ' _ ' not in chosen_word_list_underscore:
            os.system('clear')
            print('Congratulations you win, the word was: ', word)
            break

     
def run():
    
    
    word = get_work()
    hangman_game(word)
    while input('Want to play again Y/N: ').upper() == 'Y':
         word = get_work()
         hangman_game(word)


if __name__ == '__main__':
    run()
