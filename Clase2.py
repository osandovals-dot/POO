#Autor Oscar Sandoval
#primera version

#1. Estructuras de control

#Prueba
#Estructure un programa que mencione si su calificion es meritoria

Nota = float(input("Escriba en forma numerica su nota (0/5): "))

if(Nota>=4.5):
    print("Su nota es meritoria")
else:
    print("Su nota no es meritoria")

#Hacer 6 ejercicios de practica

#Escribir un programa en Java que lea un número entero desde teclado y realiza la suma de los 100 número siguientes, mostrando el resultado en pantalla. 

Numero = int(input("Escriba un numero entero de forma numerica: "))

InicioIntervalo = Numero + 1
FinIntervalo = Numero + 101

for i in range (InicioIntervalo, FinIntervalo):
     Numero = Numero + i
print (Numero)

#Escribir un programa en Java que calcule el área de un rectángulo del cual se le proporcionará por el teclado su altura y anchura (números decimales).

Alto = float(input("Escriba la altura del área en forma numerica (use el . para poner los decimales): "))
Ancho = float(input("Escriba el ancho del área en forma numerica (use el . para poner los decimales): "))

AreaTotal = Alto*Ancho
print (AreaTotal)