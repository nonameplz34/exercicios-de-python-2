for i in range (1000):
    x = int(input("número para calcular o fatorial: "))
    if x <= 0 or x > 16:
        print("so numeros entre 1 e 16, por favor ")
    else:
        fatorial = 1

        for i in range(1, x + 1):
            fatorial *= i  
    
        print("o resultado é", fatorial)


