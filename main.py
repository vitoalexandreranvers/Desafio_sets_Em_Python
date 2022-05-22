#Desafio com 'Sets'

'''
Criar um programa que gera 3 listas de acordo com a necessidade logo abaixo:

Lista 1 = Funcionários que tem carro e trabalham a noite
Lista 2 = Funcionários que tem carro e trabalham durante o dia
Lista 3 = funcionários que não tem carro
'''


funcionarios = ['Ana', 'Marcos', 'Alice', 'Pedro', 'Sofia', "Bruno", 'Melissa']
turno_dia    = ['Ana', 'Marcos', 'Alice', 'Melissa']
turno_noite  = ['Pedro', 'Sofia', 'Bruno']
tem_carro    = [ 'Marcos', 'Alice', 'Bruno', 'Melissa']

#LISTA 1
lista1 = set(tem_carro).intersection(turno_noite)
print("Funcionários que tem carro e trabalham a noite --> " , lista1)

#LISTA 2
lista2 = set(tem_carro).intersection(turno_dia)
print("Funcionários que tem carro e trabalham durante o dia --> " , lista2)

#LISTA 3
lista3 = set(funcionarios).difference(tem_carro)
print("funcionários que não tem carro --> " , lista3)