lista = 'Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Mochila', 119.99, 'Livro', 34.99
preço = 0

print('=' * 30)
print(f'{"LISTAGEM DE PREÇOS":^30}')
print('=' * 30)

for pos, produto in enumerate(lista):
    if pos % 2 == 0:
        print(f'{produto:.<20}', end='')
    else:
        print(f'R${produto:>7.2f}')
print('=' * 30)
