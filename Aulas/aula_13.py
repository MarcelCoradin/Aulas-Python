# Solicitta informações do usuário

nome = input('Digite seu nome: ')
altura_str = input('Digite sua altura: ')
peso_str = input('Digite seu peso: ')

# Converter as informações de altura e peso para números de pontos flutuantes

altura = float(altura_str)
peso = float(peso_str)

# Calculo do IMC

imc = peso / altura ** 2

# Saida do resultado

"f-strings"
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu IMC é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)