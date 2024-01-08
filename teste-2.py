lista_musicos = ['Djavan', 'Roberto Carlos', 'Elis Regina', 'Tom Jobim', 'Milton Nascimento', 'Chico Buarque', 'Nara Leão', 'Pitty', 'Simonal', 'Moacir Santos', 'Caetano Veloso', 'Elza Soares', 'Paulinho da Viola', 'Yamandú Costa', 'Gal Costa']


print("Quantidade de elementos na lista:", len(lista_musicos))

print("Dado no índice 2:", lista_musicos[2])
try:
    print("Dado no índice 9:", lista_musicos[9])
except IndexError:
    print("O índice 9 não existe na lista")
try:
    print("Dado no índice 14:", lista_musicos[14])
except IndexError:
    print("O índice 14 não existe na lista")
