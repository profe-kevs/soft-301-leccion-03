PV = float(input("Ingrese Precio de venta"))
print("Ingrese 'N' para Nacional o 'E' para extranjero")
OPCION = input()
if OPCION == "N":
    TOTAL = PV + (PV * .08)
else:
    TOTAL = PV + (PV * .18)

print("El total es: "+ str(TOTAL))