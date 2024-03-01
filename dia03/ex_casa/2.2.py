#%%
# Faça um programa que receba um número.
# Verifique se o número informado é par ou ímpar.
#Exiba o resultado da seguinte maneira:

	#O número x é impar
# ou
	#O número x é par

numero = int(input("Olá, digite um número: "))

if numero % 2 == 0: #se o resto da divisão por 2 = 0, é par!
    print("O número", numero, "é par!")
          
else:
    print("O número", numero, "é ímpar!")
# %%
