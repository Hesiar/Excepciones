
try:
    y = 1 / 0
# Excepción más concreta
except ZeroDivisionError:
    print("No se puede dividir por cero")
# Excepción más abstracta/general
except ArithmeticError:
    print("¡Problema aritmético!")
# Todo lo demás con excepción sin nombre
except:
    print("Algo salió mal")
    
print ("FIN")