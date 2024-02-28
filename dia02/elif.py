idade = int(input("Entre com a sua idade: "))

if idade <18:
    print("Você é menor de idade")
    print("Vai pra casa beber leite!")

elif idade >=90:
    print("Tome cuidado, você já tem certa idade")

else:
    print("Beba à vontade!")
    print("Você é maior de idade!")

# elif = como se houvesse outro if dentro do else. 

# podem ter quantos elif você quiser
    
#if e else só podem ter um de cada
    
#%%
#Versão 2.0:
    
if 18 <= idade >= 89:
    print("Beba à vontade!")
    print("Você é maior de idade!")

elif idade >= 90:
    print("Você precisa se cuidar!")