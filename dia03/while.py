
while True: #laço de repetição eterno
    
    senha = input("Entre com a senha: ")

    print("FDS!")
    if senha == "fds":
        break

    else:
        print("quase...")
        continue #sai dessa linha e volta pra linha 5

print("Saí do loop!")

# %%

#todos os numereos pares entre 1 e 15

contador = 1
while contador <= 15:
    if contator % 2 == 0: #se o contador for divisível por 2
        print(contador)

        contador +=1
# %%
