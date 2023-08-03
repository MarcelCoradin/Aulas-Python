"""
CONTRATANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- contagem de complexidade (ruim)
"""
velocidade = 61 # velocidade atual do carro
local_carro = 100 # local em que o carro está na estrada

RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 esta
RADAR_RANGE = 1 # A distância onde o radar pega

velocidade_do_carro_passou_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE) and velocidade > RADAR_1
carro_multado_radar_1 = carro_passou_radar_1 and velocidade_do_carro_passou_radar_1

if velocidade_do_carro_passou_radar_1:
    print('Velocidade carro passou do radar 1')

if carro_passou_radar_1:
    print('Carro passou radar 1')

if carro_passou_radar_1 and velocidade_do_carro_passou_radar_1:
    print('Carro multado em radar 1')




 #-------------------------------------------------------EXEMPLO DE CODIGO LIMPO USANDO O CHATGPT-------------------------------------------------------------------------------------------------

"""No exemplo que você compartilhou, podemos fazer algumas melhorias para tornar o código mais claro:

Uso de nomenclatura descritiva: Utilize nomes de variáveis e constantes que descrevam bem o que elas representam. Isso ajuda a entender o código mais facilmente.

Comentários para explicação: Adicione comentários para explicar partes importantes do código. Isso torna mais fácil para outras pessoas entenderem a lógica por trás de cada linha.

Evitar redundâncias: Algumas comparações podem ser simplificadas e combinadas, eliminando a necessidade de variáveis intermediárias."""

# Dados do radar 1
VEL_MAX_R1 = 60  # Velocidade máxima permitida pelo radar 1
LOCAL_R1 = 100  # Localização do radar 1
RADAR_RANGE = 1  # Alcance do radar em relação ao local definido

# Dados do carro
velocidade_carro = 61  # Velocidade atual do carro
local_carro = 100  # Localização atual do carro na estrada

# Verificações
velocidade_do_carro_passou_radar_1 = velocidade_carro > VEL_MAX_R1
carro_passou_radar_1 = LOCAL_R1 - RADAR_RANGE <= local_carro <= LOCAL_R1 + RADAR_RANGE
carro_multado_radar_1 = carro_passou_radar_1 and velocidade_do_carro_passou_radar_1

# Mensagens
if velocidade_do_carro_passou_radar_1:
    print('Velocidade do carro passou do radar 1.')

if carro_passou_radar_1:
    print('Carro passou pelo radar 1.')

if carro_multado_radar_1:
    print('Carro multado no radar 1.')


"""
Com essas melhorias, o código se torna mais fácil de entender e ler. A nomenclatura das variáveis e constantes foi tornada mais descritiva, 
e comentários foram adicionados para explicar a finalidade de cada seção do código.

Lembre-se de que a legibilidade e a organização do código são habilidades essenciais para um programador, 
pois facilitam a colaboração em projetos e tornam a manutenção do código mais eficiente. 
Continue praticando esses conceitos e aprimorando suas habilidades em Python. Se tiver mais perguntas ou precisar de mais exemplos, estou aqui para ajudar! Boa programação! :)
"""
