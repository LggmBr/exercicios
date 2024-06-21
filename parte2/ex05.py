num[0] = int(input("First number: "))
num[1] = int(input("Second number: "))
num[2] = int(input("Third number: "))

num.sort()

if num[0]**2 + num[1]**2 == num[2]**2:
    print("Esses valores podem formar um triângulo retângulo")
else:
    print("Esses valores não podem formar um triângulo retângulo")
