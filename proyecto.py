def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

print("Operaciones disponibles:")
print("1. Suma")
print("2. Resta")

opcion = input("Elige una opción (1/2): ")

num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

if opcion == "1":
    print(f"La suma de {num1} + {num2} es: {suma(num1, num2)}")
elif opcion == "2":
    print(f"La resta de {num1} - {num2} es: {resta(num1, num2)}")
else:
    print("Opción no válida. Por favor, elige 1 o 2.")

