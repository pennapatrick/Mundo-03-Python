tabelaBrasileiro = ('Palmeiras', 'Atlético', 'São Paulo', 'Santos', 'Internacional',
                    'Goiás', 'Botafogo', 'Corinthians', 'Flamengo', 'Athletico-PR',
                    'Bahia', 'Ceará SC', 'Fluminense', 'Fortaleza', 'Cruzeiro',
                    'Chapecoense', 'Avaí', 'CSA', 'Grêmio', 'Vasco da Gama')

print('-' * 90 + f'\n{"DADOS": ^90}\n' + '-' * 90)

print(f'Os 5 primeiros colocados são: {tabelaBrasileiro[:5]}')
print('-' * 90)
print(f'Os 4 da lanterna são: {tabelaBrasileiro[16:]}')
print('-' * 90)
print(f'A lista em ordem alfabética: {sorted(tabelaBrasileiro)}')
print('-' * 90)
print(f'A Chapecoense se encontra na {tabelaBrasileiro.index("Chapecoense")+ 1}º Posição')
print('-' * 90)