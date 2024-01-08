def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero."

def menu():
    print("1: Soma")
    print("2: Subtração")
    print("3: Multiplicação")
    print("4: Divisão")
    print("0: Sair")

def main():
    while True:
        menu()
        escolha = input("Digite o número da operação desejada: ")

        if escolha == '0':
            print("Saindo da calculadora.")
            break
        elif escolha in {'1', '2', '3', '4'}:
            try:
                valor1 = float(input("Digite o primeiro valor: "))
                valor2 = float(input("Digite o segundo valor: "))

                if escolha == '1':
                    resultado = soma(valor1, valor2)
                elif escolha == '2':
                    resultado = subtracao(valor1, valor2)
                elif escolha == '3':
                    resultado = multiplicacao(valor1, valor2)
                elif escolha == '4':
                    resultado = divisao(valor1, valor2)

                print(f"Resultado: {resultado}")
            except ValueError:
                print("Erro: Insira valores numéricos válidos.")
        else:
            print("Essa opção não existe. Tente novamente.")

if __name__ == "__main__":
    main()
