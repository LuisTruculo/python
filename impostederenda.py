sal = float(input("Qual o seu salário? "))
if sal >= 2112 and sal <= 2826:
    imposto = sal * 0.075
    print(f"{imposto}")
elif sal >= 2826 and sal <= 3751:
    imposto = sal * 0.15
    print(f"{imposto}")
elif sal >= 3751 and sal <= 4664:
    imposto = sal * 0.225
    print(f"{imposto}")
elif sal >= 4664:
    imposto = sal * 0.275
    print(f"{imposto}")