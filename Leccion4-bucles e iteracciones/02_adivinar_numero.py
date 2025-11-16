import random

numero_secreto = random.randint(1, 100)
intentos = 10
adivinado = False

while intentos > 0 and not adivinado:
    intento = int(input(f"Adivina (intentos: {intentos}): "))
    
    if intento == numero_secreto:
        print(f"¡Correcto! Lo adivinaste en {11 - intentos} intentos")
        adivinado = True
    elif intento < numero_secreto:
        print("El número es mayor")
    else:
        print("El número es menor")
    
    intentos -= 1

if not adivinado:
    print(f"Game Over. El número era {numero_secreto}")
