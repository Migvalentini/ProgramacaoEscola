num = int(input("Digite um número: "))

if num % 2 == 1:
    print("Estranho")
elif 2 < num < 5:
    print("Não é estranho")
elif 6 < num < 20:
    print("Estranho")
elif num > 20:
    print("Não é estranho")