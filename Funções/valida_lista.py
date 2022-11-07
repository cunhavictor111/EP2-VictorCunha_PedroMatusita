def valida_questoes(questoes):
    erros = []
    for q in questoes:
        dic = valida_questao(q)
        erros.append(dic)

    return erros