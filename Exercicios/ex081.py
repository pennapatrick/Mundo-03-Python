lista = []

while True:
    lista.append(int(input('Digite um número: ')))
    continuar = input('Valor Adicionado, Deseja continuar? [S/N] ').upper()
    if continuar == 'N':
        print('-' * 30)
        print(f'{"DADOS":^30}')
        print('-' * 30)
        break
print(f'O total de número digitados foram: {len(lista)}')
print(f'Aqui temos a lista em ordem decrescente: {(sorted(lista, reverse=True))}')
if 5 in lista:
    for pos, cont in enumerate(sorted(lista, reverse=True)):
        if cont == 5:
            print(f'O valor 5 está presente nessa lista na posição {pos + 1}.')
else:
    print('O valor 5 NÃO está presente nessa lista')
