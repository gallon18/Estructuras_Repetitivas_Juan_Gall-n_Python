# Pedir los datos de los alumnos, estos son: sexo, edad y altura. Al final del programa 
#se deberá mostrar la cantidad de hombres, la cantidad de mujeres, la altura promedio 
#la cantidad de alumnos que tienen una altura mayor a 1.70 cm, la cantidad de alumnos 
#que tiene una altura menor o igual a 1.50 cm. El programa debe finalizar cuando la edad 
# sea igual a 0hombres = 0  
hombres = 0
mujeres = 0
altura_total = 0
alumnos_altura_mayor_170 = 0
alumnos_altura_menor_150 = 0
contador_alumnos = 0

# Bucle para pedir datos de los alumnos
while True:
    sexo = input("Ingrese el sexo del alumno (H/M): ")
    edad = int(input("Ingrese la edad del alumno: "))
    altura = float(input("Ingrese la altura del alumno en cm: "))

    # Verificamos si el usuario quiere salir del programa
    if edad == 0:
        break

    # Contamos hombres y mujeres
    if sexo.upper() == "H":
        hombres += 1
    elif sexo.upper() == "M":
        mujeres += 1

    # Sumamos la altura total
    altura_total += altura

    # Contamos alumnos con altura mayor a 1.70 cm
    if altura > 170:
        alumnos_altura_mayor_170 += 1

    # Contamos alumnos con altura menor o igual a 1.50 cm
    if altura <= 150:
        alumnos_altura_menor_150 += 1

    # Incrementamos el contador de alumnos
    contador_alumnos += 1

# Calculamos la altura promedio
altura_promedio = altura_total / contador_alumnos

# Mostramos los resultados
print("Cantidad de hombres:", hombres)
print("Cantidad de mujeres:", mujeres)
print("Altura promedio:", altura_promedio)
print("Cantidad de alumnos con altura mayor a 1.70 cm:", alumnos_altura_mayor_170)
print("Cantidad de alumnos con altura menor o igual a 1.50 cm:", alumnos_altura_menor_150)