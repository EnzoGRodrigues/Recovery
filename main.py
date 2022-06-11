logMemoria = []  # bufferLog
logDisco: list[int] = []  # Log do disco
bufferDados: list[int] = []  # Buffer de dados
discoDados: list[int] = [7, 14, 21, 28, 35]  # Dados do disco
aux = ''


def viewLogMemoria():
    print("Visualizando Log da memória\n")
    print(logMemoria, "\n")
def viewLogDisco():
    print("Visualizando Log do disco\n")
    print(logDisco, "\n")
def update():






while aux != 's':
    t = input("Escolha a trasação: ")
    print("a - Visualizar buffer do Log")
    print("b - Visualizar log do disco")
    print("c - Update")
    print("d - Checkpoint")
    print("e - Falha")
    print("f - Commit")
    print("s - Sair do programa")
    aux = input("Escolha uma opcao:\n")

    if aux == 'a':
        viewLogMemoria()
    elif aux == 'b':
        viewLogDisco()
    elif aux == 'c':
        i = input("Digite a posicao do elemento: ")
        iInt = int(i) - 1
        newValue = input("Digite a idade atualizada: ")
        newValueInt = int(newValue)
        JlogMemoria.append([t, "idade", discoDados[iInt], newValueInt])
        # bufferDados[iInt] = newValueInt

        # i = input("Digite a posicao do elemento: ")
        # iInt = int(i) - 1
        # newValue = input("Digite novo valor: ")
        # newValueInt = int(newValue)
        # updateList.insert(iInt, newValueInt)

        # i = input("Digite a posicao do elemento: ")
        # iInt = int(i) - 1
        # newValue = input("Digite novo valor: ")
        # newValueInt = int(newValue)
        # bufferLog[iInt] = newValueInt

    # elif aux == 'd':
    # logDisco = bufferLog
    # elif aux == 'e':
    # bufferLog.clear()
    # elif aux == 'f':

    else:
        print("Programa encerrado")