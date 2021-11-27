"""
Crear un menú interactivo por consola
que me brinde las siguientes opciones.
1) Calcular si un número es par o impar
2) Calcular la edad del usuario
3) Salir

Tome en cuenta cuando el usuario no ingrese un valor válido
muestre un mensaje diferente
"""

def calculo_edad():
    nombre = input("Ingrese su nombre :")
    anio = int(input("Ingrese su año de nacimiento: "))
    if (anio < 2022):
        edad = 2021 - anio
        print ("Hola {nom} tu edad es {ed} años".format(nom=nombre,ed=edad))
    else:
        print("Aun no naces")

def par_impar(a):
    if (a%2==0):
           print("El numero {num} es par".format(num=a))
    else:
        print("El numero {num} es impar".format(num=a))

 

print("Bienvenido al menu interactivo")
while True:
    print ("""
    Que quieres hacer? escriba una opcion
    1) Calcular si un numero es par o impar
    2) Calcular la edad del usuario
    3) Salir
    """)
    opcion = input()
    if opcion=='1':
        numero1= int(input("Ingrese numero:"))
        par_impar(numero1)
    elif opcion == '2':
        calculo_edad()
    elif opcion== '3':
        break
    else:
        print("Comando desconocido, vuelve a intentarlo")