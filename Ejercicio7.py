#La oficina de tránsito de Ibagué desea saber, de los n autos que entran a la ciudad 
#de Ibagué, cuantos entran con calcomanía de cada color. Conociendo el ultimo 
#dígito de la placa de cada carro, se puede determinar el color de la calcomanía 
#utilizando la siguiente relación:
# Pedimos al usuario que ingrese el número total de autos
n = int(input("Ingrese el número total de autos: "))

# Creamos un diccionario para almacenar la cantidad de autos por color de calcomanía
calcomanias = {"Amarilla": 0, "Rosa": 0, "Roja": 0, "Verde": 0, "Azul": 0}

# Pedimos al usuario que ingrese el último dígito de la placa de cada auto
for i in range(n):
    ultimo_digito = int(input(f"Ingrese el último dígito de la placa del auto {i+1}: "))

    # Determinamos el color de la calcomanía según el último dígito
    if ultimo_digito in [1, 2]:
        calcomanias["Amarilla"] += 1
    elif ultimo_digito in [3, 4]:
        calcomanias["Rosa"] += 1
    elif ultimo_digito in [5, 6]:
        calcomanias["Roja"] += 1
    elif ultimo_digito in [7, 8]:
        calcomanias["Verde"] += 1
    else:
        calcomanias["Azul"] += 1

# Imprimimos el resultado
print("Cantidad de autos por color de calcomanía:")
print(f"Amarilla: {calcomanias['Amarilla']}")
print(f"Rosa: {calcomanias['Rosa']}")
print(f"Roja: {calcomanias['Roja']}")
print(f"Verde: {calcomanias['Verde']}")
print(f"Azul: {calcomanias['Azul']}")