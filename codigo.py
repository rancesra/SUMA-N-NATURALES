n = int(input("Escribe el numero: "))

i = 1
suma = 0
while (i<=n):
    suma = suma+i
    i = i+1
    print("i = " +str(i))
    print("La suma es" +str(suma))

print("La suma de los N " +str(n) + " primeros numeros es: " + str(suma))