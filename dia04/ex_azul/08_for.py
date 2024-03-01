#Faça um programa que receba 4 alturas, armazene em uma lista e depois mostre a soma dessas alturas.

#%%

alturas = []

for i in range (4):
    a = int(input(f"Entre com as alturas em cm {i+1}: ")) #f = formatação de string: passando a variável externa pra dentro da string.
    alturas.append(a)


soma = sum(alturas)
print("A soma das alturas é: ", soma,".")
# %%
