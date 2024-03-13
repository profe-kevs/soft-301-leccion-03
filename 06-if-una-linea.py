# Condicional doble
# if condicion:
#   sentencias
# else:
#   sentencias

A = int(input("Ingrese el número 01: "))
B = int(input("Ingrese el número 02: "))

# if A > B:
#     M = A
# else:
#     M = B
M = A if A > B else B
print("El mayor es: " + str(M))

# Migrar el programa de pares e impares
A = int(input("Ingrese el valor de A: "))

R = A % 2

# if R == 0:
#     print("Par")
# else:
#     print("Impar")

print("Par") if R == 0 else print("Impar")