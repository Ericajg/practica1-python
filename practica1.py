import random 
numero_secreto = random.randint (1, 80)
intento = 0
print("-"*41)
print ("BIENVENIDOS AL JUEGO DE ADIVINA EL NUMERO")
print("-"*41)
while intento < 5: 

    numero = (input("ingrese un numero del 1 al 80: ")) 
    if numero.isdigit():
        if int(numero) >0 and int(numero) <81:
        
            if int(numero) == numero_secreto:
                print("tu numero es correcto ganasteeee!! promoción directa atte: Gabi")
                break
        
            elif  int(numero) < numero_secreto:
                intento = intento+1
                print  ("El número es mayor. Te quedan: ",5-intento,"intentos")
            elif  int(numero) > numero_secreto:
                intento = intento+1
                print  ("El número es menor. Te quedan: ",5-intento,"intentos")
        
        else:
            print("Fuera de rango")
                
        
    else:
        print("Ingresa un NUMEROOO, infeliz")  

if intento==5:
    print ("<<<<<| PERDISTE, otra vez será!!! |>>>>>")
    print("-"*40)
    print ("       El numero secreto es:",numero_secreto )
    print("-"*40)