# Developed by Henrique Treza

#Desafio 16


#No gráfico de budget por lucro temos um ponto com muito custo e prejuizo, descubra com é esse filme (budget próximo de 2.5).


imdb_usa.sort_values('lucro').head(1)['movie_title']