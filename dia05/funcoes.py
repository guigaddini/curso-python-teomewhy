# y = f(x) = x + 10

###

# y = f(x) = x * x + 1

#Derinição da Função
def funcao(x): #assinatura da função
    res = x + 10
    return res

# Invocação da Função
y = funcao(100)
print(y)

# Pode ter vários argumentos ou pode nem ter argumento, ela apenas exibe na tela:
def fds():
    print("FDS!")

# Invocação da Função
fds()

# Definição da função soma com um argumento opcional
def soma(a, b=0): #o primeiro valor é obrigatório, os outros são opcionais
    return a + b

# Invocação da função soma com dois argumentos
print(soma(10, 20))

# Invocação da função soma com um argumento usando o valor padrão para b
print(soma(a=10))