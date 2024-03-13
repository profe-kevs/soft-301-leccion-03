A = int(input("Ingrese el valor de A: "))
B = int(input("Ingrese el valor de B: "))
C = int(input("Ingrese el valor de C: "))

if A > B:
	if A > C:
		M = A
	else:
		M = C
else:
	if B > C:
		M = B
	else:
		M = C

print(M)