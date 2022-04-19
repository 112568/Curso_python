usuario = input('Nome de usuário:')
senha = input('Senha do usuário:')

usuario_bd = 'joao'
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
    print('O usuário esta logado')
else:
    print('Usuário ou senha inválidos')