# Ejercicio 1: Leer 20 números e imprimir cuantos son positivos, cuantos negativos y cuantos neutros

# Inicializamos las variables para contar los números positivos, negativos y neutros
positivos = 0
negativos = 0
neutros = 0

# Pedimos al usuario que ingrese 20 números
for i in range(20):
    numero = float(input(f"Ingrese el número {i+1}: "))

    # Verificamos si el número es positivo, negativo o neutro
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    else:
        neutros += 1

# Imprimimos los resultados
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")
print(f"Neutros: {neutros}")