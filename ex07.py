#A partir de três notas de um estudante, prepare um algoritmo para “Calcular Média com Pesos”, capaz de calcular a média final com pesos de notas 20%, 30% e 50%, respectivamente. Ao final, o programa deve imprimir o nome do aluno, suas notas parciais e sua média final.

aluno = input ( "Informe o nome do aluno: " )
nota1 = float (input ("Informe a 1ª nota: "))
nota2 = float (input ("Informe a 2ª nota: "))
nota3 = float (input ("Informe a 3ª nota: "))

media = (nota1/2) + (nota2/3) + (nota3/5) / 10

print ("Média final: " + "{:.2f}".format (media))