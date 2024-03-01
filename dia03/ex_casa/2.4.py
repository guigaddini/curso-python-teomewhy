#Faça um programa que receba 4 notas de um aluno. 
#Retorne a média dessas notas, a menor e a maior nota:

#Média: x
#Menor: y
#Maior: z

#%%

#criei uma lista:
notas = [int(input("Digite a primeira nota que vc tirou: ")),

int(input("Digite a segunda nota que vc tirou: ")),

int(input("Digite a terceira nota que vc tirou: ")),

int(input("Digite a quarta nota que vc tirou: "))]

###

media = sum(notas)/len(notas)
#sum() = soma todos os elementos da lista
#len() = quantidade de elemntos da lista

menor = min(notas)
maior = max(notas)

print("A média dessas notas é:", media, ". A nota mais alta é:", maior, "e a mais baixa é:", menor, ".")

# %%
