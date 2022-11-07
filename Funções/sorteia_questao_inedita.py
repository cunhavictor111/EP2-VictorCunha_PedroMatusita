def sorteia_questao_inedida(questoes,nivel,jasort):
    while True:
        qadd = sorteia_questao(questoes,nivel)
        if qadd not in jasort:
            jasort.append(qadd)
            break

    return qadd