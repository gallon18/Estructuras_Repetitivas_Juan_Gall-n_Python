# Ejercicio: Leer 10 números negativos y convertirlos a positivos e imprimir la suma de dichos números

# Inicializamos la variable para almacenar la suma de los números positivos
sumaPositivos = 0

# Pedimos al usuario que ingrese 10 números negativos
for i in range(10):
    numeroNegativo = float(input(f"Ingrese el número negativo {i+1}: "))

    # Verificamos si el número es negativo
    while numeroNegativo >= 0:
        print("Error: El número debe ser negativo.")
        numeroNegativo = float(input(f"Ingrese el número negativo {i+1}: "))

    # Convertimos el número negativo a positivo
    numeroPositivo = abs(numeroNegativo)

    # Sumamos el número positivo a la suma total
    sumaPositivos += numeroPositivo

# Imprimimos la suma de los números positivos
print(f"La suma de los números positivos es: {sumaPositivos}")