from typing import List, Any

logMemoria = [1, 2, 3, 4, 5]  # bufferLog
logDisco = []  # Log do disco
bufferDados: list[Any] = []  # Buffer de dados da memoria
discoDados = [7, 14, 21, 28, 35]  # Dados do disco
aux = ''


def viewLogMemoria():
    print("Visualizando Log da memória\n")
    print(logMemoria, "\n")


def viewLogDisco():
    print("Visualizando Log do disco\n")
    print(logDisco, "\n")


def viewBufferDadosMemoria():
    print("Visualizando Dados da memoria\n")
    print(bufferDados, "\n")


def update():
    t = input("Escolha a transação: ")
    i = input("Digite a posicao do elemento: ")
    iInt = int(i) - 1
    newValue = input("Digite a idade atualizada: ")
    newValueInt = int(newValue)
    logMemoria.append([t, "idade", discoDados[iInt], newValueInt])
    bufferDados.append(newValue)


def checkpoint():
    logDisco.append(logMemoria)
    discoDados.append(bufferDados)


def failure():
    logMemoria.clear()
    logDisco.clear()
    bufferDados.clear()


def commit():
    logDisco.append(logMemoria)
    logMemoria.clear()


while aux != 's':
    print("a - Visualizar buffer do Log")
    print("b - Visualizar log do disco")
    print("c - Visualizar Dados da memoria")
    print("d - Update")
    print("e - Checkpoint")
    print("f - Falha")
    print("g - Commit")
    print("s - Sair do programa")
    aux = input("Escolha uma opcao:\n")

    if aux == 'a':
        viewLogMemoria()
    elif aux == 'b':
        viewLogDisco()
    elif aux == 'c':
        viewBufferDadosMemoria()

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

    elif aux == 'd':
        update()
    # logDisco = bufferLog
    elif aux == 'e':
        checkpoint()
    elif aux == 'f':
        failure()

    elif aux == 'g':
        commit()
    else:
        print("Programa encerrado")
