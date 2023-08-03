"""
Flag (Bandeira) - Marcar um local
None = não valor
is e is not  = é ou não é (tipos, valor, indentidade)
id = indentidade
"""

condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')

if passou_no_if in None:
    print('Não passou no if')

else:
    print('Passou no if')




"""
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Vamos entender o que está acontecendo aqui:

1. condicao = False: Aqui, condicao é uma variável do tipo booleano que foi definida como False.

2. passou_no_if = None: Aqui, passou_no_if é uma variável inicializada com o valor especial None. Isso significa que ela não possui nenhum valor atribuído no momento.

3. O código usa uma estrutura condicional if-else para avaliar a variável condicao. Se condicao for True, ele define passou_no_if como True e exibe "Faça algo". Caso contrário, exibe "Não faça algo".

4. Após a estrutura condicional, há outra estrutura if-else. Neste caso, ele está verificando se passou_no_if é None usando o operador is.

O operador is verifica se duas variáveis têm a mesma identidade, ou seja, se apontam para o mesmo objeto na memória.

    Se passou_no_if for None, a mensagem "Não passou no if" será exibida.

    Caso contrário, a mensagem "Passou no if" será exibida.

Como passou_no_if foi inicializado como None e não foi alterado na primeira estrutura condicional, ele permanece com o valor None, e a mensagem "Não passou no if" será exibida.

Isso é apenas um exemplo introdutório, e tenho certeza de que você aprenderá muito mais sobre esses conceitos em sua próxima aula. 

"""