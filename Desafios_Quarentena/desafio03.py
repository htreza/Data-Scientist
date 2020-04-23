# Developed by Henrique Treza

#Desafio 3


#Colocar o número de avaliações por filme, isto é, não só a média mas o TOTAL de votos por filme.


total_votos_por_filme = avaliacoes.groupby('filmeId')['nota'].count()
total_votos_por_filme.head()

filmes_com_media_e_votos = filmes_com_media.join(total_votos_por_filme, on='filmeId')
filmes_com_media_e_votos = filmes_com_media_e_votos.rename(columns={'nota': 'total_votos'})
filmes_com_media_e_votos.head()