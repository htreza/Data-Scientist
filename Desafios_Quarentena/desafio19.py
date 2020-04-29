# Developed by Henrique Treza

#Desafio 19


#No gráfico de filmes_irmaos por dindin temos alguns pontos estranhos entre 15 e 20. Confirme a tese genial do Paulo que o cidadão estranho é o Woody Allen. (Se ele tiver errado pode cornete nas redes sociais kkkkk)


gross_director.drop_duplicates('director_name').query('filmes_irmaos == 18')

plt.figure(figsize=(12, 6))
sns.scatterplot(x="filmes_irmaos", y="dindin", data=gross_director)

gross_director[(gross_director['filmes_irmaos'] > 16) & (gross_director['filmes_irmaos'] < 20)]