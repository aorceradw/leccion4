total_horas = 0
dias = 6

for dia in range(1, dias + 1):
    horas = float(input(f"Horas día {dia}: "))
    total_horas += horas

precio_hora = float(input("Precio por hora: "))
sueldo = total_horas * precio_hora

print(f"Total horas: {total_horas}")
print(f"Sueldo: {sueldo}€")
