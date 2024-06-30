
impares = []
pares = []
i=1
while i <= 10:
    x = int(input(f"escolha um numero aleatorio, ({i}/10): "))
    if x % 2 != 0:
        impares.append(x)
    else:
        pares.append(x)
    i += 1
print("Números ímpares:", impares)
print("Números pares:", pares)