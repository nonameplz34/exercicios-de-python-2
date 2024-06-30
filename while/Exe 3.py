while True:  
    nome = input("seu nome (mais de 3 letras): ")
    idade = int(input("sua idade (entre 0 e 150): "))
    salario = float(input("salário (maior que zero): "))
    sexo = input("sexo (f ou m): ").lower()
    estadocivil = input("estado civil (s, c, v, d): ").lower()

    if len(nome) > 3 and  idade >= 0 or idade <= 150 and salario > 0 and sexo in ['f', 'm'] and estadocivil in ['s', 'c', 'v' 'd']:
        break
    else:
        print("tente de novo ")



print("boa")
