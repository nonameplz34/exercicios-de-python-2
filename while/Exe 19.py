x = int(input("quantos numeros vc quer trbalhar?:  "))

while x < 0 or x > 1000 :
    (print("so numeros de 1 a 1000  "))
    x = int(input("quantos numeros vc quer trbalhar?:  "))

y=[]
i = 0
while i in range(x):
    numero = int(input(f"Digite o {i + 1}º número: "))
    y.append(numero)
    i+=1

print("o maior numero é ",max(y))
print("o menor numero é ", min(y))

somar = min(y) + max(y)

print("a soma dos dois é", somar)
