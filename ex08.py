""" Exercicio 08
(Para profissionais!) O programa de uma indústria realiza a folha mensal de pagamentos de seus empregados baseando-se nas seguintes regras:

Deve-se, primeiro, ler os dados de cada funcionário (matrícula, nome e salário bruto);

Depois, o programa irá/deve processar o salário e exibir na tela o seu contracheque, cujo formato é dado a seguir (próxima página):

Matrícula: 
Nome completo:
Salário Bruto:
Dedução INSS:
Salário Líquido:

Onde: o desconto do INSS é 15% do salário bruto e o salário líquido é a diferença entre o salário bruto e a dedução do INSS. """


nome = input ("Nome do funcionário: ")
matricula = int (input("Matrícula do funcionário: "))
salario_bruto = float (input("Salário bruto do funcionário: "))

inss = (salario_bruto * 0.15) 

salario_liquido = (salario_bruto - inss)

print ( "CONTRACHEQUE" )
print ( "Matrícula: " + str(matricula) )
print ( "Nome: " + nome )
print ( "Salario bruto: " + "{:.2f}".format (salario_bruto) )
print ( "INSS: " + "{:.2f}".format (inss) )
print ( "Salario liquido: " + "{:.2f}".format (salario_liquido) )

