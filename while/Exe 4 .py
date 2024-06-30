paisA = 80000
taxaDeCrescimentoA = 3 / 100
paisB = 200000
taxaDeCrescimentoB = 1.5 / 100
anos = 0



while paisA < paisB:
        
        paisA += paisA * taxaDeCrescimentoA
        paisB += paisB * taxaDeCrescimentoB
        anos += 1

print("o pais A ira passar o pais B em", anos, "anos ")
