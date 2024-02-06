nome = (input("Qual o seu nome? "))
p1 = float(input("Qual foi a nota da sua primeira prova? "))
if p1 < 0 or p1 > 10:
    p1 = float(input("Digite o valor de 0-10 para a primeira prova"))
    
p2 = float(input("Digite o valor da segunda prova: "))
if p2 < 0 or p2 > 10:
    p2 = float(input("Digite o valor de 0-10 para a segunda prova"))

t = float(input("Digite o valor do trabalho: "))
if t < 0 or t > 10:
    t = float(input("Digite o valor de 0-10 para o trabalho"))

media = p1 * 0.35 + p2 * 0.35 + t * 0.30
if  media >= 5:
    situacao = "Aprovado"
elif media >= 3.5:
    situacao = "Recuperação"
elif media < 3.5:
    situacao = "Reprovado"
print(f"Olá, {nome}, sua média final foi de {media}. Situação: {situacao}")




