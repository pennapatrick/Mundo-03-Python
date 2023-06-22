cadastro = []
dados = []
maip = menp = 0


while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    if len(cadastro) == 0:
        maip = menp = dados[1]
    else:
        if dados[1] > maip:
            maip = dados[1]
        if dados[1] < menp:
            menp = dados[1]


    cadastro.append(dados[:])
    dados.clear()
    continuar = input('Deseja continuar [S/N] ').upper()
    if continuar == 'N':
        break
print('=' * 20)
print(f'Foram cadastradas {len(cadastro)} pessoas')
print(f'O maior peso foi de {maip}kg ', end='')
for p in cadastro:
    if p[1] == maip:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {menp}kg ', end='')
for p in cadastro:
    if p[1] == menp:
        print(f'[{p[0]}] ', end='')

