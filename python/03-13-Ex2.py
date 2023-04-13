tempo = int(input("Digite o tempo gasto: "))
velocidade = int(input("Digite a velocidade: "))

litros = round(tempo * velocidade / 12, 3)

print(litros)