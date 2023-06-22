#Programa que leia 5 valores e coloque em ordem crescente sem usar sorted
#Precisa informar a posição da lista que foi adicionado
lista = []  # Começa com uma lista vazia para adicionar os 5 valores inputados pelo usuario
for c in range(0, 5):  # Quero 5 valores, portando o range é de 0 a 5, pois o 5 não conta
    n = int(input('Digite um valor: '))  # Peço pro usuário digitar um valor a cada loop do for
    if c == 0 or n > lista[-1]:  # Checo com um if a cada for, pra ver se adiciono o n no final da lista.
        # O primeiro valor que é digitado em c == 0 sempre irá pro final da lista, pois é o primeiro da lista.
        # Depois só será adicionado ao final caso o n for maior que o valor na posição -1, que é a ultima da lista
        lista.append(n)
        print('Valor adicionado ao final da lista...')
    else:  # Caso o primeiro if não seja verdadeiro, preciso checar a posição que o n irá tomar
        pos = 0 # começo na posição 0
        while pos < len(lista):  # E preciso ir até a posição 4 (percorrer de 0 a 4 dentro da lista)
            if n <= lista[pos]:  # Vou checar primeiro na posição 0 e adicionar +1 na posição caso o if não seja
                # verdadeiro na posição anterior
                lista.insert(pos, n)  #Quando encontrar a posição que o n deve ser inserido,
                # ele entra na posição pos e insere o valor n
                print(f'Valor adicionado na posição {pos}')  # E me informa a posição que o valor n entrou
                break  # Quando ele insere ele para o while e volta pro for para pedir outro valor n
                # e verificar a posição novamente
            pos += 1  # Quando o if não for verdadeiro, ou seja, a posição não conter um maior ou igual a n
            # Eu adiciono +1 para procurar na próxima posição e assim por diante até a posição 4
print('~' * 30)
print(f'Os valores digitados em ordem crescente foram {lista}')