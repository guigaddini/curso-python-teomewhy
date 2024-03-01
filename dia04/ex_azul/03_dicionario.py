#%%
tipo_sorvete = input("Entre com o tipo do sorvete: [casquinha/cascão/cestinha] ").lower()

massa = input("Entre com o sabor que você quer: [morango/creme/chocolate] ").lower()

cobertura = input("Que cobertura você quer? [Caramelo/Morango/Chocolate] ").lower()

valor = 0

massas = ["morango", "creme", "chocolate"]

if massa not in massas:
    print("Sabor de massa inválido. Por favor, escolha entre morango, creme ou chocolate.")
    exit()

# tipos de sorvete
sorvetes = {
    "casquinha": 1.00,
    "cascão": 2.50,
    "cestinha": 4.00
}

if tipo_sorvete in sorvetes:
    valor += sorvetes[tipo_sorvete] #O que meu usuário passar (tipo_sorvete), eu busco no preço de sorvete (sorvetes)
    # += -> o valor inicial é zero. Eu pego o valor inicial (0) e somo com o novo (sorvetes)

else:
    print("Seu pedido vai vir zuado. Entre com um valor válido!")
    exit()

# coberturas
coberturas = {
    "caramelo": 1.50, 
    "morango":  1.50, 
    "chocolate":  1.50, 
    "": 0,
    "sem": 0,
    "sem cobertura": 0

}

if cobertura in coberturas:
    valor += coberturas[cobertura]
else:
    print("Seu pedido vai vir zuado. Entre com um valor válido!")
    exit()

print("Seu sorvete", tipo_sorvete, "de", massa, "com cobertura", cobertura, "custará: R$", valor)

# %%
