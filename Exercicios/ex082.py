lista = []
listapares = []
listaimpares = []

while True:
    lista.append(int(input('Adicione um número a lista: ')))
    continuar = input('Deseja continuar: [S/N] ').upper()
    if continuar == 'N':
        break

for pos, cont in enumerate(lista):
    if cont % 2 == 0:
        listapares.append(cont)
    else:
        listaimpares.append(cont)

print(f'Lista completa: {lista}')
print(f'Lista filtrada com números pares: {listapares}')
print(f'Lista filtrada com números ímpares: {listaimpares}')
