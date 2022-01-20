from ast import Num, Pass
from lib2to3.pgen2.token import MINUS
import random

MAYUS = ("A","B","C","D","E","F","G")
MINUS = ("h","i","j","k","l","m","n")
SIMBO = ("!","#","$","%","&","/","(",")")
NUM   = ("1","2","3","4","5","6","7","8","9","0")

CARACTERES = MAYUS + MINUS + SIMBO + NUM 

def generate_pass():
    
    generator = []
    for i in range(0,14):
        caracter_random = random.choice(CARACTERES)
        generator.append(caracter_random)

        password = "".join(generator)   
    
    return print("Tu contraseña es: " + password)



def run():
    
    generate_pass()




if __name__ == '__main__':
    run()