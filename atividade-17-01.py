# Declara as variáveis
afirmacoes = ["O Brasil é um país da América do Sul", "A capital da França é Paris", "A água é um composto químico", "O número 7 é um número primo", "O sol é uma estrela"]
respostas = []
pontuacao = 0

# Apresenta as afirmações
for afirmacao in afirmacoes:
    print(afirmacao)
    resposta = input("(V) Verdadeiro ou (F) Falso: ").upper()  # Converte a entrada do usuário para maiúsculas
    respostas.append(resposta)

# Calcula a pontuação
for i in range(len(afirmacoes)):
    if respostas[i] == afirmacoes[i][0].upper():  # Converte o primeiro caractere da afirmação para maiúsculas
        pontuacao = pontuacao + 1

# Exibe a pontuação
print("Sua pontuação é:", pontuacao)
