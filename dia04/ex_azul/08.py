#Faça um programa que receba 4 alturas, armazene em uma lista e depois mostre a soma dessas alturas.

#%%
h1 = int(input("Digite a altura inicial:"))
h2 = int(input("Digite a segunda altura :"))
h3 = int(input("Digite a terceira altura :"))
h4 = int(input("Digite a quarta altura :"))

alturas = [h1,h2,h3,h4]

print("A soma das alturas é: ", sum(alturas),".")
# %%
