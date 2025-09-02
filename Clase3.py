#Autor: Oscar Sandoval

#Version para probar funcion de commit en github
#ejercicio 1: Ingresar valor de compra y el programa devuelve un descuento

def actividad1():
    valordecompra = int(input("Que valor tiene la compra?: "))
    descuento1 = (valordecompra/100)*5
    descuento2 = (valordecompra/100)*10
    descuento3 = (valordecompra/100)*15

    if (valordecompra >= 50000) and (valordecompra < 90000):
        print(f"Su compra cuenta con un descuento de {descuento1}, queda con un valor de {(valordecompra-descuento1)}")
    elif(valordecompra >= 90000) and (valordecompra < 100000):
        print(f"Su compra cuenta con un descuento de {descuento2}, queda con un valor de {(valordecompra-descuento2)}")
    elif(valordecompra >= 100000):
        print(f"Su compra cuenta con un descuento de {descuento3}, queda con un valor de {(valordecompra-descuento3)}")
    else:
        print(f"Su compra tiene un valor de {valordecompra}")

#ejercicio 2: hacer una encuesta con: nombre, carrera, idea de proyecto

def actividad2():
    nombres = ["oscar"]
    carreras = []
    ideas = []
    for n in range (6):
        nombre = str(input("¿Cual es tu nombre?: "))
        carrera = str(input("¿Que carrera estas estudiando?: "))
        ideadeproyecto = str(input("¿Cual es tu idea de proyecto?: "))
        nombres.append(nombre)
        carreras.append(carrera)
        ideas.append(ideadeproyecto)
    

    for i in range (6):
        print(f"Encuestado {i}:")
        print("Nombre del enmcuestado: " + nombres[i])
        print("Carrera que esta estudiando: " + carreras[i])
        print("Idea de proyecto" + ideas[i])
