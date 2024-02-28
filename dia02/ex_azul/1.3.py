# %%

#Receber raio da circunfência em cm
#Retornar a área e o perímetro no seguinte formato: 
#Área:  x.xx
#Perímetro:  y.yy

# Área = π * raio²
# Perímetro = 2 * π * raio

raio = float(input("Digite o raio da circunferência, vou calcular a área e o perímetro"))

area = (raio**2) * 3.14
perimetro = 2 * 3.14 * raio

print("Ok, para a circunferência de raio = ", raio, ", \no perímetro é aproximadamente:", perimetro, "\ne a área é aproximadamente: ", area, ".")
