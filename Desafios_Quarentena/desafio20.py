# Developed by Henrique Treza

#Desafio 20


#Analise mais detalhadamente o gráfico pairplot, gaste um tempo pensando e tentando enteder os gráficos.


filmes_depois_de_2000 = imdb_usa.query('title_year >= 2000')
filmes_depois_de_2000[["gross", "budget", "lucro", "title_year"]].corr()

