total_pagado = 0
pago_mensual = 10

for mes in range(1, 21):
    total_pagado += pago_mensual
    print(f"Mes {mes}: {pago_mensual}€ - Total: {total_pagado}€")
    pago_mensual *= 2

print(f"Total pagado en 20 meses: {total_pagado}€")
