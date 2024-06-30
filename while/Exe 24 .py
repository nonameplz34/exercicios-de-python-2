x = int(input("quantas notas vamos trabalhrar ?  "))
soma = 0
i=0
while i < x:
    numero = int(input(f"{i+1}º nota: "))
    soma += numero  
    i+=1


media = soma / x

print("A média é:", media)



