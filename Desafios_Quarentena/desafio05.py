# Developed by Henrique Treza

#Desafio 5



#Descobrir os generos dos filmes (quais são eles, únicos). (esse aqui o bicho pega)


generos_df = filmes_com_media_e_votos.generos.str.get_dummies('|')
generos = generos_df.columns.to_list()
generos