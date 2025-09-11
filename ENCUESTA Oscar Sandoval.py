#Autor Oscar Sandoval

#Encuesta:

class encuesta:
        turnos=[]
        nombres=[]
        edades=[]
        ideas=[]
        def __init__(self,nombre, edad, idea_proyecto):
            
            self.nombre = nombre
            self.edad = edad
            self.idea_proyecto = idea_proyecto

        def guardar_datos(self):
            self.nombres.append(self.nombre)
            self.edades.append(self.edad)
            self.ideas.append(self.idea_proyecto)
        
        @classmethod
        def mostrar_datos(cls):
            print("\n--- RESULTADOS DE LA ENCUESTA ---")
            for i in range(len(cls.nombres)):
                print(f"   Nombre: {cls.nombres[i]}")
                print(f"   Edad: {cls.edades[i]}")
                print(f"   Idea: {cls.ideas[i]}")

            

x=0
while x == 0:


    opcion = int(input("Tiene las siguientes opciones: \n1. añadir encuestado\n2. terminar formulario\nElija la opción: "))


    while opcion < 1 or opcion > 2:
        opcion = int(input("OPCION NO VÁLIDA\nTiene las siguientes opciones: \n1. añadir encuestado\n2. terminar formulario\nElija la opción: "))
    if opcion == 1:
        nombre = input("¿Cual es tu nombre?: ")
        edad = input("¿Que edad tienes?: ")
        idea_proyecto = input("Cuentame acerca de tu idea de proyecto: ")

        persona=encuesta(nombre,edad,idea_proyecto)
        encuesta.guardar_datos()
    elif opcion == 2:
        print("Resultados encusta:")
        encuesta.mostrar_datos()
        print("\n\n\n\nEncuesta finalizada.")
        break









