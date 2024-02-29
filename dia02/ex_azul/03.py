tipo_sorvete = input("Entre com o tipo do sorvete: [casquinha/cascao/cestinha] ")

massa = input("Entre com o sabor que você quer: [morango/creme/chocolate] ")

cobertura = input("Que cobertura você quer? [Caramelo/Morango/Chocolate] ")

valor = 0

# tipos de sorvete
if tipo_sorvete == 'casquinha':
    valor += 1.00

elif tipo_sorvete == 'cascao':
    valor += 2.5

elif tipo_sorvete == 'cestinha':
    valor += 4.00

else:
    print("Escolha corretamente")

# coberturas
if cobertura == 'caramelo':
    valor += 1.5

elif cobertura == 'morango':
    valor += 1.5

elif cobertura == 'chocolate':
    valor += 1.5

elif cobertura == 'sem' or cobertura == 'sem cobertura' or cobertura == '':
    pass

else:
    print("Entre com uma cobertura válida")

# sabor de massa não precisa de if, porque não impacta no preço
