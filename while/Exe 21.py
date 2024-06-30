numero = int(input("Digite um número: "))
verificar = []
i = 1

while i <= numero:
    if numero % i == 0:
        verificar.append(i)
    i += 1

if len(verificar) == 2:
    print("É primo")
else:
    print("Não é primo")