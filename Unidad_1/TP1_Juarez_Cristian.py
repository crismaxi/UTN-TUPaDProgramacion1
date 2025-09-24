#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Hola Mundo!")


#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado. 
# Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir por pantalla “Hola Marcos!”. 
# Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.

nombre= input("Ingrese su nombre: ")
print(f"Hola {nombre}!")


#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia 
# e imprima por pantalla una oración con los datos ingresados. 
# Por ejemplo: si el usuario ingresa “Marcos”, “Pérez”, “30” y “Argentina”, 
# el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en Argentina”. 
# Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.

nombre= input("Ingrese su nombre: ")
apellido= input("Ingrese su apellido: ")
edad= input("Ingrese su edad: ")
lugar_residencia= input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido} tengo {edad} años y vivo en {lugar_residencia}")


#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.

radio= float(input("Ingrese el radio del circulo: "))
pi= 3.14159
area= float(pi* radio*radio)
perimetro= float (2 * pi * radio)
print("El area del circulo es",area)
print("El perimetro del circulo es",perimetro)


#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.

segundos= float(input("Ingrese la cantidad de segundos: "))
horas= float(segundos / 3600)
print(f"Los segundos ingresados {segundos} equivalen a: {horas} horas")


#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.

numero= int(input("Ingrese un numero: "))

print("La tabla de multiplicar del numero", numero, "es: ")
print(numero, "x 1 =" , int(numero * 1))
print(numero, "x 2 =" , int(numero * 2))
print(numero, "x 3 =" , int(numero * 3))
print(numero, "x 4 =" , int(numero * 4))
print(numero, "x 5 =" , int(numero * 5))
print(numero, "x 6 =" , int(numero * 6))
print(numero, "x 7 =" , int(numero * 7))
print(numero, "x 8 =" , int(numero * 8))
print(numero, "x 9 =" , int(numero * 9))
print(numero, "x 10 =" , int(numero * 10))

#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla 
# el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

numero1=int(input("Ingrese el primer numero entero distinto de cero: "))
numero2=int(input("Ingrese el segundo numero entero distinto de cero: "))
suma= numero1 + numero2
resta = numero1-numero2
multiplicacion= numero1 * numero2
division= float(numero1 / numero2)

print("La suma de ambos numeros es: ", suma)
print("La resta de ambos numeros es: ", resta)
print("La multiplicacion de ambos numeros es: ", multiplicacion)
print("La division de ambos numeros es: ", division)


#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. 
# Tener en cuenta que el índice de masa corporal se calcula del siguiente modo:

altura= float(input("Ingrese su altura en metros: "))
peso= float(input("Ingrese su peso en kg: "))
Imc= float(peso / (altura **altura))
print("El indice de masa corporal es: ",Imc)


#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit. 
# Tener en cuenta la siguiente equivalencia:

celsius= float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit= float(((celsius * 9)/5)+32)
print("La temperatura en grados Fahrenheit es  ",fahrenheit)


#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.

numero1= float(input("Ingrese el 1er numero: "))
numero2= float(input("Ingrese el 2do numero: "))
numero3= float(input("Ingrese el 3er numero: "))
promedio= float ((numero1 + numero2 + numero3) / 3)
print(f"El promedio de {numero1}, {numero2} y {numero3} es: {promedio}")