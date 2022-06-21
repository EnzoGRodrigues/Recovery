import os

logMemoria = []  # bufferLog
logDisco = []  # Log do disco
bufferDados = [7, 14, 21, 28, 35]  # Buffer de dados da memoria
discoDados = [7, 14, 21, 28, 35]  # Dados do disco
redo = []
undo = []
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
    logMemoria[:] += ([t, i, "idade", discoDados[i - 1], newValue])
    bufferDados[i - 1] = newValue


def checkpoint():
    logDisco[:] = logMemoria[:]
    discoDados[:] = bufferDados[:]


def failure():
    logMemoria.clear()
    logDisco.clear()
    bufferDados.clear()


def commit():
    t = input("Digite a transação que deseja commitar: ")
    logDisco[:] += ([s for s in logMemoria if t in s])
    redo[:] += ([s for s in logMemoria if t in s])  #
    if os.path.exists('LogDisco.txt'):
        f = open("LogDisco.txt", "w")
        # for i in discoLog:
        f.write(str(logDisco) + "\n")
        f.close()


while aux != 's':
    print("\na - Visualizar buffer do Log")
    print("b - Visualizar log do disco")
    print("c - Visualizar Dados da memoria")
    print("d - Visualizar Dados do disco")
    print("-------------------------------")
    print("e - Update")
    print("f - Checkpoint")
    print("g - Falha")
    print("h - Commit")
    print("-------------------------------")
    print("s - Sair do programa")
    print("-------------------------------")
    aux = input("Escolha uma opcao: ")

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
