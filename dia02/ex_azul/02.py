# %%

# Faça um programa que vende uma garrafa de água:
# Se o cliente escolher água mineral natural, será cobrado R$1,50
# Se o cliente escolher água mineral com gás, será cobrado R$2,50
# Altere o programa anterior para considerar a quantidade de água


escolha = input("Água com ou sem gás? [com/sem]")

quantidade = int(input("Quantas águas vc deseja?"))

preco = 0

if escolha == "sem":
    preco = quantidade * 1.50

elif escolha == "com":
    preco = quantidade * 2.50

else:
    print("Faça uma escolha válida!")

print("Você me deve R$", preco,".")
# %%