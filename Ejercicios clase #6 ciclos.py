#Ejercicios clase #6 ciclos

#Punto 1

a= int(input("#1: "))
b= int(input("#2: "))
contador=0
resultado = 0
if a < 0 and b > 0:
    signo = -1
elif a > 0 and b < 0:
    signo = -1
elif a < 0 and b < 0:
    signo = 1

if a < 0:
    a = -a
if b < 0:
    b = -b

while contador < a:
    resultado += b
    contador += 1


print(f"Resultado final: {resultado}")

#Punto 2

cantidad = int(input("¿Cuántas notas vas a ingresar? "))

suma = 0
contador = 0

while contador < cantidad:
    nota = float(input(f"Ingrese la nota #{contador + 1} (entre 0 y 5): "))
    
    if nota < 0 or nota > 5:
        print("Nota inválida. Debe estar entre 0 y 5.")
        continue  # No cuenta esta nota, vuelve a pedirla
    
    suma += nota
    contador += 1

promedio = suma / cantidad
print(f"El promedio de las notas es: {promedio:.2f}")

#punto 3

n = int(input("Ingrese el valor de n (hasta dónde se eleva): "))
x = int(input("Ingrese el valor de x (el exponente): "))

i = 0
while i <= n:
    potencia = i ** x
    print(f"{i}^{x} = {potencia}")
    i += 1

#punto 4

N = int(input("Ingrese un número N: "))

suma = 0
numero = 1

while numero <= N:
    if numero % 2 != 0:  # Si es impar
        suma += numero
    numero += 1

print(f"La suma de los números impares entre 1 y {N} es: {suma}")

#punto 5

continuar = "s"

while continuar.lower() == "s":
    numero = int(input("Ingrese un número entre 0 y 20: "))

    if numero < 0 or numero > 20:
        print("Número fuera de rango. Intente de nuevo.")
        continue

    factorial = 1
    contador = 1

    while contador <= numero:
        factorial *= contador
        contador += 1

    print(f"El factorial de {numero} es: {factorial}")

    continuar = input("¿Desea calcular otro factorial? (s/n): ")

#punto 6

n = int(input("Ingrese el número hasta donde desea sumar: "))

suma = 0
contador = 1

while contador <= n:
    suma += contador
    contador += 1

print(f"La sumatoria de 1 hasta {n} es: {suma}")













    

