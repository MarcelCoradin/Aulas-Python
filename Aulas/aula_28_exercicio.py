nome = input('Digite o seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')

    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')

    print(f'Seu nome tem {len(nome)}, letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[-1]}')
else:
    print(f'Desculpe, você deixou campos vazios')


# nome = input('Digite o seu nome: ').strip()  # Remover espaços extras no início e fim do nome
# idade = input('Digite sua idade: ')

# if nome and idade.isdigit():  # Verificar se o nome não está em branco e se a idade é um número inteiro
#     idade = int(idade)  # Converter a idade para um número inteiro

#     print(f'Seu nome é {nome}')
#     print(f'Seu nome invertido é {nome[::-1]}')

#     if ' ' in nome:
#         print('Seu nome contém espaços')
#     else:
#         print('Seu nome não contém espaços')

#     print(f'Seu nome tem {len(nome)} letras')
#     print(f'A primeira letra do seu nome é {nome[0]}')
#     print(f'A última letra do seu nome é {nome[-1]}')
# else:
#     print('Desculpe, verifique se você digitou seu nome e idade corretamente.')
