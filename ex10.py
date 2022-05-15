nome_aluno = input ( "Digite seu nome: " )
nota1 = float (input ( "Digite sua primeira nota (Ex: 8.5): "))
nota2 = float (input ( "Digite sua segunda nota (Ex: 8.5): "))

media = (nota1 + nota2) /2

print ( "Olá, " + nome_aluno + "!" )
print ( "Sua média final é: " + "{:.1f}".format (media) )