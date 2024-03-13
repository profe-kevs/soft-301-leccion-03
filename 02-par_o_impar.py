# +   suma
# -   resta
# /   división
# //  división entera 
# %   módulo o residuo
# 3 % 2 == 1

A = int(input("Ingrese el valor de A: "))

R = A % 2

if R == 0:
    print("Par")
else:
    print("Impar")