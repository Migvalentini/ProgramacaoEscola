number = 0
numbers = []
while number >= 0:
    number = int(input("Digite um número: "))
    if number % 2 == 0:
        numbers.append(number)
        
print(numbers)