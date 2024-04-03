#codigo que halla el maximo comun divisor de dos numeros

def mcd(a, b):
    while b:
        a, b = b, a % b
    return a


# Solicitar al usuario que ingrese ambos números
while True:
    try:
        num1 = int(input("Ingrese el primer número: "))
        if num1 < 0:
            raise ValueError("Por favor, ingrese un número positivo.")

        num2 = int(input("Ingrese el segundo número: "))
        if num2 < 0:
            raise ValueError("Por favor, ingrese un número positivo.")

        break  # Salir del bucle si ambos números son positivos
    except ValueError as e:
        print(e)

# Calcular y mostrar el máximo común divisor
print("El máximo común divisor de", num1, "y", num2, "es:", mcd(num1, num2))




