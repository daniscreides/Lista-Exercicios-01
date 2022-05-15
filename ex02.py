#(Para profissionais!) O custo final de um carro novo para seu consumidor é dado pela soma entre o  custo de fábrica, a percentagem do distribuidor (obtida do custo de fábrica) e ainda os impostos (obtidos do custo de fábrica). Supondo que a percentagem do distribuidor seja 10% e os impostos 45%, escreva um programa em Python capaz de processar e calcular o custo final de um carro. Este programa deve ler o custo de fábrica inicial do carro e exibir o custo final calculado para seu comprador.

valor_carro = float (input ("Digite o valor do carro sem os encargos: "))

valor_distribuidor = ( valor_carro * 0.1 )
valor_impostos = ( valor_carro * 0.45 )

valor_total = ( valor_carro + valor_distribuidor + valor_impostos )

print ( "Valor com encargos é: " + str(valor_total) )