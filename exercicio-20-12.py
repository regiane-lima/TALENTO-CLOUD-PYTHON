def obter_numero(mensagem):
    while True:
        try:
            num = int(input(mensagem))
            return num
        except ValueError:
            print('Precisa ser um número inteiro')

def mostrar_numero():
    numero = obter_numero('Escreva um número entre 0 e 100: ')
    while not (0 <= numero <= 100):
        print('Número inválido. Deve estar entre 0 e 100.')
        numero = obter_numero('Escreva um número entre 0 e 100: ')
    print(f'Ótimo, você escolheu o {numero}')

def verificar_par():
    num = obter_numero('Insira um número: ')
    print(f'Ótimo, você inseriu um número par: {num}' if num % 2 == 0 else 'Erro: O número inserido não é par')

def verificar_divisivel():
    num = obter_numero('Insira um número: ')
    print(f'O número {num} é divisível por 2 ou por 3' if num % 2 == 0 or num % 3 == 0 else f'O número {num} não é divisível por 2 ou por 3')

# Testar as funções
mostrar_numero()
verificar_par()
verificar_divisivel()
