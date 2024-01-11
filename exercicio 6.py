from random import randint
from time import sleep
from operator import itemgetter

jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6), 
        }
ranking = list()

print('valores sorteados:')

for j, v in jogo.items():
    print(f'{j} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1),  reverse=True)
print(ranking)
for i,k in enumerate(ranking):
    print(f'{i+1}° lugar: {k[0]} com {k[1]}.')
    sleep(1)
    