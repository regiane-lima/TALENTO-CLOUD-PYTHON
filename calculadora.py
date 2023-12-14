def calculadora(num1, num2, operador):
    if operador == 1:
        return num1 + num2
    elif operador == 2:
        return num1 - num2
    elif operador == 3:
        return num1 * num2
    elif operador == 4:
        return num1 / num2
    else:
        return 0

resultado = calculadora(5, 6, 7)
print(resultado)
