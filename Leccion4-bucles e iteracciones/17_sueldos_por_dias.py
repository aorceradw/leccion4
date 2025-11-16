n_trabajadores = int(input("Trabajadores: "))

total_empresa = 0
precio_hora = float(input("Precio por hora: "))
dias_semana = 6

for trabajador in range(1, n_trabajadores + 1):
    total_horas = 0
    
    for dia in range(1, dias_semana + 1):
        horas = float(input(f"Trabajador {trabajador} día {dia}: "))
        total_horas += horas
    
    sueldo = total_horas * precio_hora
    total_empresa += sueldo
    print(f"Trabajador {trabajador}: {sueldo}€")

print(f"Total empresa: {total_empresa}€")
