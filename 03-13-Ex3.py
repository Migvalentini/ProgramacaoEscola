nome = ''
lista = []

while nome != '0':
    nome = input("Digite um nome: ")
    lista.append(nome)

lista.remove('0')
print(lista)
print(f"O tamanho {len(lista)}")