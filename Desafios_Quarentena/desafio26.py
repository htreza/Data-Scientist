# Developed by Henrique Treza

#Desafio 26


#Remover todos os zeros. Tomar o cuidado que no desafio 1 já tomamos decisões ligadas a limpeza dos dados também. Você também pode exportar para outro CSV se quiser.


# Seguindo a dica da Thais
import numpy as np

dados_nota_sem_0 = dados_nota_2.copy()

# dados_nota_sem_0['NU_RESPOSTAS_CORRETAS_CN'] = dados_nota_2['NU_RESPOSTAS_CORRETAS_CN'].replace(0, None)
# dados_nota_sem_0['NU_RESPOSTAS_CORRETAS_CH'] = dados_nota_2['NU_RESPOSTAS_CORRETAS_CH'].replace(0, None)
# dados_nota_sem_0['NU_RESPOSTAS_CORRETAS_LC'] = dados_nota_2['NU_RESPOSTAS_CORRETAS_LC'].replace(0, None)
# dados_nota_sem_0['NU_RESPOSTAS_CORRETAS_MT'] = dados_nota_2['NU_RESPOSTAS_CORRETAS_MT'].replace(0, None)

dados_nota_sem_0['NU_NOTA_CN'] = dados_nota_2['NU_NOTA_CN'].replace(0., np.NAN)
dados_nota_sem_0['NU_NOTA_CH'] = dados_nota_2['NU_NOTA_CH'].replace(0., np.NAN)
dados_nota_sem_0['NU_NOTA_LC'] = dados_nota_2['NU_NOTA_LC'].replace(0., np.NAN)
dados_nota_sem_0['NU_NOTA_MT'] = dados_nota_2['NU_NOTA_MT'].replace(0., np.NAN)

dados_nota_sem_0.dropna(subset=['NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT'], inplace=True)

dados_nota_sem_0[['NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT']].head()