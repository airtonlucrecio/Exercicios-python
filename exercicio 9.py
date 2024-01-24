
pessoas = {}
dados = []
soma = média = 0

while True:
    pessoas.clear()
    pessoas['nome'] = input('Nome: ')
    while True:
        pessoas['sexo'] = input('Sexo: [M/F] ').upper()[0]
        if pessoas['sexo'] in 'MF':
            break
        print("ERRO, por favor, digite apenas M ou F.")
    pessoas['idade'] = int(input('Idade: '))
    soma += pessoas['idade']
    dados.append(pessoas.copy())
    while True:
        resp =  input('quer continuar? [S/N]').upper()[0] 
        if resp in 'SN':
            break
        print('ERRO, responda penas S ou N.')
    if resp == 'N':
         break
        
print('-='*30)

print(f'Ao todo temos {len(dados)} pessoas cadastradas. ')
média = soma / len(dados)
print(f'A média de idade é de {média:5.2f} anos.')
print(f' As mulheres cadatradas foram: ', end='')
for p in dados:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end='')
print()
print(f'Lista de pessoas que estão acima da média:', end='')
for p in dados:
    if p['idade'] >= média:
        print('   ')
        for k,v in p.items():
            print(f'{k} = {v}', end= '')
        print()
print('<< ENCERRADO >>')

print('-='*40)

