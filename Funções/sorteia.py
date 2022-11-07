import random

def sorteia_questao(questoes,nivel):
    q_nivel = questoes[nivel]
    sort = random.randint(0,len(q_nivel)-1)
    return q_nivel[sort]
    