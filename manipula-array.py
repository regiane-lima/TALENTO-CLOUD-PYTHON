lista_produtos = ['máscaras faciais', 'rímel', 'esmaltes', 'perfumes', 'cremes hidratantes', 'xampus', 'sabonetes']

# Removendo 'delineadores'
lista_produtos.remove('delineadores')

# Adicionando dois novos produtos
lista_produtos.append('protetor solar')
lista_produtos.append('máscara capilar')

# Imprimindo a nova lista
print("Lista de produtos atualizada:")
for produto in lista_produtos:
    print(f"Temos {produto} à venda!")
