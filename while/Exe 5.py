paisA  = int(input("Informe a população inicial do país A: "))
taxaDeCrescimentoA  = float(input("Informe a taxa de crescimento anual do país A (%): "))
paisB = int(input("Informe a população inicial do país B: "))
taxaDeCrescimentoB  = float(input("Informe a taxa de crescimento anual do país B (%): "))
anos = 0

while paisA <= 0 or taxaDeCrescimentoA <= 0 or paisB <= 0 or taxaDeCrescimentoB <= 0:

    paisA  = int(input("Informe a população inicial do país A: "))
    taxaDeCrescimentoA  = float(input("Informe a taxa de crescimento anual do país A (%): "))
    paisB = int(input("Informe a população inicial do país B: "))
    taxaDeCrescimentoB  = float(input("Informe a taxa de crescimento anual do país B (%): "))



while paisA  < paisB:

    paisA  += paisA  * (taxaDeCrescimentoA  / 100)
    paisB += paisB * (taxaDeCrescimentoB  / 100)
    anos += 1


print("o pais A ira passar o pais B em", anos, "anos ")