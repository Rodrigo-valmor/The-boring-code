import random
import os
import re 
import string

def choose_word():
    """Extrae cualquier palabra al azar de data.txt

        Args:
            none
        return:
            palabra al azar de data.txt: string
    """
    utf_8 = 'áéíóú'
    vowels = 'aeiou'
    word_list = []
    with open('./files/data.txt','r',encoding='utf-8') as f:
        for line in f:
            word_list.append(str.rstrip(line))
    word= random.choice(word_list)
    for i in range(len(utf_8)):
        word = word.replace(utf_8[i],vowels[i])


    return word
 
def normalize(input_user):
    """ Compara si las entradas del jugador son correctas, filtra números y signos 

        args: 
            input_user: str
        return:
            si la entrada es correcta: input_user en minuscula (str)
            si hay dos entradas: mensaje(str)
            si la entrada no es una letra:  ValueError 
    """
    LYRICS_OK  = [index for index in string.ascii_letters] + ['á', 'é', 'í', 'ó','ú','Á','É','Í','Ó','Ú','Ñ','ñ']
    INPUTS = []
    for index in LYRICS_OK: 
        INPUTS.append(index)
    try:

        if input_user in INPUTS:
            input_user = input_user.lower()
            return input_user
        raise ValueError ('Solo puedes ingresar letras')
    except ValueError as ve:
        return ve
HANGMAN_IMG = ['''

   +---+
   |   |
       |
       |
       |
       |

=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

 

def run ():

    #game start
    word = choose_word()
    os.system('clear')
    underscore = ["_ "]*len(word)
    word_for_underscore = word
    life = 0
      
    #game control
   
    while life < len(HANGMAN_IMG) :
         
        print(HANGMAN_IMG[life])
        print('\033[1mRecuerda que las palabras no llevan tilde \n \033[0m')
        print( "".join(underscore))
        input_user = input('Ingresa una letra: ')
        input_user = normalize(input_user)
        try:
            index = word.find(input_user)
            if input_user == word[index]:
                    for i in re.finditer(input_user,word_for_underscore):
                        underscore[i.start():i.end()] = i.group()
                    for i in range(1):
                        word = word.replace(input_user[i],"")
                        os.system('clear')
            elif input_user != word[index]:
                    os.system('clear')
                    life += 1
        except:
                os.system('clear')
                print(input_user)
        if  life == (len(HANGMAN_IMG) - 1):
            os.system('clear')
            print(HANGMAN_IMG[6])
            print("\033[1m Game over !!\033[0m")
            print('La palabra era ' + word_for_underscore)
            break
        elif word == '' and life <= len(HANGMAN_IMG):
            os.system('clear')
            print("\033[1m Felicidades Ganaste !!\033[0m")
            break


if __name__ == '__main__':
    run()