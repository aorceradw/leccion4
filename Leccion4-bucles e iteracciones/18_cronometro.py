import time

while True:
    horas = int(input("Horas (0-23): "))
    minutos = int(input("Minutos (0-59): "))
    segundos = int(input("Segundos (0-59): "))
    
    if horas < 0 or horas > 23 or minutos < 0 or minutos > 59 or segundos < 0 or segundos > 59:
        print("Valores inválidos")
        continue
    
    while True:
        print(f"{horas:02d}:{minutos:02d}:{segundos:02d}")
        time.sleep(1)
        
        segundos += 1
        if segundos == 60:
            segundos = 0
            minutos += 1
            if minutos == 60:
                minutos = 0
                horas += 1
                if horas == 24:
                    horas = 0
