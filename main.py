#codigo que halla el maximo comun divisor de dos numeros

def mcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Solicitar al usuario que ingrese el primer número
while True:
    try:
        num1 = int(input("Ingrese el primer número: "))
        break  # Salir del bucle si la conversión a entero es exitosa
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

# Solicitar al usuario que ingrese el segundo número
while True:
    try:
        num2 = int(input("Ingrese el segundo número: "))
        break  # Salir del bucle si la conversión a entero es exitosa
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

# Calcular y mostrar el máximo común divisor
print("El máximo común divisor de", num1, "y", num2, "es:", mcd(num1, num2))



