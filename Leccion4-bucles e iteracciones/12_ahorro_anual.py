total_ahorrado = 0
meses = 12

for mes in range(1, meses + 1):
    deposito = float(input(f"Deposito mes {mes}: "))
    total_ahorrado += deposito
    print(f"Total hasta mes {mes}: {total_ahorrado}")

print(f"Total ahorrado en el año: {total_ahorrado}")
