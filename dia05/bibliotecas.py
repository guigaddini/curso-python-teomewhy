#%%

#Para descobrir raiz quadrada, ao invés de fazer:
49 * 0.5


#%%
#Pode-se fazer:

import math

math.sqrt(49) #square root

#%%

#você pode importar apenas partes da biblioteca (o que fica depois do .), pra não ficar tão pesado:
from math import pi, e

print(pi)
print(e)

#%%
#pra importar tudo:

from math import *

#testando:

sqrt(49)

#obviamente, evite isso ao máximo, pq tem bibliotecas que são mto pesadas. não é boas práticas.

###

#%%
import math as mt #alias -> um apelido pra biblioteca
mt.sqrt(64)