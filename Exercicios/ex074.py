from random import randint

lista = (randint(0, 10)) ,(randint(0, 10)) ,(randint(0, 10)), (randint(0, 10)), (randint(0, 10))
print('Os valores sorteados foram: ', end='')

for n in lista:
    print(f'{n}', end=' ')
print('\n'f'O maior valor sorteado foi {max(lista)}')
print(f'O menor valor sorteado foi {min(lista)}')

