def operacao(op, *num):
    # Função que realiza operações matemáticas.
    
    # Argumentos:
    # op (str): A operação a ser realizada. Pode ser 'soma' ou 'mult'.
    # *num (float): Números para executar a operação.
    
    # Retorna:
    # float: O resultado da operação.
    
    # Observações:
    # - Se op for 'soma', a função soma todos os números fornecidos.
    # - Se op for 'mult', a função multiplica todos os números fornecidos.
    
    total = 0  # Inicializa o total como zero

    if op == "soma":  # Se a operação for soma
        for i in num:  # Percorre todos os números fornecidos
            total += i  # Adiciona o número ao total

    elif op == "mult":  # Se a operação for multiplicação
        total = 1  # Inicializa o total como 1 para a multiplicação
        for i in num:  # Percorre todos os números fornecidos
            total *= i  # Multiplica o número ao total

    return total  # Retorna o resultado da operação

# Exemplo de uso da função para somar 10 + 20 + 100
resultado_soma = operacao("soma", 10, 20, 100)
print("Resultado da soma:", resultado_soma)

# Exemplo de uso da função para multiplicar 10 * 20 * 100
resultado_mult = operacao("mult", 10, 20, 100)
print("Resultado da mult:", resultado_mult)


#%%
      
    dados = ['teo', 'calvo']

    nome = dados[0]
    sobrenome = dados[1]

    print(nome)

#ooooooou:
#%%
dados = ['teo', 'calvo']
  
nome, sobrenome = dados

print(nome)
print(sobrenome)
# %%

# Definindo uma lista chamada dados contendo os valores 'teo' e 'calvo'
dados = ['teo', 'calvo']

# Desempacotando a lista dados em variáveis individuais
# nome irá receber o primeiro elemento da lista (índice 0), que é 'teo'
# sobrenome irá receber o segundo elemento da lista (índice 1), que é 'calvo'
# O *_ ignora o restante dos elementos da lista
nome, sobrenome, *_ = dados

# Imprimindo o valor da variável nome
print(nome)  # Saída: teo

# Imprimindo o valor da variável sobrenome
print(sobrenome)  # Saída: calvo

#%%

#Como fazer 'a' ter o valor de 'b', e 'b' ter o valor de 'a'?

a = 10
b = 20

c = a
a = b
b = c

#%%
#Porém, atalho no python:
a = 10
b = 20

a, b = [b,a]