import random #importando a biblioteca random


def valida_entrada():
    while True:
        try:
            numero = int(input("Entre com um número entre 1 e 15: "))
            if 1 <= numero <= 15:
                return numero
            else:
                print("Entre com um número válido.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")
            continue

numero_sorte = random.randint(1,15) #pro valor ser aleatorio

for i in range(3):
    numero = valida_entrada()
    if numero == numero_sorte:
        print("Você acertou!")
        break
    elif numero > numero_sorte:
        print("Tente um número menor.")
    else:
        print("Tente um número maior.")
