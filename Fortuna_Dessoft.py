#import
from funções import valida_questoes
from funções import gera_ajuda
from funções import questao_para_texto
from funções import sorteia_questao_inedida

from lib_questões import quest
from lib_questões import base

#pré-requisitos
valido = valida_questoes(quest)
for questao in valido:
    if len(questao) != 0:
        print('ERRO: Base de questões tem erros')
        exit()

#condições iniciais
lista_premios = [0,1000,5000,10000,30000,50000,100000,300000,500000,1000000]
dinheiro = 0 #índice
pulos = 3
ajudas = 2
ajuda_uma_vez = 0
questoes_ja_sorteadas = []
id_questao = 1
cparar = 0 # Você vai entender
nivel = 0 # É uma variável pra automatizar o jogo e saber qual é o nível da questão
participacao = True # É uma variável de participação só pra comentários e tudo mais.

nome = input('INFORME SEU NOME: ')

print('\nBEM-VINDO A FORTUNA DESSOFT {0}'.format(nome.upper()))

#manual
print('\n-----------------\nMANUAL\n-----------------\n')
print('Cada pergunta tem quatro alternativas: "A" , "B" , "C" , "D"\nVocê também tem direito de "ajuda" , "pula" , "parar"')
input('Aperte ENTER para continuar: ')

print('\nAgora que você conhece as regras:\n\nQUE COMECE A FORTUNA DESSOFT!!')
print('-----------------')
while participacao == True:
    if id_questao <= 3:
        nivel = 'facil' 
    elif id_questao <= 6:
        nivel = 'medio'
    else:
        nivel = 'dificil'
    questao = sorteia_questao_inedida(base,nivel,questoes_ja_sorteadas)
    questoes_ja_sorteadas.append(questao)
    print(questao_para_texto(questao,id_questao))
    r = True # Variável pra loop de resposta
    while r == True:
        resposta = input('Qual é a sua resposta? ')
        if resposta == questao['correta']:
            print('E está... certa a resposta! Você agora tem {0} reais!'.format(lista_premios[dinheiro+1]))
            id_questao += 1
            dinheiro += 1
            input('Aperte CONTINUAR para prosseguir com o jogo! ')
            r = False
        elif resposta == 'ajuda':
            ajuda = gera_ajuda(questao)
            ajudas -= 1
        elif resposta == 'pula':
            if nivel == 'facil':
                print('Eu acharia melhor guardar para as mais difíceis, mas tudo bem, cada um faz suas escolhas.')
            print('Ok, questão pulada.')
            r = False
            pulos -= 1
        elif resposta == 'parar':
            if nivel == 'facil':
                print('Parar enquanto está fácil, né? Bom, eu não te julgo.')
            if nivel == 'medio':
                print('Boa! Conseguiu garantir um prêmio gordo e é sempre bom não arriscar.')
            if nivel == 'dificil':
                print('Logo quando estava ficando interessante!')
            print('Obrigado por participar do FORTUNA DESSOFT!!')
            r = False
            participacao = False