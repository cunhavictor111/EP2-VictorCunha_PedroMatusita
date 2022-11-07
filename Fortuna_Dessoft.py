#pré-requisitos
import Funções.valida_lista
valido = valida_questoes(quest)
if len(valido) != 0:
    print('ERRO: Base de questões tem erros')
    exit()

#condições iniciais
lista_premios = [0,1000,5000,10000,30000,50000,100000,300000,500000,1000000]
dinheiro = 0 #índice
pulo = 3
ajuda = 2
ajuda_uma_vez = 0

nome = input('INFORME SEU NOME: ')

print('\nBEM-VINDO A FORTUNA DESSOFT {0}'.format(nome.upper()))

#manual
print('\n-----------------\nMANUAL\n-----------------\n')
print('Cada pergunta tem quatro alternativas: "A" , "B" , "C" , "D"\nVocê também tem direito de "ajuda" , "pula" , "parar"')
input('Aperte ENTER para continuar: ')

print('\nAgora, que você conhece as regras:\n\nQUE COMECE A FORTUNA DESSOFT!!')
