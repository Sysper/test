def funfactorial(n):
    if n == 0:
        return 1
    else:
        return n * funfactorial(n - 1)

numero = int(input("Ingresa un número entero mayor a cero: "))

if numero < 0:
    print("El número no es mayor a cero.")

else:
    factorial = funfactorial(numero)
    print(f"El factorial de {numero} es {factorial}")
