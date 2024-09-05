#un grupo de 23 estudiantes presentan un examen de algoritmia. Hacer un 
#algoritmo que lea por cada estudiante la calificación obtenida. Al finalizar calcule e 
#imprima:
# La cantidad de estudiantes que obtuvieron una calificación menor a 50. 
# La cantidad de estudiantes que obtuvieron una calificación de 50 o más pero 
#menor que 70.
# La cantidad de estudiantes que obtuvieron una calificación de 70 o más pero 
#menor que 80. 
# La cantidad de estudiantes que obtuvieron una calificación de 80 o más.
#La calificación obtenida en el examen de algoritmia debe ser entre 1 y 100
n = 23

# Creamos variables para contar la cantidad de estudiantes en cada rango de calificación
menor_50 = 0
entre_50_70 = 0
entre_70_80 = 0
mayor_80 = 0

# Pedimos al usuario que ingrese la calificación de cada estudiante
for i in range(n):
    calificacion = int(input(f"Ingrese la calificación del estudiante {i+1} (entre 1 y 100): "))
    while calificacion < 1 or calificacion > 100:
        calificacion = int(input(f"Ingrese la calificación del estudiante {i+1} (entre 1 y 100): "))

    # Contamos la cantidad de estudiantes en cada rango de calificación
    if calificacion < 50:
        menor_50 += 1
    elif calificacion < 70:
        entre_50_70 += 1
    elif calificacion < 80:
        entre_70_80 += 1
    else:
        mayor_80 += 1

# Imprimimos el resultado
print("Cantidad de estudiantes por rango de calificación:")
print(f"Menor a 50: {menor_50}")
print(f"Entre 50 y 70: {entre_50_70}")
print(f"Entre 70 y 80: {entre_70_80}")
print(f"Mayor a 80: {mayor_80}")