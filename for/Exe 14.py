impares = []
pares = []

for i in range(11):
    x = int(input(f"escolha um numero aleatorio, ({i}/10): "))
    if x % 2 != 0:
        impares.append(x)
    else:
        pares.append(x)
        
print("Números ímpares:", impares)
print("Números pares:", pares)