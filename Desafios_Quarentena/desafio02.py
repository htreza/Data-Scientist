# Developed by Henrique Treza

#Desafio 2


#Mudar o nome da coluna nota do dataframe filmes_com_media para nota_média após o join.


filmes_com_media = filmes_com_media.rename(columns={'nota': 'nota_media'})
filmes_com_media.head()