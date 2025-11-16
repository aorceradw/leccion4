while True:
    inf = int(input("Límite inferior: "))
    sup = int(input("Límite superior: "))
    
    if inf < sup:
        break
    print("El inferior debe ser menor que el superior")

suma = 0
fuera = 0
igual_limite = False

while True:
    numero = int(input("Número (0 para terminar): "))
    
    if numero == 0:
        break
    
    if numero == inf or numero == sup:
        igual_limite = True
    elif inf < numero < sup:
        suma += numero
    else:
        fuera += 1

print(f"Suma dentro: {suma}")
print(f"Fuera: {fuera}")
print(f"Igual a límite: {igual_limite}")
