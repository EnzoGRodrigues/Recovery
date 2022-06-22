import os

logDisco = []  # log do disco
logMemoria = [] # buffer do log
memoriaDado = [5000,7000,9000,11000,13000] # buffer de dados 
discoDado = [5000,7000,9000,11000,13000] # dados do disco
redo = [] # lista para armazenar transações redo
undo = [] # lista para armazenar transações undo
previaMemoria = [] # lista para armazenar os valores antigos e fazer undu no disco
arquivoDiscoDados = 'discodado.txt' # arquivo de texto para receber valores que ficam no dado dos disco
arquivoDiscoLog = 'discolog.txt' # arquivo de texto para receber valores que ficam no log do disco



def commit():
        t = input("Digite a transação que deseja commitar: ")
        logDisco[:] += ([s for s in logMemoria if t in s])
        redo[:] += ([s for s in logMemoria if t in s]) #
        if(os.path.exists(arquivoDiscoLog)):
            f = open(arquivoDiscoLog, "w")
            for i in logDisco:
                f.write(str(i)+"\n")
            f.close()

def checkpoint():
        if(os.path.exists(arquivoDiscoDados)):
            f = open(arquivoDiscoDados, "w")
            f.write(str(memoriaDado[:])+"\n")
            f.close
            previaMemoria[:] += memoriaDado[:]
        else:
            print("O arquivo \"arquivoDiscoDados.txt\" nao existe!")
        if(os.path.exists(arquivoDiscoLog)):
            f = open(arquivoDiscoLog, "w")
            for i in logMemoria:
                f.write(str(i)+"\n")
            f.write(str("<CHECKPOINT>\n"))
            f.close
        else:
            print("O arquivo \"logDisco.txt\" nao existe!")   

def falha():
    undo[:] += ([s for s in logMemoria if s not in redo])
    print("previaMemoria:",previaMemoria)
    for i in undo:
        #print("ID:",i[:][1])
        posicao = i[:][1]
        #print("disco:",discoDado[posicao-1])
        val = int(i[:][3])
        discoDado[posicao-1] = val
        previaMemoria[posicao-1] = val
        #print("Teste apos falha:", discoDado)  

    logMemoria.clear() 
    memoriaDado.clear()   
    print("previaMemoria apos falha:",previaMemoria,"\n\n\n")
    with open('discodado.txt','w')as arquivoDiscoDados:
            arquivoDiscoDados.write(str(previaMemoria))

    

def update():
        numTransacao = input("Digite a transacao: ")
        idValor = int(input("ID da pessoa: "))
        velhoVal = discoDado[idValor - 1]
        novoVal = int(input("Digite o valor: "))
        logMemoria[:] += [(numTransacao,idValor,"salario",velhoVal,novoVal)]
        memoriaDado[idValor - 1] = novoVal
        print("Sucesso ao fazer Update!")
#Transação | ID da pessoa | atributo | valor Antigo | Valor novo
def menu():
    print("MEMORIA:",memoriaDado)
    print("Tx MEMORIA:",logMemoria,"\n")
    print("a - Visualizar Log da memoria")
    print("b - Visualizar Log do disco")
    print("c - Update")
    print("d - Checkpoint")
    print("e - Falha")
    print("f - Commit")
    print("g - Visualizar dados no disco")
    print("h - Visualizar dados na memoria")
    print("i - Visualizar dados UNDO e REDO")
    print("s - Sair do programa")
    print("Digite a opcao: ")

i = None
while i != 's':
    menu()
    i = input().lower()
    if i == 'a':
        print(logMemoria)
    elif i == 'b':
        if(os.path.exists(arquivoDiscoLog)):
            f = open(arquivoDiscoLog, "r")
            print(f.read())
            f.close
        else:
            print("O arquivo \"logDisco.txt\" nao existe!")
    elif i == 'c':
        update()
    elif i == 'd':
        checkpoint()
    elif i == 'e':
        #chamar Undo e Redo
        falha()
    elif i == 'f':
        commit()
    elif i == 'g':
        if(os.path.exists(arquivoDiscoDados)):
            f = open(arquivoDiscoDados, "r")
            print(f.read())
            f.close
            #print(discoDado)
        else:
            print("O arquivo \"arquivoDiscoDados.txt\" nao existe!")
    elif i == 'h':
        print(memoriaDado)
    elif i == 'i':
        print("REDO",redo,\
              "\nUNDO",undo,
              "mt-Var discoDado:",previaMemoria
              )
    else:
        print("Saindo...")
        break