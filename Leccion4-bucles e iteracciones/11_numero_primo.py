import math

numero = int(input("Número: "))

if numero < 2:
    print("No es primo")
else:
    es_primo = True
    raiz = int(math.sqrt(numero))
    
    for i in range(2, raiz + 1):
        if numero % i == 0:
            es_primo = False
            break
    
    if es_primo:
        print("Es primo")
    else:
        print("No es primo")
