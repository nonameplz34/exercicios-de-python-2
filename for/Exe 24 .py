x = int(input("quantas notas vamos trabalhrar ?  "))
soma = 0
for i in range(x):
    numero = int(input(f"{i+1}º nota: "))
    soma += numero  


media = soma / x



print("A média é:", media)



