



for i in range (1000):
    x = int(input("quantos numeros vc quer trbalhar?:  "))
    if x <= 0 or x > 1000:
        print("so numeros entre 1 e 1000, por favor ")
    else:
        break

y=[]
for i in range(x):
    numero = int(input(f"Digite o {i + 1}º número: "))
    y.append(numero)

print("o maior numero é ",max(y))
print("o menor numero é ", min(y))

somar = min(y) + max(y)

print("a soma dos dois é", somar)




