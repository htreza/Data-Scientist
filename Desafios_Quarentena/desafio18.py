# Developed by Henrique Treza

#Desafio 18


#Quais foram os filmes da decada pré 2° guerra que tiveram muito lucro.


pre_war = imdb_usa.query('title_year < 1940').sort_values('lucro', ascending=False).dropna()
pre_war[['movie_title', 'lucro']].head(2)