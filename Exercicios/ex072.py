contagem = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze',
            'Doze', 'Treze', 'Quartorze', 'Quinze', 'Dezesseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')

num = int(input('Digite um número entre 0 e 20: '))

while True:
    if num > 20 or num < 0:
        num = int(input('Tente novamente. Digite um número entre 0 e 20: '))
    else:
        print(contagem[num])
        break
