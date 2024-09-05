#Calcular e imprimir la tabla de multiplicar de un número cualquiera, el cual se 
#digitará por teclado. Imprimir el multiplicando, el multiplicador y el producto.

numero = int(input("Ingrese el número para calcular la tabla de multiplicar: "))

# Imprimimos el título de la tabla de multiplicar
print(f"Tabla de multiplicar del {numero}:")
print("Multiplicando | Multiplicador | Producto")

# Calculamos e imprimimos la tabla de multiplicar
for i in range(1, 11):
    producto = numero * i
    print(f"{numero} | {i} | {producto}")