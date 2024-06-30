print("coloque valores maiores q 0")
anos = 0

paisA  = int(input("Informe a população inicial do país A: "))
taxaDeCrescimentoA  = float(input("Informe a taxa de crescimento anual do país A (%): "))
paisB = int(input("Informe a população inicial do país B: "))
taxaDeCrescimentoB  = float(input("Informe a taxa de crescimento anual do país B (%): "))



for _ in range(100):
    if paisA  >= paisB:
        break
    paisA  += paisA  * (taxaDeCrescimentoA  / 100)
    paisB += paisB * (taxaDeCrescimentoB  / 100)
    anos += 1


print("o pais A ira passar o pais B em", anos, "anos ")