# Pedir dos números
# A y B
# un solo igual (=) es asignación


A = int(input("Ingrese el número 01: "))
B = int(input("Ingrese el número 02: "))

if A > B:
    M = A
else:
    M = B

print("El mayor es: " + str(M))
