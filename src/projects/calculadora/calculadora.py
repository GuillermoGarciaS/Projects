# aqui declaro mis valores y al mismo tiempo imprimo los mensajes y hago que se guarden ahi mismo

numero1 = int(input("Ingresa tu primer numero:"))
numero2 = int(input("Ingresa el segundo numero:"))

# la unica que no imprime un mensaje es eleccion, ya que en esta solo guardare que tipo de operacion
# es la que el usuario va a escoger

eleccion = 0

# aqui le doy al usuario a escoger entre varias opcciones, hago uso de while para que en caso de que
# este quiera salirse, solo tenga que usar 6, y este por consecuente acabe el programa

while eleccion != 6:
    print(""" Indique la operacion que desea usar
         |1| Suma
         |2| Resta
         |3| Multiplicacion
         |4| Division              
         |5| Cambio de valores
         |6| Salir
         """)
    
# aqui realizo las operaciones matemáticas usando varios if's

    eleccion = int(input())

    if eleccion == 1:
        print(" ")
        print("Resultado: ", numero1, " + ", numero2, " = ", numero1+numero2)
    if eleccion == 2:
        print(" ")
        print("Resultado: ", numero1, " - ", numero2, " = ", numero1-numero2)
    if eleccion == 3:
        print(" ")
        print("Resultado: ", numero1, " * ", numero2, " = ", numero1*numero2)
    if eleccion == 4:
        print(" ")
        print("Resultado: ", numero1, " / ", numero2, " = ", numero1/numero2)

# en caso de que el usuario desee cambiar los valores, usaremos otro if, volviendo a repetir las mismas preguntas

    if eleccion == 5:
       numero1 = int(input("Ingresa tu primer numero:"))
       numero2 = int(input("Ingresa el segundo numero:"))