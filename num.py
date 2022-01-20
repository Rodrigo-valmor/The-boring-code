def es_primo(numero):
    contador = 0 
    
    for i in range(1, numero + 1):
        
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
            contador += 1
        
    if contador == 0:
        print("El valor es primo")
    else:
         print("El valor no es primo" )


def run():
    numeroPrim = input("Ingrese el valor: ")

    es_primo(int(numeroPrim))
    

if __name__ == "__main__":
    run()