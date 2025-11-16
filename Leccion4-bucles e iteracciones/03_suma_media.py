suma = 0
cantidad = 0

while True:
    numero = int(input("Número (0 para terminar): "))
    if numero == 0:
        break
    suma += numero
    cantidad += 1

if cantidad > 0:
    media = suma / cantidad
    print(f"Suma: {suma}")
    print(f"Media: {media}")
else:
    print("No hay números")
