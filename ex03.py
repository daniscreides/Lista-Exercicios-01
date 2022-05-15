#Escreva um programa em Python capaz de receber a idade de uma pessoa e exibir o valor equivalente em segundos. Teste o programa usando valores de idades como 18, 56 ou 94 anos;


idade = int (input ( "Digite sua idade: " ))

idade_em_segundos = ( idade * 365 * 24 * 60 * 60 )

print ("sua idade em segundos é: " + str (idade_em_segundos))