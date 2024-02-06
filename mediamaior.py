nome1 = input("Digite o nome do aluno1: ")
nota1 = float(input("Digite sua nota: "))
while nota1 < 0 or nota1 > 10:
    nota1 = float(input("Digite um valor de 0-10 "))

nome2 = input("Digite o nome do aluno2: ")
nota2 = float(input("Digite sua nota: "))
while nota2 < 0 or nota2 > 10:
    nota2 = float(input("Digite um valor de 0-10 "))
    
nome3 = input("Digite o nome do aluno3: ")
nota3 = float(input("Digite sua nota: "))
while nota3 < 0 or nota3 > 10:
    nota1 = float(input("Digite um valor de 0-10 "))
    
aluno = nome1
maior = nota1

if nota1 > nota2 and nota1 > nota3:
   print(f"O aluno {aluno}, teve a maior nota {maior}")

