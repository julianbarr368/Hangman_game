from curses.ascii import isalpha
import random

def get_work():
    """
    Toma y guarda una palabra aleatoria del archivo data.txt
    
    retorna una palabra en mayuscula
    """
    with open('./files/data.txt', 'r', encoding='utf-8') as f:
        DATA = [i for i in f ]

    word = random.choice(DATA)
    return word.upper()


def hangman_game(word):
    guess_word = '_' * len(word) - 1 
    guessed = False
    guessed_letter = []
    guessed_words =[]
    tries = 6
    print(guess_word)
    while guessed == False and tries >0:
        user = input('Please guess a letter of the word: ').upper()
        if len(user) == 1 and user.isalpha():
            if user in guessed_letter:
                print('your already guess the letter ', user)
            elif user not in word:
                print(user, ' is not in the word')
                tries -= 1
                guessed_letter.appent(user)
            else:
                print('Good job ', user , 'is in the word')
                guessed_letter.appent(user)
                word_in_list = list(guess_word)
                indices = [i for i, letter in enumerate(word) if letter == user]
                for index in indices:
                    word_in_list[index] = user
                guess_word = ''.join(word_in_list)
                if'_' not in guess_word:
                    guessed = True
        elif len(user) == len(word) and user.isalpha():
            if user in guess_word:
                print('You already guess the word: ', user)
            elif user != word:
                print(user,' Is not the word.')
                tries -= 1
                guessed_words.append(user)
            else:
                guessed= True
                guess_word = word                     
        else:
            print('please enter a letter')
        print(guess_word)
    if guessed:
        print('Congrats, you guess the word, you win!!!')
    else:
        print('Sorry, you raw out of try. The word was: ' + word + 'Try again...')

def run():
    print("""

                                                       HANGMAN GAME 

    Welcome to the hangman game. 

    You have to guess the word to win  

    Good look !!!!!   😆😆😆

    """)
    word = get_work()
    hangman_game(word)
    while input('Want to play again Y/N').upper() == 'Y':
         word = get_work()
         hangman_game(word)


if __name__ == '__main__':
    run()
