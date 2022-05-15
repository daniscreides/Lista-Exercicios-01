#Escreva um programa de “Reajustar Salário”, capaz de receber o nome completo e o salário inicial de um empregado e possa imprimir, no final, o nome e este salário reajustado em 20%.

nome_funcionario = input ("Digite o nome do funcionário: ")
salario_atual = float ( input ( "Digite o salário atual do funcionário: "))

salario_reajuste = ( salario_atual * 0.2 + salario_atual)

print ( "Salário com reajuste desse funcionário é: " + str( salario_reajuste ) )