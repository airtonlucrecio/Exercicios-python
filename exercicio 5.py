alunos = list()

nome = input('Nome: ')
media = int(input('Média: '))

alunos.append((nome, media))

for m in alunos:
    if m[1] < 7:
        print(f'O aluno(a) {m[0]} está reprovado.')
    else:
        print(f'O aluno(a) {m[0]} está aprovado.')
