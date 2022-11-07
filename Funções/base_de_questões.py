def transforma_base(questoes):
    dificuldade = {}
    for q in questoes:
        diff = q['nivel']

        #defini
        if diff not in dificuldade:
            dificuldade[diff] = []

        dificuldade[diff].append(q)

    return dificuldade