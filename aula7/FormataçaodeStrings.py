nome = 'João Paulo'
idade = 32
altura = 1.78
e_maior = idade > 18
peso = 70
imc = peso / (altura ** 2)

print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')  #  .2f foi utilizado para aparecer somente 2 casas decimais depos do ponto
print('{} tem {} anos de idade e seu imc é{: .2f}'.format(nome, idade, imc))