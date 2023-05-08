vendedores = []
controlador = 's'

while controlador == 's':
    vendedor = {}
    a = []
    vendedor['nome'] = input('Digite o nome do vendedor: ')
    vendedor['numero_loja'] = int(input('Digite o número da loja: '))
    vendedor['valor'] = float(input('Digite o valor vendido: '))
    vendedor['comissao'] = round(vendedor['valor'] * 0.08, 2)
    a.append(vendedor)
    vendedores.append(a)
    controlador = input('Você deseja adicionar um novo vendedor? [Sim / Não] ')[0].lower()

nome_vendedor = ''
maior_venda = 0
indice = 0

for v in vendedores:
    if v[0]['comissao'] > maior_venda:
        maior_venda = v[0]['comissao']
        nome_vendedor = v[0]['nome']
        i = indice
    indice += 1

vendedores[i][0]['comissao'] += 300

print(f"O nome do vendedor que mais vendeu foi o/a {vendedores[i][0]['nome']}")

for n in vendedores:
    print(f"Nome: {n[0]['nome']} - Valor da comissão: R${n[0]['comissao']} ")