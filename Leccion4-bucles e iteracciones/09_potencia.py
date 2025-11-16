base = float(input("Base: "))
exponente = int(input("Exponente: "))

resultado = 1

for i in range(exponente):
    resultado *= base

print(f"{base}^{exponente} = {resultado}")
