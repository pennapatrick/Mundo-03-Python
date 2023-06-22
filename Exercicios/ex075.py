print(f'-' * 40)
a = int(input('Digite um número: ')), int(input('Digite um número: ')), int(
    input('Digite um número: ')), int(input('Digite um número: '))
print(f'-' * 40)
print(f'Você digitou {a}')

if a.count(9) > 1:
    print(f'O numero 9 apareceu {a.count(9)} vezes')
if a.count(9) == 1:
    print(f'O numero 9 apareceu {a.count(9)} vez')
if a.count(9) == 0:
    print(f'O numero 9 não apareceu')

if a.count(3) > 0:
    print(f'O número 3 apareceu na {a.index(3) + 1}º Posição')
else:
    print('O número 3 não apareceu nenhuma vez')

print('Os valores pares digitados foram: ', end='')
for cont in a:
    if cont % 2 == 0:
        print(cont, end=' ')
