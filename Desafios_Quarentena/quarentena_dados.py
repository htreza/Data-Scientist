import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

##Aula 01

filmes = pd.read_csv("https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula0/ml-latest-small/movies.csv")
# filmes é um DataFrame
filmes.columns = ["filmeId", "titulo", "generos"]
filmes.head()

#Agora vamos analisar um pouco melhor o dataset de avaliações.
avaliacoes = pd.read_csv("https://github.com/alura-cursos/introducao-a-data-science/blob/master/aula0/ml-latest-small/ratings.csv?raw=true")
avaliacoes.head()


#Para visualizar algumas linhas estamos usando o .head(), como ela mostra apenas as 5 primeiras linhas não sabemos qual é a quantidade de
# linhas que temos. Para descobrir a "forma" dos nossos dados podemos utilizar o avaliacoes.shape, retornando uma tupla, onde o primeiro
# termo indica o número de linhas e o segundo o número de colunas.

avaliacoes.shape


len(avaliacoes)

#Vamos substituir os nomes das colunas de inglês para português e entender o que são essas colunas.

#usarioId => ID para para usuário que votou em determinado filme.

#filmeId => ID para identificar um filme votado.

#nota => A nota dada para pelo usuário para o respectivo filme.

#momento => A data da votação que não está formatada como data

#Como cada linha contém um voto para o respectivo filme é de se esperar que um filme tenha diversos votos, mas repare que nas 5 primeiras linhas temos o filme 1, 3, 6, 47, 50. Mas e se eu quiser analisar apenas as notas do filme 1, como posso separar essa informação?

avaliacoes.columns = ["usuarioId", "filmeId", "nota", "momento"]
avaliacoes.head()


#Uma forma para "separar" as informações apenas do filmeId 1 é chamando o método avaliacaoes.query("filmeId==1"), esse método retornará apenas as linhas para quais a expressão booleana, "filmeId==1", for verdadeira.

#Tendo as informações do filmeId 1 podemos chamar o avaliacoes_do_filme_1.describe(), para analisar as estatítiscas gerais dos dados.

avaliacoes_do_filme_1 = avaliacoes.query("filmeId==1")
avaliacoes_do_filme_1.head()


avaliacoes_do_filme_1.describe()

#Caso queira uma estatística particular, podemos apenas chamar o método desajado, repare abaixo como calculamos apenas a média das avaliações do filmeId 1.

avaliacoes_do_filme_1.mean()


#Calculamos as estatísicas apenas para o filmeId 1, mas também podemos chamar o método .describe() para a base completa (avaliacões).

avaliacoes.describe()


#Ok, nós calculamos um tanto de coisa usando .describe() e .mean(), mas a informação que realmente queremos é a média da nota. Então o ponto é, como calcular a média apenas das notas?

#A primeira coisa que precisamos fazer é selecionar apenas as informações de notas. Usando uma estrutura muito parecida com a de chave-valor dos dicionários python.

#Com o comando avaliacoes["nota"], obtemos os valores da coluna nota (repare que o tipo retornado é uma Série pandas, por isso o index de cada nota é mantido). Para calcular a média de todas as notas executamos avaliacoes["notas"].means()

avaliacoes["nota"]


avaliacoes["nota"].mean()


#Podemos calcular também na nota média do filmeId 1, repare que o resultado é um pouco maior que a geral. Apenas com essa análise não da para bater o martelo que o filme 1 é acima da média, mas apenas com essa análise conseguimos formular uma primeira hipótese!

avaliacoes_do_filme_1["nota"].mean()


#Nós calculamos uma média geral, uma média para o filmeId 1. Agora eu quero calcular a média das notas para todos os filmes, podemos fazer isso usando o método .groupby(filmeId), o parâmetro passado é para indicar qual coluna ele deve utilizar para "agrupar" os dados. Depois só calcular a média como fizemos anteriormente.

notas_medias_por_filme = avaliacoes.groupby("filmeId")["nota"].mean()
notas_medias_por_filme.head()


#Temos as notas médias calculadas, mas agora precisamos juntar as informações de notas médias com a base de dados filmes.

#Poderíamos criar uma nova coluna e atribuir a váriável notas_medias_por_filme, de forma direta:

#filmes["nota_media"] = notas_medias_por_filme

#Como discutimos em aula, essa não é uma boa prática pois precisamos garantir que a nota média seja do respectivo filme.

#Para garantir essa condição vamos utilizar o .join(), criando um novo dataframe (filmes_com_media = filmes.join(notas_medias_por_filme, on="filmeId")).

#Veja como fazer, nas células a seguir.

filmes


notas_medias_por_filme


filmes_com_media = filmes.join(notas_medias_por_filme, on="filmeId")
filmes_com_media.head()


#Agora que temos as médias, que tal visualizar o nosso dataframe ordenado pela nota de forma decrescente?
filmes_com_media.sort_values("nota", ascending=False).head(15)


#Fizemos um tanto de análise e manipulação de dados interessante, não é?

#Mas diz a verdade, você está sentindo falta daquele gráfico que todo cientista de dados adora  então bora plotar nosso primeiro gráfico

#O pandas facilita muito o plot de alguns gráficos simples, apenas selecionamos a informação que gostaríamos de visualizar e chamamos o método .plot()

avaliacoes.query("filmeId == 1")["nota"].plot()


#Por padrão o método plotou um gráfico de linhas, o que não é adequado para os dados que estamos analisando.

#Precisamos mudar o tipo de gráfico para realizar uma análise mais adequada, para fazer isso apenas alteramos o parâmetro kind do método .plot. Vamos plotar um histograma rodando a célula a seguir.

avaliacoes.query("filmeId == 1")["nota"].plot(kind='hist')


#Legal, agora temos uma visualização muito mais agradavel de analisar. Compare com o gráfico de linhas, qual você acha melhor para análise?

#P.S: Deixar de usar o gráfico de linhas, não significa que sejá uma visualização ruim. Apenas quer dizer que nossos dados não tem características ideias para serem visualizados como um line plot, agora pense em uma série temporal. Você acha que o gráfico de linhas ainda seria uma má ideia?

#Antes de analisar o histograms de outros filmes, quero colocar um título na imagem. Vamos ver como podemos fazer isso!

avaliacoes.query("filmeId == 1")["nota"].plot(kind='hist',
                                              title="Avaliações do filme Toy Story")


#Claro que python tem outras ferramentas muito poderosas para manipular gráficos, uma delas é o matplotlib.

#Que tal experimentar um pouquinho esta poderosa ferramenta?

#Vamos importar a lib e adicionar título no gráfico usando o matplotlib, veja como fica na célula a seguir.

avaliacoes.query("filmeId == 1")["nota"].plot(kind='hist')
plt.title("Avaliações do filme Toy Story")
plt.show()


#Agora que aprendemos a criar um histograma e manipular os gráficos, vamos plotar informações de outros filmes e realizar uma análise desses gráficos?

#Vamos plotar o histograma do filme Jumanji e da animação Liga da justiça: Doom.

avaliacoes.query("filmeId == 2")["nota"].plot(kind='hist',
                                              title="Avaliações do filme Toy Jumanji")


avaliacoes.query("filmeId == 102084")["nota"].plot(kind='hist',
                                                   title="Avaliações do filme Justice League: Doom")


####################################################Fim da Aula 01############################################################################################


####################################################Inicio da Aula 02#########################################################################################


#Nesta aula vamos estudar com mais profundidade as técnicas de centralidade, conhecer algumas boas práticas de visualização de dados e o famoso Boxplot.

#Para inciar vamos precisar resolver alguns dos desafios deixados na aula 01 (Caso não tenha tentado resolver os desafios, recomendo tentar algumas vezes antes de olhar as repostas). Começando pelo exercício 05, onde precisamos segregar os gêneros de cada um dos filmes contidos na base de dados do Movie Lens.

#Vamos relembrar como os dados estavam configurados.

filmes.head()


#Temos os títulos e uma coluna com os respectivos gêneros, todos em uma única coluna, cada label é separada com um | (Adventure|Children|Fantasy) sendo do tipo string.

#Para solucionar nosso problema precisamos separar cada um dos gêneros para então realizar a contagem. Existe várias formas de resolver este problema, por exemplo, desde métodos inputos das strings até as regex, mas como estamos usando o pandas já temos algo para facilitar nosso processamento dos dados.

#Vamos aplicar o método e logo em seguida explicar a saída geranda.

filmes["generos"].str.get_dummies('|')


#Nossa, uma linha de código gerou essa tabelona cheia de linhas, colunas e números.

#Como você percebeu a saída é um DataFrame, cada linha corresponde a respectiva linha da coluna gênero, cada coluna corresponde a um gênero (repare que cada gênero único virou uma coluna no DF). O que você deve estar se perguntando é como os valores 0/1 são preenchidos?.

#Para explicar, vamos pegar os gêneros do filme Jumanji, Adventure|Children|Fantasy, na coluna dos repectivos gêneros (dataframe gerado por filmes["generos"].str.get_dummies('|')) o valor será 1, para todos os outros gêneros, que não são gêneros do filme Jumanji, vale 0. Em suma, se o nome da coluna pertence a algum gêreno do respectivo filme, o valor será 1 caso contrário 0 (Se ainda não ficou claro, pegue alguns filmes e confira os resultas na tabela anterior).

#Até aqui resolvemos uma parte do problema, agora precisamo somar quantos 1 cada coluna tem.

filmes["generos"].str.get_dummies('|').sum()


#Ótimo, resolvemos o desafio e agora temos quantas vezes cada gênero aparece. Assim, fica fácil de reponder perguntar como, qual o gênero com mais filmes produzidos? Qual o menos? Qual o segundo? (Lembrando que o dado está restrito as informações do movie lens)

#Se você tentou reponder, deve ter notado que não foi tão fácil assim, as informações não estão ordenadas e toda hora você precisa percorrer a tabela para fazer comparações. Nós podemos melhor isso ordenando as informações.

filmes["generos"].str.get_dummies('|').sum().sort_values(ascending=False)



#Maravilha, agora tudo ficou mais fácil!

#Conseguimos responder as perguntas anterior sem grandes dificuldades. Mas ainda podemos melhor mais a forma de expor nossa informação, não acha?

#Que tal uma imagem para visualizar? (Desafio 07 da aula 01)

filmes["generos"].str.get_dummies('|').sum().sort_values(ascending=False).plot()


#Iniciamos com o plot padrão do pandas, e como percebemos não adianta só plotar uma imagem, é preciso que faça sentido para a informação que queremos analisar, um gráfico de linhas não está fazendo muito sentido!

#Temos um gráfico muito conhecido que sempre encontramos por aí, o famoso gráfico de pizza ou torta.

#Já que ele é tão famoso talvez seja uma boa ideia tentar!


filmes["generos"].str.get_dummies('|').sum().sort_values(ascending=False).plot(
    kind='pie',
    title='Categorias de filmes e suas presenças relativas',
    figsize=(8,8))
plt.show()


#E aí o que você achou?

#Algo que fica evidente neste gráfico é que Drama, Comedy, Thriller, e Action tem proporções "grandes", mas qualquer outra análise fica complicada.

#Primeiro, as cores começa a se repetir e isso não é o ideial.

#Segundo, repare nos gêneros com menos filmes,consegue tirar alguma informação de lá? é muito difícil de analisar.

#Quarto, vamos tentar comparar thriller e Action, qual está presente em mais filmes? Difícil responder, quando estamos trabalhando com gráficos tipo esse fazemos comparações entre área, não somos bons nisso.

#Por fim, o importante de uma visualização é que ela seja "transparente" ao intuíto de nossa análise. Ou seja, estamos querendo analisar as informações de quantidade, comparando as labels de forma geral e evidênciando de maneira clara as diferenças entre elas (proporções).

#Portanto, o gráfico de pizza não torna as comparações claras, sendo assim uma má ideia.

#Vamos construir juntos uma solução mais adequada!


filmes["generos"].str.get_dummies('|').sum().sort_values(ascending=False).plot(
    kind='bar',
    title='Filmes por categoria',
    figsize=(8,8))
plt.show()



#Mudamos da pizza para a barra, alterando apenas o parâmetro kind do método.

#Veja como o gráfico de barra torna a análise mais simples, logo de cara a diferença entre Drama e Comedy, comparado aos demais gêneros fica evidênte. No gráfico de pizza era super difícil comparar Thriller e Action, agora a comparação ficou fácil e conseguimos perceber o quão perto estão uma da outra.

#A interpretação dos dados melhorou muito com essa visualização, mas podemos melhorar ainda mais. O que queremos é tornar evidênte os gêneros que tem a maior participação nos filmes em geral, ou seja transparecer através da imagem uma visão geral de proporcionalidade. Para tprnar evidênte essa informação vamos utilizar algo "semelhante" a um mapa de calor.


sns.set_style("whitegrid")

filmes_por_genero = filmes["generos"].str.get_dummies('|').sum().sort_values(ascending=False)
plt.figure(figsize=(16,8))
sns.barplot(x=filmes_por_genero.index,
            y=filmes_por_genero.values,
            palette=sns.color_palette("BuGn_r", n_colors=len(filmes_por_genero) + 4))
plt.show()


#Já, já explicamos o que foi feito em toda imagem, por agora repare como a imagem passa muito mais informação. Conseguimos comparar de forma fácil entre os gêneros e através do mapa de calor (gêneros com maior número tem um verde muito mais forte, gêneros com menor número é praticamente transparente) evidênciamos quais são as labels com maior participação, médias e insignificantes. Toda essa informação em uma única imagem!

#Bom, agora vamos entender como foi o código.

#Primeiro, não plotamos mais a imagem com o .plot() do pandas, vamos precisar de uma biblioteca de visualização mais poderosa para configurar nossa imagem, utilizamos o seaborn.

#Segundo, chamamos o barplot do seaborn, adicionando uma paleta de cores com efeito de mapa de calor (parâmetro pallette), no parâmetro n_color de sns.color_palette() adicionamos +4 para que a última barra não seja totalmente transparente.

#Terceiro, também adicionamos o sns.set_style("whitegrid") para que todos os gráficos tenham a linha de grade do eixo X evidênte, facilitando a comparação entre as barras.


filmes_por_genero = filmes["generos"].str.get_dummies('|').sum().sort_values(ascending=False)
plt.figure(figsize=(8,8))
sns.barplot(x=filmes_por_genero.index,
            y=filmes_por_genero.values,
            palette=sns.color_palette("BuGn_r", n_colors=len(filmes_por_genero) + 4))
plt.show()



#Por fim, mudamos o tamanho da imagem com o figsize do métodoplt.figure(). Assim, temos um gráfico com muitas informações e agradável de analisar.

sns.set_style("whitegrid")

filmes_por_genero = filmes["generos"].str.get_dummies('|').sum().sort_values(ascending=False)
plt.figure(figsize=(16,8))
sns.barplot(x=filmes_por_genero.index,
            y=filmes_por_genero.values,
            palette=sns.color_palette("BuGn_r", n_colors=len(filmes_por_genero) + 4))
plt.show()


#Conseguimos analisar e tirar diversas conclusões trabalhando com a visualização dos gêneros. Será que conseguimos utilizar visualizações para entender melhor as notas de um filme?

#Vamos relembrar alguns pontos que já discutimos e nos aprofundar nas análises de notas para tirar conclusões mais sofisticadas.

#Na aula 01 calculamos as notas médias por filmes, vamos dar uma olhada no resultado.

filmes_com_media.head()


#Como vimos, olhar apenas as médias pode ser um problema e para interpretar um pouco melhor os dados usamos o histograma das ntoas para comparar alguns filmes. Por exemplo, Toy Story e Jumanji

notas_do_filme_1 = avaliacoes.query("filmeId==1")["nota"]
print(notas_do_filme_1.mean())
notas_do_filme_1.plot(kind='hist')


notas_do_filme_1 = avaliacoes.query("filmeId==2")["nota"]
print(notas_do_filme_1.mean())
notas_do_filme_1.plot(kind='hist')



#P.S: Se tiver dúvidas reveja essa parte da aula e tente enteder o problema da média.

#Outras métrica que pode nos ajudar a interpretar melhor os dados são os quatis, principalmente a mediana

#Vamos buscar dois filmes com médias muito mais próximas que Toy Story e Jumanji, para analisar outras métricas além das médias.


filmes_com_media.sort_values("nota", ascending=False)[2450:2500]


#Bom, ordenando os filmes pela nota médias e fatiando os dados entre 2450 e 2500, temos uma região onde as médias são semelhates e provavelmente não tem apenas um único voto. Vamos comparar o fime Wizard of Oz, filmeId=919 e *Little Miss Sunshine filmeId=46578.

#Para não precisar copiar e colar toda hora o plot dos gráficos vamos criar nossa primeira função, assim passamos apenas o FilmeId e temos as informações desejadas.


def plot_filme(n):
  notas_do_filme = avaliacoes.query(f"filmeId=={n}")["nota"]
  notas_do_filme.plot(kind='hist')
  return notas_do_filme.describe()



#Definimos nossa função plot em python e repare que estamos usando F-string para fazer a interpolação dos dados, se tiver tiver dúvida veja essa explicação no fórum da alura.

#Agora precisamos chamar a função!


#Mágico de Oz
plot_filme(919)



#A função plot, além de gerar o histograma também retorna algumas estatísticas. Vamos chamar a função agora para o filme Little Miss Sunshine.

plot_filme(46578)



#Ótimo, agora com essas informações conseguimos comparar melhor ambos os filmes. Analisando os histogramas vemos que muitas pessoas realmente amam Wizard of Oz (notas 5), mas também temos pessoas que não gostam de formal alguma (notas 1). Quando comparamos com a histograma temos um do Little mis sunshine, percebemos que os resultados se concentra entre valores medianos(notas 2.5-4).

#O que confirma nossa análise aqui é comparar os 25% 50% e 75%. 50% é o valor da mediana, e ambos filmes tem mesma mediana, mas 25% e 75% são diferentes. Se você lembra lá da estatísitca esses são os 1° 2° e 3° quartis.

#Olha, mesclar os gráficos com as estatísticas ajuda a interpretar melhor os dados. Mas o que precisamos é uma imagem que nos ajude a interpretar os dados ainda melhor, o gráfico que nos ajuda neste caso é o Boxplot. Vamos adaptar nossa função para conseguir plotar o boxplot e interpretá-lo.


def plot_filme(n):
  notas_do_filme = avaliacoes.query(f"filmeId=={n}")["nota"]
  notas_do_filme.plot(kind='hist')
  plt.show()
  print('\n')
  notas_do_filme.plot.box()
  plt.show()
  return notas_do_filme.describe()

plot_filme(919)


#E aí, viu como é simples criar criar um boxplot com o pandas?

#Apenas chamamos o método .plot.box(), agora o que precisamos fazer é interpretar este gráfico.

#Vamos focar primeiro na "caixa" a linha verde que divide a caixa em dois é a mediana (compare com as estatísticas geradas pelo discribe()), a parte superior da caixa é o 3° Quartil (75%) e a parte inferior é o 1° Quartil (25%).

#Agora repare nos limites inferior e superior, represetados pelas extremidades em preto. Por coincidência, nesta imagem os limites inferior e superior são equivalentes ao ponto de máximo e mínimo, mas nem sempre será assim, pois esse limite superir e inferior são calculados e dependem de Q1 e Q3. Algumas vezes os limites podem sobrepor os extremos das "caixas" e isso geralmente ocorre quando temos uma quantidade pequena de dados.

#Como tivemos sobreposição do limite superior vamos calcular o boxplot de outro filme, para analisar o resultado.

plot_filme(46578)


#Olha que legal, diferente do primeiro boxplot, neste os limites superiores não se sobrepõe e temos uma informação a mais, no caso temos essa bolinha localizada em y=1. A "bolinha" chamamos de valor discrepante, por ir além dos limites inferior e superior (chamamos na aula de outliers, existem várias formas de calcular os outliers, mas no nosso caso esses são os outliers do boxplot).

#Não vamos entrar em todos os detalhes do boxplot mas recomendo a explicação do wikipedia, ela é muito completa, cheias de exemplo e imagens para facilitar o entendimento.

#Agora comparando os boxplot dos dois filmes deixa muito mais evidente as diferenças entre elas, o que ficava complexo olhando só médias e outras informações separadas.

#Embora melhoramos muito nossa qualidade de análise ainda temos mais um ponto. Estamos comparando os boxplot dos filmes, mas eles estão em imagens separadas, vamos juntas vários boxplot em uma imagem só. Veja como podemos fazer isso usando o seaborn, para aprendermos outra forma de plotar boxplot!

sns.boxplot(data = avaliacoes.query("filmeId in [1,2,919,46578]"), x ="filmeId", y="nota")



####################################################Fim da Aula 02############################################################################################


####################################################Inicio da Aula 03#########################################################################################



