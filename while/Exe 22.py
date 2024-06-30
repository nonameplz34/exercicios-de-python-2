verificar = []
mostrinho = []

numero = int(input("Digite um número: "))
i = 1

while i <= numero:
    if numero % i == 0:
        verificar.append(i)
        if numero+1 / i != 1: 
            mostrinho.append(i)
    i += 1

if len(verificar) == 2:
    print("É primo")
else:
    print("Não é primo, pode ser divisível por", mostrinho)
