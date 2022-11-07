#import
from funções import valida_questoes
from funções import gera_ajuda
from funções import questao_para_texto
from funções import sorteia_questao_inedida

from lib_questões import quest

#pré-requisitos
valido = valida_questoes(quest)
for questao in valido:
    if len(questao) != 0:
        print('ERRO: Base de questões tem erros')
        exit()

#condições iniciais
lista_premios = [0,1000,5000,10000,30000,50000,100000,300000,500000,1000000]
dinheiro = 0 #índice
pulo = 3
ajuda = 2
ajuda_uma_vez = 0
questoes_ja_sorteadas = []
id_questao = 1

nome = input('INFORME SEU NOME: ')

print('\nBEM-VINDO A FORTUNA DESSOFT {0}'.format(nome.upper()))

#manual
print('\n-----------------\nMANUAL\n-----------------\n')
print('Cada pergunta tem quatro alternativas: "A" , "B" , "C" , "D"\nVocê também tem direito de "ajuda" , "pula" , "parar"')
input('Aperte ENTER para continuar: ')

print('\nAgora, que você conhece as regras:\n\nQUE COMECE A FORTUNA DESSOFT!!')
