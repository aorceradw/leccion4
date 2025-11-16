# Lección 3: Bucles e Iteraciones en Python

Ángela Orcera Ruiz (1º DAW - Entornos de Desarrollo)

---

## Cómo He Hecho los Ejercicios

He resuelto 20 ejercicios de bucles e iteraciones siguiendo un patrón de diseño claro y consistente. Cada ejercicio practica conceptos fundamentales como el uso de bucles `for` y `while`, condiciones lógicas y acumuladores.

### El Patrón que He Seguido

Para que todos los ejercicios fueran claros y estructurados, he seguido siempre el mismo esquema:

1. **Pido los Datos (Entrada):** Uso `input()` o defino variables iniciales según lo que el ejercicio necesite.

2. **Proceso:** Aquí es donde utilizo bucles y lógica condicional para transformar los datos y realizar los cálculos.

3. **Printeo (Salida):** El resultado final siempre lo enseño con `print()` o múltiples prints según sea necesario.

4. **Validación:** Solo valido datos cuando es imprescindible para que el programa funcione correctamente.

---

## Los 20 Ejercicios: Grupos y Concepto Clave

Los ejercicios están organizados en bloques que van aumentando en complejidad. Aquí te explico cómo los he agrupado y qué se supone que estoy practicando en cada uno.

| Grupo | Ejercicios | El Foco Principal |
|---|---|---|
| 1 al 5 | Bucles Básicos | Primeros pasos con `for` y `while`: iterar números, contar caracteres, repetir acciones simples. |
| 6 al 10 | Bucles con Condiciones | Combinación de bucles con `if/elif/else`: filtrar números, multiplicaciones, operadores módulo. |
| 11 al 15 | Bucles Anidados y Acumuladores | Dos bucles dentro de otro, contadores y acumuladores: primos, pagos mensuales, sueldos. |
| 16 al 20 | Aplicación Compleja | Bucles anidados avanzados, validación de datos y control de flujo: empleados, cronómetro, menús. |

---

## La Estructura General que He Usado

Esta es la plantilla que he seguido para la mayoría de ejercicios:

```python
# Ejercicio N: Descripción del ejercicio

# 1. Entrada de datos (si la necesita)
variable = input("Pídeme algo: ")
# o simplemente definir valores iniciales

# 2. Proceso con bucle
for elemento in rango:
    # Lógica aquí
    pass

while condicion:
    # Más lógica
    pass

# 3. Salida
print(f"Resultado final: {resultado}")
```

---

## Resumen de Ejercicios

| # | Nombre del Ejercicio | Concepto Clave | Tipo de Bucle | ¿Entrada? |
|---|---|---|---|---|
| 1 | Factorial | Multiplicación iterada | for | Sí |
| 2 | Adivinar Número | Bucle while con condición | while | Sí |
| 3 | Suma y Media | Acumulador con while | while | Sí |
| 4 | Positivos, Negativos, Ceros | Contadores múltiples | for | Sí |
| 5 | Vocales | String y condición en while | while | Sí |
| 6 | Números Pares | Filtro con módulo | for | Sí |
| 7 | Tabla Multiplicar | Tabla de un número | for | Sí |
| 8 | Números Intervalo | Validación y acumuladores | while | Sí |
| 9 | Potencia | Bucle como alternativa a ** | for | Sí |
| 10 | Tablas Multiplicar | Bucles anidados | for | No |
| 11 | Número Primo | Lógica con raíz cuadrada | for | Sí |
| 12 | Ahorro Anual | Acumulador en bucle | for | Sí |
| 13 | Sueldo Semanal | Bucle para sumar horas | for | Sí |
| 14 | Encuentro Coches | Simulación con while | while | No |
| 15 | Pagos Mensuales | Acumulador con multiplicación | for | No |
| 16 | Sueldos Empleados | Bucles anidados, cálculos | for | Sí |
| 17 | Sueldos por Días | Bucles triples anidados | for | Sí |
| 18 | Cronómetro | Control de tiempo con time | while | Sí |
| 19 | Menú | Bucle infinito con break | while | Sí |
| 20 | N Números Primos | Búsqueda iterativa | while | Sí |

---

## Desglose por Conceptos

### Bucles FOR (Iteración determinada)
Ejercicios: 1, 4, 6, 7, 9, 10, 12, 13, 16, 17

El bucle `for` lo utilizas cuando **sabes de antemano cuántas veces tienes que iterar**. Ejemplos:
- Repetir 12 meses (ejercicio 12)
- Recorrer un rango de números (ejercicio 6)
- Iterar sobre trabajadores (ejercicio 16)

### Bucles WHILE (Iteración indeterminada)
Ejercicios: 2, 3, 5, 8, 14, 18, 19, 20

El bucle `while` lo utilizas cuando **no sabes cuántas iteraciones necesitas** o cuando depende de una condición externa. Ejemplos:
- Adivinar un número hasta acertarlo (ejercicio 2)
- Leer números hasta que el usuario ingrese 0 (ejercicio 3)
- Un menú que se repite hasta que el usuario salga (ejercicio 19)

### Bucles Anidados
Ejercicios: 10, 16, 17

Cuando un bucle está dentro de otro, la combinación es poderosa:
- Tabla de multiplicar del 1 al 5 (ejercicio 10)
- Para cada trabajador, sumar horas de cada día (ejercicio 17)

### Acumuladores
Ejercicios: 3, 8, 12, 13, 15, 16, 17

Un acumulador es una variable que suma o multiplica valores a lo largo del bucle:
```python
total = 0
for i in range(10):
    total += i  # Acumulamos
```

---

## Conclusión Rápida

La clave de estos ejercicios es entender:

1. **Cuándo usar `for`:** Cuando sabes el número de iteraciones.
2. **Cuándo usar `while`:** Cuando la condición de parada depende de algo variable.
3. **Cómo anidar bucles:** Para problemas que requieren "bucles dentro de bucles".
4. **Acumuladores:** Para sumar, contar o multiplicar valores durante la iteración.

Con estos 20 ejercicios, dominas los bucles básicos y puedes pasar a estructuras más complejas como listas, diccionarios y funciones.
