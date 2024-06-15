numero = int(input("Digite um número: "))
divisores = []

for i in range(1, numero + 1):
    if numero % i == 0: divisores.append(i) 

print("Os divisores de {} são: {}".format(numero, divisores))
