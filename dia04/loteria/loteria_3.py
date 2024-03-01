# Define o número sorteado
numero_sorte = 7

# Loop para permitir três tentativas ao usuário
for i in range(3):
    # Loop de 3x para garantir que o usuário forneça uma entrada válida
    while True:
        try:
            numero = int(input("Entre com um número entre 1 e 15: "))
            break  # Se a entrada do usuário for válida, saia do loop while

        except ValueError:
            # Se o usuário inserir algo que não possa ser convertido para um número inteiro, continue solicitando uma entrada válida
            print("Entrada inválida. Por favor, insira um número inteiro.")

    # Verifica se o número inserido é igual ao número sorteado
    if numero == numero_sorte:
        print("Você acertou!")
        break  # Encerra o loop for
    elif numero > numero_sorte:
        # Imprime "Tente um número menor."
        print("Tente um número menor.")
    else:
        print("Tente um número maior.")
