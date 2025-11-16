import math

cantidad = int(input("Cuántos números primos: "))

primos_encontrados = 0
numero = 2

while primos_encontrados < cantidad:
    es_primo = True
    raiz = int(math.sqrt(numero))
    
    for i in range(2, raiz + 1):
        if numero % i == 0:
            es_primo = False
            break
    
    if es_primo:
        print(numero)
        primos_encontrados += 1
    
    numero += 1
