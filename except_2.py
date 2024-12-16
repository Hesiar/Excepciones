
try:
    y = 1 / 0
# Excepción más concreta
except (ZeroDivisionError, ArithmeticError):
    print("Hubo un problema al hacer la operación")
# Excepción más abstracta/general
except:
    print("Algo salió mal")
    
print ("FIN")