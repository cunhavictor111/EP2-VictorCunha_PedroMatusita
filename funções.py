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

    
def transforma_base(questoes):
    dificuldade = {}
    for q in questoes:
        diff = q['nivel']

        #defini
        if diff not in dificuldade:
            dificuldade[diff] = []

        dificuldade[diff].append(q)

    return dificuldade

def questao_para_texto(questao,idq):
    txt = '----------------------------------------\nQUESTAO {0}\n\n{1}\n\nRESPOSTAS:\nA: {2}\nB: {3}\nC: {4}\nD: {5}\n'.format(idq,questao['titulo'],questao['opcoes']['A'],questao['opcoes']['B'],questao['opcoes']['C'],questao['opcoes']['D'])

    return txt

def sorteia_questao(questoes,nivel):
    q_nivel = questoes[nivel]
    sort = random.randint(0,len(q_nivel)-1)
    return q_nivel[sort]

def sorteia_questao_inedida(questoes,nivel,jasort):
    while True:
        qadd = sorteia_questao(questoes,nivel)
        if qadd not in jasort:
            jasort.append(qadd)
            break

    return qadd

def valida_questao(questao):
    valida = {}

    #quatro chaves
    if len(questao) != 4:
        valida['outro'] = 'numero_chaves_invalido'
    #chaves diferentes
    check = ['titulo','nivel','opcoes','correta']
    

    #se estao
    for chave in check:
        if chave not in questao:
            valida[chave] = 'nao_encontrado'

    #titulo
    if 'titulo' in questao:
        tit = questao['titulo'].strip()
        if len(tit) == 0:
            valida['titulo'] = 'vazio'

    #nivel
    diff = ['facil','medio','dificil']
    if 'nivel' in questao:
        if questao['nivel'] not in diff:
            valida['nivel'] = 'valor_errado'

    #opcoes
    if 'opcoes' in questao:
        t4 = False
        if len(questao['opcoes']) != 4:
            valida['opcoes'] = 'tamanho_invalido'
        else:
            t4 = True

        if t4 == True:
            v4 = True
            op = ['A','B','C','D']
            if len(questao['opcoes']) != 4:
                valida['opcoes'] = 'chave_invalida_ou_nao_encontrada'
                v4 = False
                
            for alt in questao['opcoes']:
                if alt not in op:
                    valida['opcoes'] = 'chave_invalida_ou_nao_encontrada'
                    v4 = False

            if v4 == True:
                for alt in questao['opcoes']:
                    resp = questao['opcoes'][alt].strip()
                    if len(resp) == 0:
                        if 'opcoes' not in valida:
                            valida['opcoes']= {}
                        
                        valida['opcoes'][alt] = 'vazia'

    #correta
    op = ['A','B','C','D']
    if 'correta' in questao:
        if questao['correta'] not in op:
            valida['correta'] = 'valor_errado'

    return valida

def valida_questoes(questoes):
    erros = []
    for q in questoes:
        dic = valida_questao(q)
        erros.append(dic)

    return erros