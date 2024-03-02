#%% 
#Abrindo o arquivo em modo de escrita ('w') e escrevendo o número 1 nele
arquivo = open("arquivo.txt", 'w')
arquivo.write("1")
arquivo.close()

#%% 
#Abrindo o arquivo em modo de leitura ('r') e lendo todas as linhas
arquivo = open("arquivo.txt", "r")
conteudo = arquivo.readlines()  
# Lê todas as linhas do arquivo e as armazena em uma lista
arquivo.close()

print(conteudo)  # Imprime o conteúdo do arquivo (uma lista de linhas)
print(type(conteudo))  # Imprime o tipo de dados da variável conteudo

#%% 
#Usando a sintaxe 'with' para abrir o arquivo em modo de leitura ('r') de forma mais segura
with open("arquivo.txt", "r") as file:
    conteudo = file.read()  # Lê todo o conteúdo do arquivo e o armazena em uma string

print(conteudo)  # Imprime o conteúdo do arquivo
