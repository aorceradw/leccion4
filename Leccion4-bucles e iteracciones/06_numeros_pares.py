inicio = int(input("Inicio: "))
fin = int(input("Fin: "))

for num in range(inicio, fin + 1):
    if num % 2 == 0:
        print(num)
