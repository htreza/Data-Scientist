# Developed by Henrique Treza

#Desafio 6



#Contar o número de aparições de cada genero.


total_filmes_por_genero = filmes_com_media_e_votos.generos.str.get_dummies().sum()
total_filmes_por_genero