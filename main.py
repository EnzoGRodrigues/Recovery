bufferLog: list[int] = [7, 14, 21, 28, 35]  # memoria
logDisco: list[int] = [7, 14, 21, 28, 35]  # disco
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
        print("Visualizando buffer do log")
        print(bufferLog)
    elif aux == 'b':
        print("Visualizando log do disco")
        print(logDisco)
    elif aux == 'c':
        i = input("Digite a posicao do elemento: ")
        iInt = int(i) - 1
        newValue = input("Digite novo valor: ")
        newValueInt = int(newValue)
        bufferLog[iInt] = newValueInt

    elif aux == 'd':
        logDisco = bufferLog
    elif aux == 'e':
        bufferLog.clear()
    # elif aux == 'f':

    else:
        print("Programa encerrado")

