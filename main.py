import os

logDisco = [] # log do disco
logMemoria = [] # buffer do log
dadosMemoria = [7,14,21,28,35] # buffer de dados 
dadosDisco = [7,14,21,28,35]  # dados do disco
auxDadosDisco = [] 
redo = [] # lista para armazenar transações redo
undo = [] # lista para armazenar transações undo
txtDadosDisco = 'dadosDisco.txt' # arquivo de texto para receber valores que ficam no dado dos disco
txtLogDisco = 'logDisco.txt' # arquivo de texto para receber valores que ficam no log do disco
aux = '' # variável para escolha da atividade que o programa irá realizar 



def viewLogMemoria(): # função que mostra o log da memoria
    print("\nVisualizando buffer do log\n")
    print(logMemoria, "\n")



def viewLogDisco(): # função que mostra o log do disco
    print("\nVisualizando log do disco\n")
    print(logDisco, "\n") 



def viewDadosMemoria(): # função que mostra os dados da memoria
    print("\nVisualizando buffer de dados\n")
    print(dadosMemoria, "\n")



def viewDadosDisco(): # função que mostra os dados do disco
    print("\nVisualizando dados da disco\n")
    print(dadosDisco, "\n")



def update(): # função que realiza o update
        t = input("Escolha a transação: ") # t recebe a transação
        i = int(input("Digite a posição do elemento: ")) # i recebe a posição do elemento que será alterado
        newValue = int(input("Digite o valor: ")) # newValue recebe o valor novo do elemento
        logMemoria.append([t,i,"idade",dadosDisco[i - 1],newValue]) #a lista logMemoria terá uma lista adicionada dentro dela, essa lista será a própria transação
        dadosMemoria[i - 1] = newValue # a lista de dadosMemoria terá o seu valor alterado pelo newValue na posição que foi colocado pelo usuário
        print("\n--> Update realizado <--")



def commit(): # função que realiza o commit
        t = input("Digite a transação que deseja commitar: ") # t recebe a transação que o usuário quer commitar
        logDisco.extend([s for s in logMemoria if t in s]) # s percorre logMemoria e tudo o que estiver lá é copiado no logDisco através do extend
        redo.extend([s for s in logMemoria if t in s]) #s percorre logMemoria e copia tudo o que tem no redo através do extend
        if(os.path.exists(txtLogDisco)): # if testa se existe o path do txtLogDisco
            with open(txtLogDisco, 'w') as f: # se tiver, abre esse txt e escreve algo nele atraves do 'w'
                for i in logDisco: # o i percorre o logDisco
                    f.write(str(i)+"\n") # f.write escreve tudo o i percorreu no txtLogDisco
            print("\n--> Transação",t,"comitada com sucesso <--")
        else:
            print("O arquivo \"logDisco.txt\" nao existe!")



def checkpoint(): # função que realiza o checkpoint
        if(os.path.exists(txtDadosDisco)): # if faz o teste para ver se existe o path desse txt
            with open(txtDadosDisco,'w') as f: # se existir, ele abre o txt e escreve através do 'w'
                f.write(str(dadosMemoria)+"\n") # f.write escreve a lista dadosMemoria no txtDadosDisco
        else: #se não existir ele emite uma mensagem
            print("O arquivo \"dadosDisco.txt\" nao existe!")
        if(os.path.exists(txtLogDisco)): # if faz o teste para ver se existe o path desse txt 
            with open(txtLogDisco, 'w') as f: # se existir, ele abre o txt e escreve através do 'w'
                for i in logMemoria: # o for faz com que o i percorra a lista logMemoria
                    f.write(str(i)+"\n") # tudo o que o i encontrar na lista logMemoria, vai escrever no txtLogDisco
                f.write(str("--> Ponto de CHECKPOINT <--\n")) # vai escrever a mensagem no txtLogDisco
            dadosDisco[:] = list(dadosMemoria[:])
            logDisco[:] = list(logMemoria[:])
        else:
            print("O arquivo \"logDisco.txt\" nao existe!") # se nao existir vai exibir essa mensagem na tela
        print("\n--> Checkpoint realizado com sucesso <--")  #imprime esta mensagem quando o checkpoint for utilizado pelo usuario



def failure(): # função que realiza a falha
    undo.extend([s for s in logMemoria if s not in redo]) # undu é uma lista, através do extend será adicionado valores nele.
                                                         # o for vai fazer com que s percorra logMemoria, e o if irá testar se o conteudo que tem dentro está em redo ou não, se não tiver, ele vai escrever em undo
    auxDadosDisco = list(dadosMemoria[:]) #lista auxDadosDisco esta recebendo a lista dadosMemoria
    for i in range(len(undo)): # len retorna o tamanho de undo, o i percorre o range de undo
        beforeImage = undo[i][3] # beforeImage recebe o valor que vai estar no indice que o i irá percorrer e dentro desse indice i, no indice 3 estará o valor que beforeImage vai receber
        id = undo[i][1] # id recebe o valor que vai estar no indice i, e dentro de i, no indice 1 estará o valor que id vai receber
        auxDadosDisco[id-1] = beforeImage #auxDadosDisco 
    logMemoria.clear() # após a falha o log da memoria é limpo
    dadosMemoria.clear() # após a falha os dados da memoria serão limpos
    with open('dadosDisco.txt','w')as f: # abre o txtDadosDisco
            f.write(str(auxDadosDisco)) # escreve dentro do txt o que está na lista auxDadosDisco
    print("\n-> Falha <--")



def viewRedoUndo(): #funcao que mosta as transação REDO e UNDO
    print("\nREDO",redo,\
            "\nUNDO",undo)



def menu(): # função que mostra o menu para o usuário
    print("\na - Visualizar buffer do Log")
    print("b - Visualizar log do disco")
    print("c - Visualizar Dados da memoria")
    print("d - Visualizar Dados do disco")
    print("-------------------------------")
    print("e - Update")
    print("f - Commit")
    print("g - Checkpoint")
    print("h - Failure")
    print("i - Visualizar REDO e UNDO")
    print("-------------------------------")
    print("s - Sair do programa")
    print("-------------------------------")



while aux != 's': # laço de repetição que enquanto a variável aux for diferente de s ele continuará apresentando e realizando aquelas atividades
    menu()
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
        commit()
    elif aux == 'g':
       checkpoint()
    elif aux == 'h':
        failure()
    elif aux == 'i':
        viewRedoUndo()
    else:
        print("Programa encerrado")
        break