x = int(input("escolha um numero: "))
y = int(input(f"escolha um numero mior q {x}: "))

soma=0

while x+1 < y:
    print(x+1)
    soma += x
    x +=1


print("a soma de tudo é ", soma)