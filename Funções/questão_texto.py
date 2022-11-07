def questao_para_texto(questao,idq):
    txt = '----------------------------------------\nQUESTAO {0}\n\n{1}\n\nRESPOSTAS:\nA: {2}\nB: {3}\nC: {4}\nD: {5}\n'.format(idq,questao['titulo'],questao['opcoes']['A'],questao['opcoes']['B'],questao['opcoes']['C'],questao['opcoes']['D'])

    return txt