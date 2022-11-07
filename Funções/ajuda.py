import random

def gera_ajuda(questao):
    n_ajuda = random.randint(1,2)
    n_para_letra = {1:"A",2:'B',3:"C",4:'D'}
    retirada = []

    correta = questao['correta']

    while n_ajuda != 0:
        retira = n_para_letra[random.randint(1,4)]
        if retira != correta and retira not in retirada:
            n_ajuda -= 1
            retirada.append(questao['opcoes'][retira])
    
    if len(retirada) ==2:
        return 'DICA:\nOpções certamente erradas: {0} | {1}'.format(retirada[0],retirada[1])
    else:
        return'DICA:\nOpções certamente erradas: {0}'.format(retirada[0])