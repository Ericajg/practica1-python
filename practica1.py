import random 

numero_secreto = random.randint(1, 99)
intento = 0

print("-"*41 + "\nBIENVENIDOS AL JUEGO DE ADIVINA EL NUMERO\n" + "-"*41 + "\n")
nombre = input("\nIngresa nombre Jugador:\n")

while intento < 5:
    numero = input("\nIngrese un numero del 1 al 99:\n")

    if not numero.isdigit():
        print("\nError!.\nEl valor ingresado no es un numero.\nIntenta de nuevo...\n")

    else:
        numero = int(numero)
 
        if numero == numero_secreto:
            print("\nFelicitaciones "+ nombre +"!.\nGanasteeee!!\nAcertaste el numero\nPromocion directa atte: Gabi\n┌∩┐(◣_◢)┌∩┐")
            break
 
        elif numero < numero_secreto:
            intento += 1
            print("\nEl numero secreto es mayor.\nTe quedan:", 5 - intento, "intentos\n")
 
        elif numero > numero_secreto:
            intento += 1
            print("\nEl numero secreto es menor.\nTe quedan:", 5 - intento, "intentos\n")
 
        else:
            print("\nNumero fuera de rango.\nIntenta nuevamente...\n")

if intento == 5:
    print("\n(--)| -PERDISTE- |(--)\n"+"-"*25+"\n"+"El numero secreto era: " + str(numero_secreto)+"\n"+"-"*25)



