# Este é um objeto de estudo para aprender a linguagem de programação Python

print('Hello Word, vamos lá!')


# Atribuição de variáveis
vendas = 1000 # variável recebe
custo = 300
lucro = vendas - custo

print('O lucro foi de:', lucro)


#Atividades:

#Desafio 1:
"""Criar um script em Python que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas de acordo com o valor digitado."""

#resultado
nome = input('Qual o seu nome?')
print('Olá ' + nome + ' seja bem-vindo(a)!')

##################################################

#Desafio 2:
"""Criar um script em Python que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada."""

#resultado
print('Insira as informações abaixo:')
dia = input('Dia = ')
mes = input('Mês = ')
ano = input('Ano = ')
print('Você nasceu no dia ' + dia + ' de ' + mes + ' de ' + ano + '. Correto?')

##################################################

#Desafio 3
"""Criar um script em Python que leia dois números e tente mostrar a soma entre eles."""

#resultado
print('Insira os números para soma:')
primeiro_numero = input('Primeiro Número = ')
segundo_numero = input('Segundo Número = ')

#Convertendo para tipo numérico
primeiro_numero = int(primeiro_numero)
segundo_numero = int(segundo_numero)

resultado = (primeiro_numero + segundo_numero)
print('O resultado da soma é: ' + str(resultado)) #concatenando e convertendo para string novamente com str()