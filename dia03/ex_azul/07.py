#Faça um programa que conte quantas vezes a letra “a” aparece em uma palavra

palavra = input("Digite uma palavra: ")

qtde = 0
for i in palavra:
    if i == "a":
        qtde += 1

print("A letra 'a' possui", qtde, "ocorrencias na palavra", palavra)