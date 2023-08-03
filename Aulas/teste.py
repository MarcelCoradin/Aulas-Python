# Dados de acesso (exemplo)
usuario_valido = 'usuario123'
senha_valida = 'senha123'

def fazer_login():
    tentativas = 3

    while tentativas > 0:
        nome_usuario = input('Digite o nome de usuário: ')
        senha = input('Digite a senha: ')

        if nome_usuario == usuario_valido and senha == senha_valida:
            print('Login bem-sucedido!')
            return True
        else:
            tentativas -= 1
            print(f'Acesso negado! Tentativas restantes: {tentativas}')

    print('Você excedeu o número máximo de tentativas. Tente novamente mais tarde.')
    return False

if fazer_login():
    # Aqui você pode colocar o código que será executado após o login bem-sucedido
    print('Bem-vindo(a) à aplicação!')
    # Exemplo de funcionalidade após o login:
    print('Aqui você pode executar outras ações e funcionalidades.')

# Se o login falhar, o programa será encerrado.
