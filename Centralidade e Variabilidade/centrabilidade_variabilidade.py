"""
@author: Henrique Treza
"""

import numpy as np
from scipy import stats

# Lista com salarios de jogadores
jogadores = [40000, 18000, 12000, 250000, 30000, 140000, 300000, 40000, 800000]

#Media dos salarios dos jogadores
np.mean(jogadores)

#Mediana dos salarios dos jogadores(Valor central)
np.median(jogadores)

#Seleciona a variavel na qual eu quero o calculo, seleciono a % dos dados que quero que seja calculado
quartis = np.quantile(jogadores, [0, 0.25, 0.50, 0.75, 1])

#Como calcular o Desvio Padrao, precisa passar um parametro adicional(ddof = 1) denonimador igual a n, no R é n-1
np.std(jogadores)
np.std(jogadores, ddof = 1)

#Visualizar alguns dados detalhados
stats.describe(jogadores)