pos1 = 70
pos2 = 150
velocidad = 1

encontrados = False

while not encontrados:
    pos1 -= velocidad
    pos2 += velocidad
    
    if pos1 >= pos2:
        km_encuentro = (pos1 + pos2) / 2
        print(f"Se encuentran en km {km_encuentro}")
        encontrados = True
