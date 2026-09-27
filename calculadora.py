print("hola, bienvenido a la calculadora")

num1 = float(input("Dame el primer numero: "))
num2 = float(input("Dame el segundo: "))

print("\nElige: +  -  *  /")
operacion = input("Que operación quieres hacer?: ")

if operacion == "+":
    resultado = num1 + num2
elif operacion == "-":
    resultado = num1 - num2
elif operacion == "*":
    resultado = num1 * num2
elif operacion == "/":
    resultado = num1 / num2
else:
    resultado = "operación no válida"

print("Resultado:", resultado)