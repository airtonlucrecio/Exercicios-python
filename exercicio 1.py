rep = list()
totmai = totmen = 0 

while True:
    rep.append([str(input('nome: ')), int(input('peso: '))])
    # rep.append(int(input('peso: ')))
    
    if input('quer continuar?') == 'N':
        break
    
for p in rep:   
    if p[1] >= 90:
        print(f'{p[0]} está acima do peso')
        totmai += 1 
    else:
        print(f'{p[0]} esta com peso normal')
        totmen += 1 
        
print(f'temos {totmai} acima do peso e {totmen} com peso normal.')   
