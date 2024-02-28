#%%

#Receber número em segundos
#Converter para horas, minutos e segundos

segundos_user = int(input("Digite um número de segundos. Vou te falar quanto ele equivale em horas."))

horas = int(segundos_user / 3600)
minutos = int((segundos_user % 3600)/60)
segundos = int(segundos_user % 60)

print("O valor que você digitou equivale a: ", horas, "hora(s), ", minutos, "minuto(s) e ", segundos, "segundos.")