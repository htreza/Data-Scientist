"""
@author: Henrique Treza
"""

import pandas as pd
import numpy as np

base = pd.read_csv('iris.csv')
base

base.shape

#/função do numpy para selecionar números random, passa o parametro [0,1], size = tamanho
# replace = True, para selecionar o mesmo número mais de uma vez, e p = probabilidade [0.5, 0.5] chance de 50% 


np.seed(2345) #Semente geradora aleatoria seed, sempre gera os mesmo dados
amostra = np.random.choice(a = [0, 1], size = 150, replace = True, p = [0.5, 0.5])
len(amostra)
len(amostra[amostra == 1])
len(amostra[amostra == 0])
