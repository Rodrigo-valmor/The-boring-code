from ast import If
import random


def run():

    numero_Aleatorio = random.randint(1,100)
    num_insert = int(input("Inserte un número del 1 al 100: "))
    score = 1
    life = 5

    while num_insert != numero_Aleatorio:
        if num_insert < numero_Aleatorio and life > 0:
            print("\nTe QUEDAN " + str(life) + " vidas" +"\nEscoge un numero mayor\n")
            score += 1  
            life -=1 
            num_insert = int(input("\nInserte un número: "))

        elif num_insert < numero_Aleatorio and life > 0:
            print("\nTe quedan " + str(life) + " vidas" +"\nEscoge un numero menor\n")
            score +=1
            num_insert = int(input("\nInserte un número: "))
            life -=1 
        else:
            if life <= 0:
               print("\nGame over\n")
               break
            
            else:
                print("¡¡Felicidades ganaste!!! tus intentos fueron: " + str(score))
                score +=1
                break

 
if __name__ == "__main__":
    run()