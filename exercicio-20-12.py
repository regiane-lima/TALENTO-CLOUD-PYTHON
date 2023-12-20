def mostrarNumero():
    print('Escreva um número menor ou igual a 100')
    numero_valido = False

    while not numero_valido:
        try:
            num = int(input())
            if num > 100:
                print('Precisa ser um número menor ou igual a 100')
            elif num < 0:
                print('Não é permitido inserir números negativos')
            else:
                print('Ótimo, você escolheu o ' + str(num))
                numero_valido = True
        except ValueError:
            print('Precisa ser um número inteiro')

def verificarPar():
    try:
        num = int(input('Insira um número: '))
        if num % 2 == 0:
            print('Ótimo, você inseriu um número par:', num)
        else:
            raise ValueError('Erro: O número inserido não é par')
    except ValueError as ve:
        print(ve)

def verificarDivisivel():
    try:
        num = int(input('Insira um número: '))
        if num % 2 == 0 or num % 3 == 0:
            print(f'O número {num} é divisível por 2 ou por 3')
        else:
            print(f'O número {num} não é divisível por 2 ou por 3')
    except ValueError:
        print('Precisa ser um número inteiro')

# Testar as funções
mostrarNumero()
verificarPar()
verificarDivisivel()
