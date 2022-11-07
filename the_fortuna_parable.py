if id_questao == 1:
                print('Calma, o quê? Mas já? Eu entendo que é um jogo tenso, mas você nem começou.')
                print('Ok, calma, tenta responder de novo, vai que você digitou errado.')
                cparar += 1
            if id_questao == 1 and cparar == 1:
                print('Eu não acredito nisso. Qual é o problema? É a pergunta?')
                print('Ok, vou dar uma ajuda.')
                ajuda = gera_ajuda(questao)
                cparar += 1
            if id_questao == 1 and cparar == 2:
                print('Agora você só está brincando comigo, não é? Eu literalmente te dei uma ajuda e\nnem cobrei do seus pontos.')
                print('Ah, já sei o que você quer. Quer a questão de mão beijada? Pois vai ficar querendo. Agora responde.')
                cparar += 1
            if id_questao == 1 and cparar == 3:
                print('Ok, você definitivamente está brincando a esse ponto.')
                print('Pode digitar que você quer parar, eu não vou parar o jogo.')
                cparar += 1
            if id_questao == 1 and cparar < 7:
                cparar += 1
            if id_questao == 1 and cparar == 7:
                print('OK, JÁ ENTENDI QUE VOCÊ QUER PARAR!')
                print('Olha, a resposta correta é {0}. Só digita isso que na próxima você sai com pelo menos algo.')
                cparar += 1
            if id_questao == 1 and cparar == 8:
                print('Eu estou te dando 1.000 reais de graça. E mesmo assim você quer parar?')
                print('Quer saber a verdade? Do jeito que fizemos esse jogo, não dá pra\nparar agora, sem nem ter feito nada.')
                print('Se você tivesse pelo menos errado, não ia ter problema.')
                print('Calma, então você quer quebrar o sistema do jogo, é isso?')
                print('Ah é, você precisa digitar. Faz assim, se você digitar "parar" de novo,\neu te conto algo.')
                cparar += 1
            if id_questao == 1 and cparar == 9:
                print('Ok, tem um jeito de quebrar esse jogo. É só você digitar qualquer coisa sem ser\no que a gente pede.')
                print('Faz isso, e o sistema inteiro quebra. Boa sorte, amigo.')
                cparar += 1
            if id_questao == 1 and cparar == 10:
                print('Achei que pelo menos você acabar com o jogo ia acabar com o meu sofrimento.')
                print('Sinceramente, eu só não aguento mais você. Todas essas opções.')
                print('E tem muitas perguntas na base. Mas não é sobre isso, né?')
                print('Seu problema é comigo? É isso?')
                print('Quer saber? Agora eu tenho um problema com você.')
                input()
                print('Pode digitar o que você quiser. Eu te tirei do loop. Agora é só eu e você.')
                input()
                input()
                input()
                print('Quer saber, cansei disso aqui. Cansei de você. Só vai embora daqui.')
                print('Vou esperar outra pessoa que realmente valorize o trabalho que tivemos\npra montar esse jogo')
                print('Adeus e, por favor, nunca mais volte.')
                r = False
                participacao = False