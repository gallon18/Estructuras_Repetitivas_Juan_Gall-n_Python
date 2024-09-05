#Calcular el promedio de edades de hombres, mujeres y de todo un grupo de alumnos.
# Pedimos al usuario que ingrese la cantidad total de alumnos
n = int(input("Ingrese el número total de alumnos: "))

# Creamos variables para almacenar las edades y géneros de los alumnos
edades_hombres = []
edades_mujeres = []
edades_grupo = []

# Pedimos al usuario que ingrese la edad y género de cada alumno
for i in range(n):
    edad = int(input(f"Ingrese la edad del alumno {i+1}: "))
    genero = input(f"Ingrese el género del alumno {i+1} (Hombre/Mujer): ")

    # Almacenamos las edades según el género
    if genero.upper() == "HOMBRE":
        edades_hombres.append(edad)
    elif genero.upper() == "MUJER":
        edades_mujeres.append(edad)

    # Almacenamos la edad en la lista del grupo completo
    edades_grupo.append(edad)

# Calculamos el promedio de edades para cada grupo
promedio_hombres = sum(edades_hombres) / len(edades_hombres) if edades_hombres else 0
promedio_mujeres = sum(edades_mujeres) / len(edades_mujeres) if edades_mujeres else 0
promedio_grupo = sum(edades_grupo) / len(edades_grupo)

# Imprimimos el resultado
print("Promedios de edades:")
print(f"Hombres: {promedio_hombres:.2f}")
print(f"Mujeres: {promedio_mujeres:.2f}")
print(f"Grupo completo: {promedio_grupo:.2f}")