
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

print("Preencha os números da matriz 3x3:")
for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(f'Digite o número para a posição [{i}][{j}]: '))


print("Matriz preenchida:")
for linha in matriz:
    for elemento in linha:
        print(f'{elemento}', end=' | ')
    
    print()  
