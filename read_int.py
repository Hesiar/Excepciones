def read_int(prompt, min, max):
    while True:
        try:
            value = int(input(prompt))
            if min <= value <= max:
                return value
            else:
                raise ValueError
        except ValueError:
            print("No es un numero valido. Pruebe otra vez.")
            

v = read_int("Ingresa un número entre -10 a 10: ", -10, 10)

print("El número es:", v)