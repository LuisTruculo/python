j = input("Você está em jejum s/n? ")
t = input("Trigliceres? ")
t = int(t)
if j == 's':
    if t > 150:
        print("Alto")
    else:
        print("Normal")
else:
    if t > 175:
        print("Alto")
    else:
        print("Normal")
