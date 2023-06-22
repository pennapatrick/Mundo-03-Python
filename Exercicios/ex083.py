contador1 = 0
contador2 = 0

lista = (input('Digite: '))

for pos, cont in enumerate(list(lista)):
    if cont == '(':
        contador1 += 1
    if cont == ')':
        contador2 += 1
if contador1 == contador2:
    print('Sua expressão é válida!')
else:
    print('Sua expressão está errada!')