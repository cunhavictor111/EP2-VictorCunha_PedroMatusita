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