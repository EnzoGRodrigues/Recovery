bufferLog: list[int] = []  # memoria
logDisco: list[int] = [7, 14, 21, 28, 35]  # disco
updateList: list[int] = []
aux = ''

while aux != 's':

    print("a - Visualizar buffer do Log")
    print("b - Visualizar log do disco")
    print("c - Update")
    print("d - Checkpoint")
    print("e - Falha")
    print("f - Commit")
    print("s - Sair do programa")
    aux = input("Escolha uma opcao:\n")

    if aux == 'a':
        print("Visualizando buffer do log\n")
        print(bufferLog, "\n")
    elif aux == 'b':
        print("Visualizando log do disco\n")
        print(logDisco, "\n")
    elif aux == 'c':
        i = input("Digite a posicao do elemento: ")
        iInt = int(i) - 1
        newValue = input("Digite novo valor: ")
        newValueInt = int(newValue)
        updateList.insert(iInt, newValueInt)

        # i = input("Digite a posicao do elemento: ")
        # iInt = int(i) - 1
        # newValue = input("Digite novo valor: ")
        # newValueInt = int(newValue)
        # bufferLog[iInt] = newValueInt

    elif aux == 'd':
        logDisco = bufferLog
    elif aux == 'e':
        bufferLog.clear()
    elif aux == 'f':
        print("Visualizando buffer do log\n")
        print(updateList, "\n")

    else:
        print("Programa encerrado")

