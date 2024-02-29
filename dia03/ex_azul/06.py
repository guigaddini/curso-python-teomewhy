#Faça um programa que verifique se o item que a pessoa 
# escolheu para comprar na loja está na lista: 
# laranja, cerveja, miojo, carvão, abobrinha.

lista = "laranja, cerveja, miojo, carvão, abobrinha"

item = input("O que você quer comprar? [laranja, cerveja, miojo, carvão, abobrinha] ")

if item in lista:
    print("Top! Pode ir pro caixa")

else:
    print("Puts, estamos em falta")
