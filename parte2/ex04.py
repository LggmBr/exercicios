number = int(input("Digite um número inteiro positivo: "))
primo = "é"

for i in range(1, number, +1):
    print(i)
    if number % i == 0 and 1<i<number:
        primo = "não é"
        break

print("O número {} {} primo!".format(number, primo))
