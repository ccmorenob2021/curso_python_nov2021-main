"""def mi_funcion():
    print("Hola mundo desde una función")

def nombre(a,b):
    print("Hola " + a, b + " espero que estes bien")

mi_funcion()
nombre("Diego","Saavedra")
nombre("Yomara","Fernandez")
nombre("Victoria","Saavedra")

frase=mi_funcion()
print(frase)



def resta(a,b):
    return a - b

print(resta(25, 5))
print(resta(b=25, a=5))
"""

def multiplicación(a=None,b=None):
    if a == None or b == None:
        print("Por favor ingresar valores para realizar la operación")
        return
    return a * b

multiplicación()

def indeterminados_posicion(*args):
    for arg in args:
        print(arg)

indeterminados_posicion(5,"Hola", [1,2,4])

def indeterminados_posicion(**kwargs):
    print(kwargs)

indeterminados_posicion(a=5,b="Hola",c=[1,2,4])
#indeterminados_posicion()