# %%

minha_lista_vazia = []
print(minha_lista_vazia)

# %%

minha_lista = ["Teo", "Calvo", 31, 1.82]
print(minha_lista)
# %%

minha_lista[0] #na posição(índice) 0 - o primeiro elemento do índice
# %%

minha_lista[3]
# %%

len(minha_lista) #tamanho da lista
# %%

indice = len(minha_lista)-1 #pegar o ultimo elemento da lista
print(indice)

#%%
#ou, resumindo:
minha_lista[-1]

#%%
minha_lista[-2] #penúltimo item da lista

#---------------------------

#%%
#Fatiamento de listas:

#Slice de Lista só com nome e sobrenome:
minha_lista[0:2] # início:fim
#começar onde vc quer e subtrair o começo

# %%

minha_lista[1:3] # segundo elemento:terceiro elemento
# %%

minha_lista [0:-1] #todos os elementos, menos o último
# %%

minha_lista [0:int(len(minha_lista)/2)] #do começo até metade da lista
# %%

minha_lista[:2] # se ocultar o valor antes dos :, começa do início

minha_lista[3:] # se ocultar o valor depois dos :, vai até o fim

#---------------

#%%
#Steps:
minha_lista[::2] #de 2 em 2 passos
#start:stop:step | qualquer iterável, vai ter sempre o start (onde começa), onde você quer parar, e a quantidade de passos que vc quer dar
# %%

#Reordenar lista:
minha_lista[::-1]
# %%
