#%%

# Dicionários (ou mapas)
# Chaves associadas a valores (e os valores podem ter valores inclusos)

dados = {"nomes": "Téo", 
         "sobrenome": "Calvo", 
         "idade": 31,
         "bichinhos": ["Banguela", "Madonna"],
         "filhos": [{"nome": "Maria", "idade": 2}, {"nome": "Raul", "idade":1}]}

nome = dados["nomes"]
print(nome)

# %%
#Retornar as chaves:
chaves = dados.keys()
print(chaves)

#Retornar os valores:
dados = dados.values()
print(dados)

# %%

#Retornar os itens (chave e valor):
itens = dados.items()
print(itens)
# %%
