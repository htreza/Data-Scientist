# Developed by Henrique Treza

#Desafio 1
# O Paulo fez uma análise rápida e disse que tem 18 filmes sem avaliações, será que ele acertou?
# Determine quantos filmes não tem avaliações e quais são esses filmes.


selecao = filmes_com_media['nota'].isnull()
filmes_com_media[selecao]