"""
Crear una funcion que ingrese por teclado un valor numérico, y presente por pantalla
si este valor es impar o par

"""

def par_e_impar(a):
    if a%2 == 0:
        print("Es par")
    else:
        print("Es impar")

a = int(input("Ingrese un valor numérico: "))
par_e_impar(a)