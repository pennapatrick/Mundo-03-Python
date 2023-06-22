lista = []

while True:
    num = int(input('Digite um número: '))
    if num not in lista:
        lista.append(num)
        print('Valor Adicionado com sucesso')
    else:
        print('Valor Duplicado! Não foi possivel adicionar')
    continuar = input('Deseja continuar? [S/N] ').upper()
    print('=' * 20)
    if continuar == 'N':
        break
print(f'Sua lista completa em ordem crescente: {sorted(lista)}')
