from datetime import datetime

dados = dict()
dados['nome'] = input('nome: ')
nasc = int(input('ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('carteira de trabalho (0 se nao tem):'))

if dados['ctps'] != 0: 
    dados['contratacao'] = int(input('ano de contratação: '))
    dados['Salário'] = float(input('Salário R$: '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratacao'] + 35) - datetime.now().year)
    print('-=' *30)
for k,v in dados.items():
    print(f' - {k} tem o valor =  {v}')