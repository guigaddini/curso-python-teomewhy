def valida_entrada():
    """Essa função é top""" 
# doc string: string de documentação em Python que fornece uma descrição concisa do propósito e uso de uma função, método, classe ou módulo. É colocado logo após a definição do objeto, cercado por aspas triplas ("""), e é acessível através do atributo __doc__ do objeto.

    while True:
        try: # Tenta pegar um número do usuário
            numero = int(input("Entre com um número entre 1 e 15: "))
            
            # Se a entrada estiver dentro do intervalo válido, retorna o número
            if 1 <= numero <= 15:
                return numero
            else:
                print("Entre com um número válido.")
        
        # Entrou com algo que não é um numeral? Vem para cá.
        except ValueError: 
            print("Entrada inválida. Por favor, insira um número inteiro.")
            continue # Volta para o começo do laço, ignorando o restante
        
numero_sorte = 7

for i in range(3):
    numero = valida_entrada()

    if numero == numero_sorte:
        print("Você acertou!")
        break  
    elif numero > numero_sorte:
        print("Tente um número menor.")
    else:
        print("Tente um número maior.")
