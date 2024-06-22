num = int(input("Quantos números? "))
i = int(input("Primeiro número: "))
j = int(input("Segundo número: "))

numset = set()

for n in range(0, num, +1):
    numset.add(i*n)
    numset.add(j*n)

multiplos = sorted(numset)

print("Os {} primeiros multiplos de {} e {} são {}".format(num, i, j, multiplos[:n+1]))

