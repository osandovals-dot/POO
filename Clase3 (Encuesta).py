#Autor: Oscar Sandoval


#actividad encuesta:
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

actividad2()