verificar = []
mostrinho = []
        

numero = int(input("Digite um numero "))
for i in range(1, numero+1):
    if numero % i == 0:
        verificar.append(i)
        if numero / i != 0:
            mostrinho.append(i)
            
    
if len(verificar) == 2 :
    print("é primo")
    
else:
    print("nao é primo, pode ser divisivel por", mostrinho )
    
                
    




