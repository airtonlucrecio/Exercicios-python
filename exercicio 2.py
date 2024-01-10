num = list()
pares = []
impares = []

for p in range(0, 7):
    valor = int(input('Digite um valor: '))
    num.append(valor)
    
    if valor % 2 == 0 and valor != 0:
        pares.append(valor)
        pares = sorted(pares)
             
    else: 
        impares.append(valor)
        impares = sorted(impares)

print(f'Os números pares são: {pares}')
print(f'Os números ímpares são: {impares}')

