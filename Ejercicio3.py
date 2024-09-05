#Suponga que se tiene un conjunto de calificaciones de un grupo de 20 alumnos. 
#Realizar un algoritmo para calcular el promedio y la calificación más alta y más baja 
#de todo el grupo.
promedio = 0
calificacionMasAlta = 0
calificacionMasBaja = 100

# Pedimos al usuario que ingrese las calificaciones de los 20 alumnos
for i in range(20):
    calificacion = float(input(f"Ingrese la calificación del alumno {i+1}: "))

    # Verificamos si la calificación es válida (entre 0 y 100)
    while calificacion < 0 or calificacion > 100:
        print("Error: La calificación debe estar entre 0 y 100.")
        calificacion = float(input(f"Ingrese la calificación del alumno {i+1}: "))

    # Sumamos la calificación al promedio
    promedio += calificacion

    # Verificamos si la calificación es la más alta o la más baja
    if calificacion > calificacionMasAlta:
        calificacionMasAlta = calificacion
    elif calificacion < calificacionMasBaja:
        calificacionMasBaja = calificacion

# Calculamos el promedio
promedio /= 20

# Imprimimos los resultados
print(f"Promedio: {promedio:.2f}")
print(f"Calificación más alta: {calificacionMasAlta}")
print(f"Calificación más baja: {calificacionMasBaja}")