#(Para profissionais!) Um cliente resolveu poupar e efetuou um depósito (em R$) num Banco em uma conta poupança. Neste banco, o valor do rendimento da poupança é fixo de 1% a cada mês decorrido. Com base neste cenário, escreva um programa em Python que leia o montante inicial depositado e o tempo (em meses) que o dinheiro ficará aplicado na conta. O programa deve calcular e exibir na tela o rendimento (i.e., quanto dinheiro esta conta irá acumular) após a passagem destes meses. Assuma que cliente não efetuará nenhuma retirada de dinheiro desta conta poupança até lá.

valor = float ( input ( " Digite o valor do deposito: ") )

meses = int ( input ( " Digite o tempo que ficará guardado em meses: ") )

rendimentos = valor * ( ( ( 1 + 0.01 ) ** meses ) - 1 )

print ( " Seus rendimentos são: " + "{:.2f}".format(rendimentos) )
