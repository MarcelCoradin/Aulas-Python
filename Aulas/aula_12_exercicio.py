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

print(nome, 'tem', altura, 'de altura')
print('pesa', peso, 'kg e seu IMC é de')
print(imc)



"""
RESOLUÇÃO DA ATIVIDADE COM BASE NO QUE APRENDEMOS NAS AULAS ANTERIORES!

nome = 'Marcel Augusto Coradin'
altura = 1.79
peso = 119

# Cálculo do IMC
imc = peso / altura ** 2

# Saida dos resultados
print(nome, 'tem', altura, 'de altura')
print('pesa', peso, 'kg e seu IMC é de', int(imc))

"""