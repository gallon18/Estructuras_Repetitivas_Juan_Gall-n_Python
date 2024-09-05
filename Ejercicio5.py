#Una persona debe realizar un muestreo con 50 personas para determinar el 
#promedio de peso de los niños, jóvenes, adultos y ancianos que existen en su zona. 
#Las categorías se determinar de acuerdo a la siguiente tabla:
# Creamos un diccionario para almacenar los pesos y edades de las personas
personas = {}

# Pedimos al usuario que ingrese la edad y peso de cada persona
for i in range(50):
    edad = int(input(f"Ingrese la edad de la persona {i+1}: "))
    peso = float(input(f"Ingrese el peso de la persona {i+1}: "))
    personas[i] = {"edad": edad, "peso": peso}

# Creamos un diccionario para almacenar los promedios de peso por categoría
promedios = {"niños": 0, "jóvenes": 0, "adultos": 0, "ancianos": 0}
conteos = {"niños": 0, "jóvenes": 0, "adultos": 0, "ancianos": 0}

# Calculamos el promedio de peso por categoría
for persona in personas.values():
    if 0 <= persona["edad"] <= 12:
        promedios["niños"] += persona["peso"]
        conteos["niños"] += 1
    elif 13 <= persona["edad"] <= 29:
        promedios["jóvenes"] += persona["peso"]
        conteos["jóvenes"] += 1
    elif 30 <= persona["edad"] <= 59:
        promedios["adultos"] += persona["peso"]
        conteos["adultos"] += 1
    else:
        promedios["ancianos"] += persona["peso"]
        conteos["ancianos"] += 1

# Calculamos el promedio de peso para cada categoría
for categoria in promedios.keys():
    if conteos[categoria] > 0:
        promedios[categoria] /= conteos[categoria]

# Imprimimos los promedios de peso por categoría
print("Promedios de peso por categoría:")
print(f"Niños: {promedios['niños']:.2f} kg")
print(f"Jóvenes: {promedios['jóvenes']:.2f} kg")
print(f"Adultos: {promedios['adultos']:.2f} kg")
print(f"Ancianos: {promedios['ancianos']:.2f} kg")