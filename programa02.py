numero = input("Digite um número de dois digitos menor que 100: ")
if int(numero) >= 100 or int(numero) < 10: raise ValueError("Escolha um número de 2 digitos!")

print(int(numero[:1])+int(numero[1:]))
