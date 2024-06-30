

x = int(input("qunatas pessoas tem na turma? "))
soma = 0

for i in range(x):
    pessoinha = float(input(f"a {i+1}º pessoa tem..? "))
    soma += pessoinha  

media = soma / x
print("A média de idade é:", media)

if media <= 25:
    print("a turma é jovem")
elif 26 <= media <= 60:
    print("a turma é jovem adulta")
else:
    print("a turma é jovem idosa")





