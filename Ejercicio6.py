#Calcular la cantidad de hombres y mujeres presentes en un salón de clases con un 
#total de n personas
# Pedimos al usuario que ingrese el número total de personas
n = int(input("Ingrese el número total de personas: "))

# Creamos un diccionario para almacenar el género de cada persona
personas = {}

# Pedimos al usuario que ingrese el género de cada persona (H para hombre, M para mujer)
for i in range(n):
    genero = input(f"Ingrese el género de la persona {i+1} (H/M): ").upper()
    while genero not in ["H", "M"]:
        genero = input(f"Ingrese el género de la persona {i+1} (H/M): ").upper()
    personas[i] = genero

# Contamos el número de hombres y mujeres
hombres = sum(1 for genero in personas.values() if genero == "H")
mujeres = sum(1 for genero in personas.values() if genero == "M")

# Imprimimos el resultado
print(f"La cantidad de hombres es: {hombres}")
print(f"La cantidad de mujeres es: {mujeres}")