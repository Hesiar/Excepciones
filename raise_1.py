def mal_asunto(n):
    raise ZeroDivisionError

try:
    mal_asunto(0)
except ArithmeticError:
    print("¿Qué ha pasado?")
    
print("EN-FIN")