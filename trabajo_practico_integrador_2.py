seguir = True

while seguir == True:
    numero_entero = input("Por favor, ingresá un número entero mayor a 0 para iniciar el programa: ")

    if numero_entero.isdigit():
        numero_entero = int(numero_entero)

        if numero_entero != 0:
            frase = input("¡Bienvenido/a!, ingresá una palabra o frase por favor: ")
            caracteres = len(frase)
            print(f"Tu frase o palabra contiene {caracteres} caracteres")

            factorial = 1
            for i in range(1, caracteres + 1):
                factorial = factorial * i

            print(f"El factorial de {caracteres} es: {factorial}")

            if factorial % 2 == 0:
                print("El número es par")
            else:
                print("El número es impar")

        else:
            print("Te pedí que sea mayor a 0. DESAPROBADO .Finalizando el programa...")
            seguir = False

    else:
        print("Ingresaste una dato incorrecto, DESAPROBADO. Finalizando el programa...")
        seguir = False