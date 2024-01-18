import random

def multi_escolha():
    perguntas = [
        {"pergunta": "Qual é a capital da França?", "opcoes": ["1. Paris", "2. Berlim", "3. Londres", "4. Madri"], "resposta": "1", "dica": "A cidade das luzes."},
        {"pergunta": "Qual é o maior planeta do sistema solar?", "opcoes": ["1. Terra", "2. Júpiter", "3. Marte", "4. Saturno"], "resposta": "2", "dica": "Possui uma grande mancha vermelha."},
        # Adicione mais perguntas conforme necessário
    ]

    pontuacao = 0

    random.shuffle(perguntas)  # Embaralha as perguntas

    for pergunta_atual in perguntas:
        print(pergunta_atual["pergunta"])
        
        for opcao in pergunta_atual["opcoes"]:
            print(opcao)

        escolha = input('Escolha uma opção de 1 a 4: ')

        if escolha == pergunta_atual["resposta"]:
            print('Correto! Você ganhou 1 ponto.')
            pontuacao += 1
        else:
            print('Incorreto. Tente novamente.')
            print('Dica:', pergunta_atual["dica"])
            
    print("Sua pontuação final é:", pontuacao)

multi_escolha()
