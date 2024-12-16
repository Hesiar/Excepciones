import math

try:
    x = float(input("Ingrese un número: "))
    assert x >= 0.0
except AssertionError:
    print("El número ingresado debe ser igual o mayor que cero")
    exit(1)

x = math.sqrt(x)

print(x)