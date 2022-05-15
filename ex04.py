#(Para profissionais!) Escreva um programa em Python que seja capaz de calcular o número de litros no abastecimento em um posto de combustíveis. O programa deverá receber a quantia em reais (e.g., 335.90), o preço do combustível (e.g., 7.27) e seja capaz de exibir, com duas casas decimais, quantos litros de combustível serão colocados no tanque.


valor_carteira = float ( input ( "Informe o valor na carteira: " ))
valor_gasolina = float ( input ( "Informe o valor da gasolina: " ))

litros =  ( valor_carteira / valor_gasolina )

print ( " Você irá colocar " + "{:.1f}".format (litros) + " litros no tanque. " )