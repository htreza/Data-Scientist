# Developed by Henrique Treza

#Desafio 7



#Plotar o gráfico de aparições de cada genero. Pode ser um gráfico de tipo igual a barra.


total_filmes_por_genero.sort_values(ascending=False).plot(kind='bar', figsize=(16, 6))