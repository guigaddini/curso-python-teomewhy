# Faça um programa que receba uma quantidade indefinida de valores correspondentes a “saldo em conta”
# MAAAAS quando o usuário apertar “enter” sem digitar valor algum, o programa para de receber valores
# EEEEE exibe a soma te todos os valores digitados anteriormente.

total = 0

entrada = "x"
while True:
    entrada = input ("Entre com o valor do saldo: ")

    if entrada == "":
        break
    total += float(entrada)

print(total)