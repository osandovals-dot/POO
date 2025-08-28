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

#Escriba un programa que lea tres números enteros positivos, y que calcule e imprima en pantalla el menor y el mayor de todos ellos.

Numero1 = int(input("Escriba el primer numero entero en forma numerica: "))
Numero2 = int(input("Escriba el segundo numero entero en forma numerica: "))
Numero3 = int(input("Escriba el tercer numero entero en forma numerica: "))

if Numero1 > Numero2:
    if(Numero1 > Numero3):
        print(f"El numero {Numero1} es el mayor")
    else:
        print(f"El numero {Numero3} es el mayor")
if Numero2 > Numero1:
    if (Numero2 > Numero3):
        print(f"El numero {Numero2} es el mayor")
    else:
        print(f"El numero {Numero3} es el mayor")

#Escribir un programa en Java que lea un número entero por el teclado e imprima todos los número impares menores que él.

NumeroIntervalo = int(input("Ingrese un numero del 1 al 10: "))

for r in range (0,10):
    if r%2:
        print(r)
        if r == NumeroIntervalo:
            pass
    else:
        pass
