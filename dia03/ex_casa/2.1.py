#%%

nome = input("Oi, qual é seu nome?")
idade = int(input("E sua idade?"))

if 18 <= idade < 65:
    print(nome, ", você pode dirigir!")

elif idade >= 65:
    print(nome, ", beba com muita moderação!")

else:
    print(nome, ", você não pode dirigir nem beber")
# %%