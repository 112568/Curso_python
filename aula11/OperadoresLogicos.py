"""
Operadores lógicos
and, or, not
in e not in
"""
#  (verdadeiro e verdadeiro)= verdadeiro
#  (verdadeiro e falso)= falso
comparacao1 and comparacao2

# (verdadeiro ou verdadeiro) qualquer uma que for verdadeiro, retorna valor verdadeiro
comp1 or comp2

# funçao (NOT) é utilizado para inverter a expreção.

# expreçao in
nome = 'Joao Paulo'

if 'Jo' in nome:
    print("Existe.")
else:
    print('Nao existe.')
    
#  expreçao not in
nome = 'Joao Paulo'

if 'Jo' not in nome:
    print("Executei.")
else:
    print('Existe o texto.')