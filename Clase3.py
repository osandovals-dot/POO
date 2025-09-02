#Autor: Oscar Sandoval


#ejercicio 1: Ingresar valor de compra y el programa devuelve un descuento

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