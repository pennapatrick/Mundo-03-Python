lista = []
for v in range(0, 5):
    lista.append(int(input(f'Digite um número para posição {v}: ')))

print('=-' * 20 + '=')

print(f'Você digitou os valores: {lista}')

print(f'O maior valor digitado foi {max(lista)} nas posiçoes ', end='')
for pos, cont in enumerate(lista):
    if cont == max(lista):
        print(f'{pos}... ', end='')
print()
print(f'O menor valor digitado foi {min(lista)} nas posiçoes ', end='')
for pos, cont in enumerate(lista):
    if cont == min(lista):
        print(f'{pos}... ', end='')
print()
