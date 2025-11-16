n_trabajadores = int(input("Trabajadores: "))

total_empresa = 0
precio_hora = float(input("Precio por hora: "))

for trabajador in range(1, n_trabajadores + 1):
    horas = float(input(f"Horas trabajador {trabajador}: "))
    sueldo = horas * precio_hora
    total_empresa += sueldo
    print(f"Trabajador {trabajador}: {sueldo}€")

print(f"Total empresa: {total_empresa}€")
