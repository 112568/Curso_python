"""
Operadores Relacionais
==, >, >=, <, <=, !=
"""
"""
print(2 == 2)
print(2 > 2)
print(2 >= 2)
print(2 < 2)
print(2 <= 2)
print(2 != 2)
"""

nome = input('Digite seu nome: ')
idade = input('Digite a sua idade: ')

idade = int(idade)

idade_limite = 18

if idade >= idade_limite:
    print(f'{nome} pode pegar o empréstimo')
else:
    print(f'{nome} Não pode pegar o empréstimo')
