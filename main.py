from typing import List, Any

logMemoria = []  # bufferLog
logDisco: list[Any] = []  # Log do disco
bufferDados: list[Any] = [7, 14, 21, 28, 35]  # Buffer de dados da memoria
discoDados = [7, 14, 21, 28, 35]  # Dados do disco
aux = None


def viewLogMemoria():
    print("Visualizando Log da memória\n")
    print(logMemoria, "\n")


def viewLogDisco():
    print("Visualizando Log do disco\n")
    print(logDisco, "\n")


def viewDadosMemoria():
    print("Visualizando Dados da memoria\n")
    print(bufferDados, "\n")


def viewDadosDisco():
    print("Visualizando Dados da memoria\n")
    print(discoDados, "\n")


def update():
    t = input("Escolha a transação: ")
    i = int(input("Digite a posicao do elemento: "))
    newValue = int(input("Digite a idade atualizada: "))
    logMemoria.append([t, i, "idade", discoDados[i - 1], newValue])
    bufferDados[i - 1] = newValue


def checkpoint():
    logDisco[:] = logMemoria[:]
    discoDados[:] = bufferDados[:]


def failure():
    logMemoria.clear()
    logDisco.clear()
    bufferDados.clear()


def commit():
    i = 0
    t = int(input("Numero da transação que deseja commitar: "))
    for x in logMemoria:
        if t in x:
            i = +1
            break
    logDisco.append(logMemoria[t])
    # logDisco.append(logMemoria)d
    # logMemoria.clear()


while aux != 's':
    print("a - Visualizar buffer do Log")
    print("b - Visualizar log do disco")
    print("c - Visualizar Dados da memoria")
    print("d - Visualizar Dados do disco")
    print("e - Update")
    print("f - Checkpoint")
    print("g - Falha")
    print("h - Commit")
    print("s - Sair do programa")
    aux = input("Escolha uma opcao:\n")

    if aux == 'a':
        viewLogMemoria()
    elif aux == 'b':
        viewLogDisco()
    elif aux == 'c':
        viewDadosMemoria()
    elif aux == 'd':
        viewDadosDisco()
    elif aux == 'e':
        update()
    elif aux == 'f':
        checkpoint()
    elif aux == 'g':
        failure()
    elif aux == 'h':
        commit()
    else:
        print("Programa encerrado")
        break
