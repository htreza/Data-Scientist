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

#Olá, seja bem-vinda e bem-vindo ao notebook da aula 03! A partir desta aula iremos analisar e discutir uma base de dados junto com você. Por isso, será importante que as discussões nos vídeos sejam acompanhadas para entender todos os processos das análises.

#Nessa aula utilizaremos uma base totalmente nova, que nós também não conhecíamos até o momento da análise. Você vai acompanhar a exploração e, principalmente, as dificuldades ao analisar uma base de dados desconhecida.

#Vamos começar importando a nossa base de dados! Nessa aula iremos trabalhar com a IMBD 5000, base que contém uma série de informações sobre filmes, sendo uma pequena amostra da famosa base de dados IMBD.

import pandas as pd
imdb = pd.read_csv("https://gist.githubusercontent.com/guilhermesilveira/24e271e68afe8fd257911217b88b2e07/raw/e70287fb1dcaad4215c3f3c9deda644058a616bc/movie_metadata.csv")
imdb.head()


#Como você acompanhou, iniciamos a aula tentando conhecer as diversas colunas de cada filme e uma das que chamou mais a atenção foi a color. Vamos conhecer quais valores temos nesta colunas?!

imdb["color"].unique()

#Verificamos que essa coluna color informa se o filme é colorido ou é preto e branco. Vamos descobrir agora quantos filmes de cada tipo nós temos:

imdb["color"].value_counts()

imdb["color"].value_counts(normalize=True)


#Agora já descobrimos quantos filmes coloridos e preto e branco temos, e também sabemos que há mais de 5000 filmes na base. Fizemos algo novo, que foi chamar o value_counts(), passando o parâmetro normalize como True. Desse modo, já calculamos qual é a participação de cada um dos tipos de filmes (95% são filmes coloridos).

#Excelente! Agora vamos explorar outra coluna a fim de conhecer os diretores que tem mais filmes na nossa base de dados (lembrando que nossa base é uma amostra muito pequena da realidade)

imdb["director_name"].value_counts()


#Steven Spielberg e Woody Allen são os diretores com mais filmes no IMDB 5000.

#Continuando com nossa exploração de algumas informações, vamos olhar para o número de críticas por filmes.


imdb["num_critic_for_reviews"]


imdb["num_critic_for_reviews"].describe()


#Veja que as colunas color e director_name são strings, não fazendo sentido olhar para médias, medianas e afins. Olhar para o número de avaliações já pode ser interessante, por isso usamos o .describe().

#Agora podemos até plotar um histograma para avaliar o número de review.


import seaborn as sns
sns.set_style("whitegrid")
imdb["num_critic_for_reviews"].plot(kind='hist')


#Introdução
#Olá, seja bem-vinda e bem-vindo ao notebook da aula 03! A partir desta aula iremos analisar e discutir uma base de dados junto com você. Por isso, será importante que as discussões nos vídeos sejam acompanhadas para entender todos os processos das análises.

#Nessa aula utilizaremos uma base totalmente nova, que nós também não conhecíamos até o momento da análise. Você vai acompanhar a exploração e, principalmente, as dificuldades ao analisar uma base de dados desconhecida.

#Vamos começar importando a nossa base de dados! Nessa aula iremos trabalhar com a IMBD 5000, base que contém uma série de informações sobre filmes, sendo uma pequena amostra da famosa base de dados IMBD.


import pandas as pd
imdb = pd.read_csv("https://gist.githubusercontent.com/guilhermesilveira/24e271e68afe8fd257911217b88b2e07/raw/e70287fb1dcaad4215c3f3c9deda644058a616bc/movie_metadata.csv")
imdb.head()


#Como você acompanhou, iniciamos a aula tentando conhecer as diversas colunas de cada filme e uma das que chamou mais a atenção foi a color. Vamos conhecer quais valores temos nesta colunas?!

imdb["color"].unique()


#Verificamos que essa coluna color informa se o filme é colorido ou é preto e branco. Vamos descobrir agora quantos filmes de cada tipo nós temos:


imdb["color"].value_counts()


imdb["color"].value_counts(normalize=True)


#Agora já descobrimos quantos filmes coloridos e preto e branco temos, e também sabemos que há mais de 5000 filmes na base. Fizemos algo novo, que foi chamar o value_counts(), passando o parâmetro normalize como True. Desse modo, já calculamos qual é a participação de cada um dos tipos de filmes (95% são filmes coloridos).

#Excelente! Agora vamos explorar outra coluna a fim de conhecer os diretores que tem mais filmes na nossa base de dados (lembrando que nossa base é uma amostra muito pequena da realidade)


imdb["director_name"].value_counts()


#Steven Spielberg e Woody Allen são os diretores com mais filmes no IMDB 5000.

#Continuando com nossa exploração de algumas informações, vamos olhar para o número de críticas por filmes.


imdb["num_critic_for_reviews"]



imdb["num_critic_for_reviews"].describe()


#Veja que as colunas color e director_name são strings, não fazendo sentido olhar para médias, medianas e afins. Olhar para o número de avaliações já pode ser interessante, por isso usamos o .describe().

#Agora podemos até plotar um histograma para avaliar o número de review.


import seaborn as sns
sns.set_style("whitegrid")
imdb["num_critic_for_reviews"].plot(kind='hist')


#Verificamos que poucos filmes tem mais de 500 votos, por isso um paralelo que podemos fazer é que filmes com muitos votos são mais populares e filmes com poucos votos não são tão populares. Logo, pelo histograma fica evidente que poucos filmes fazem muito muito sucesso. Claro que não conseguimos afirmar isso com propriedade, pois, novamente, estamos lidando com um número restrito de dados, mas são pontos interessantes de se pensar.
#Outra informação interessante de se analisar, são os orçamentos e receitas de um filme, ou seja o aspecto financeiro. Vamos começar pelo gross:

imdb["gross"].hist()


#Como você deve ter reparado, essa é a primeira vez que as escalas estão totalmente diferentes, pois no eixo X temos valores tão altos que a escala teve que ser de centena de milhões. Veja como pouquíssimos filmes tem alto faturamento, o que nos acende um primeiro alerta de que tem algo estranho (ou temos filmes que rendem muito dinheiro neste dataset).

#Vamos tentar conhecer quais são esses filmes com faturamento astronômico.


imdb.sort_values("gross", ascending=False).head()


#Nessa lista temos Avatar, Titanic, Jurassic World e The Avengers, o que parece fazer sentido para nós, pois sabemos que esses foram filmes com bilheterias gigantescas. Analisando esses dados conseguimos verificar que os maiores faturamentos fazem sentido, mas encontramos um problema nos dados, dado que encontramos duas linhas diplicadas. Podemos usar o pandas para remover esses dados, mas por enquanto vamos manter todas as informações (Se estiver curioso em saber como se faz, consulte o .drop_duplicates()).

#Maravilha, agora temos o faturamento e parece estar OK. Queremos começar a responder algumas perguntas e uma delas é: será que filmes coloridos tem faturamento maior que filmes preto e branco?

#Para começar a responder essa pergunta precisamos transformar a coluna Color:


color_or_bw = imdb.query("color in ['Color', ' Black and White']")
color_or_bw["color_0_ou_1"] = (color_or_bw["color"]=="Color") * 1
color_or_bw["color_0_ou_1"].value_counts()


color_or_bw.head()


#Veja que agora nós temos uma última coluna em nosso dataframe com valores 0 e 1. Agora podemos construir gráficos com essa informação de filmes coloridos ou não.

#P.S: Em aula tivemos problemas porque Black and White tinha um espaço no início, vou cortar esses detalhes aqui no notebook, mas reforço a importância de acompanhar este processo no vídeo.


sns.scatterplot(data=color_or_bw, x="color_0_ou_1", y="gross")



#Então plotamos nossos dados com um displot! Existem várias formas de visualizar essa informação, mas por ora essa nos ajuda a comparar os resultados. Repare como filmes coloridos tem valores bem maiores (isso já era até esperado), mas também temos pontos bem altos em filmes preto e branco, chamando muito atenção.

#Vamos explorar algumas estatísticas destes filmes:


color_or_bw.groupby("color").mean()["gross"]


color_or_bw.groupby("color").mean()["imdb_score"]


color_or_bw.groupby("color").median()["imdb_score"]


#Das estatísticas temos duas bem interessantes, a média e mediana das notas de filmes preto e branco são maiores. Há várias possíveis explicações sobre o porquê disso, reflita aí sobre algumas delas e compartilhe conosco!

#A partir de agora, vamos fazer uma investigação melhor em relação às finanças dos filmes (faturamento e orçamento). Vamos iniciar plotando e interpretando um gráfico de gross por budget:


budget_gross=  imdb[["budget", "gross"]].dropna().query("budget >0 | gross > 0")

sns.scatterplot(x="budget", y="gross", data = budget_gross)


#Para plotar os dados, primeiro removemos as linhas com informações de faturamento e orçamento vazias e também com valores igual a 0, para então gerar o gráfico.

#Agora vamos analisar esse gráfico juntos, veja que a escala de budget mudou, agora é e10. Repare que apenas poucos filmes tem orçamentos tão grandes assim, e seus faturamentos são muito baixos. Será que temos algum problema nos dados? Vamos investigar melhor!


imdb.sort_values("budget", ascending=False).head()


#Ordenando os dados pelo budget percebemos que as primeiras posições são de filmes asiáticos. O Guilherme trouxe um ponto interessante para a investigação, pois países como a Coreia usam moedas que tem três casas decimais a mais que o dólar. Então provavelmente o que está ocorrendo é que os dados de orçamento tem valores na moeda local, por isso detectamos valores tão discrepantes.

#Como não temos garantia dos números, vamos precisar trabalhar apenas com filmes americanos, assim garantimos que tanto gross e budget estão em dólares. Então vamos iniciar esse processo:


imdb["country"].unique()


#Veja que temos filmes de diversos locais de origem:


imdb = imdb.drop_duplicates()
imdb_usa = imdb.query("country == 'USA'")
imdb_usa.sort_values("budget", ascending=False).head()


#Agora temos os dados para fazer uma análise melhor entre gross e budget. Vamos plotar o gráfico novamente:


budget_gross = imdb_usa[["budget", "gross"]].dropna().query("budget >0 | gross > 0")

sns.scatterplot(x="budget", y="gross", data = budget_gross)


#Veja que interessante, aparentemente temos uma relação entre orçamento e faturamento. Quanto maior o orçamento, maior o faturamento.

#Já que estamos trabalhando com orçamento e faturamento, podemos construir uma nova informação, o lucro, para analisar. De forma bem simplista esse processo de construir novas informações a partir das existentes no dataset é conhecido como feature engineering.


imdb_usa['lucro'] = imdb_usa['gross'] - imdb_usa['budget']

budget_gross = imdb_usa.query("budget >0 | gross > 0")[["budget", "lucro"]].dropna()

sns.scatterplot(x="budget", y="lucro", data = budget_gross)


#MUito bom! Nós construímos nossa coluna lucro na base de dados e plotamos o orçamento contra lucro.

#Repare que temos pontos interessantes nesta visualização, um deles são esses filmes com muito custo e prejuizo. Isso pode ser um prejuizo real, mas também podem ser filmes que ainda não tiveram tempo de recuperar o investimento (lançamentos recentes). Outros pontos interessantes de se anlisar seriam os filmes com baixos orçamentos e muito lucro, será que são estão corretos ou pode ser algum erro da base? Parece que nem sempre gastar uma tonelada de dinheiro vai gerar lucros absurdos, será que é isso é verdade?

#Esse gráfico é muito rico em informações, vale a pena você gastar um tempo criando hipóteses.

#Já que essa nova feature (lucro) parace ser interessante de se analisar, vamos continuar! Mas agora quero ver o lucro em relação ao ano de produção:


budget_gross = imdb_usa.query("budget >0 | gross > 0")[["title_year", "lucro"]].dropna()

sns.scatterplot(x="title_year", y="lucro", data = budget_gross)


#Olha que legal esse gráfico, veja como alguns pontos mais recentes reforça a teoria de que alguns filmes podem ainda não ter recuperado o dinheiro investido (Claro que temos muitas variáveis para se analisar, mas é um indício relevante).

#Outro ponto que chama muito atenção, são os filmes da década de 30 e 40 com lucros tão altos. Quais serão esses filmes? Bom, essa pergunta você vai responder no desafio do Paulo, que está louco para descobrir!

#Falando em Paulo, ele sugeriu uma análise com os nome dos diretores e o orçamento de seus filmes, vamos ver se conseguimos concluir alguma coisa:


filmes_por_diretor = imdb_usa["director_name"].value_counts()
gross_director = imdb_usa[["director_name", "gross"]].set_index("director_name").join(filmes_por_diretor, on="director_name")
gross_director.columns=["dindin", "filmes_irmaos"]
gross_director = gross_director.reset_index()
gross_director.head()

sns.scatterplot(x="filmes_irmaos", y="dindin", data = gross_director)


#Essa imagem aparentemente não é muito conclusiva, então não conseguimos inferir tantas informações.

#Esse processo de gerar dados, visualizações e acabar não sendo conclusivo é muito comum na vida de um cientista de dados, pode ir se acostumando =P.

#Para finalizar, que tal realizar uma análise das correlações dos dados? EXistem várias formas de calcular a correlação, esse é um assunto denso.Você pode ler mais sobre essas métricas neste link.

#Vamos então inciar a análise das correlações plotando o pairplot.


sns.pairplot(data = imdb_usa[["gross", "budget", "lucro", "title_year"]])


#O pairplot mostra muita informação e a melhor forma de você entender é assistindo as conclusões que tiramos sobre esses gráficos na vídeoaula.

#Embora plotamos um monte de informação, não necessariamente reduzimos a correlação em um número para simplificar a análise. Vamos fazer isso com a ajuda do .corr() do pandas.


imdb_usa[["gross", "budget", "lucro", "title_year"]].corr()


#Com o pandas é simples de se calcular a correlação, mas precisamos saber interpretar os resultados. Vamos fazer isso?

#A correlação é uma métrica que vai de 1 a -1. Quando a correlação é 1, dizemos que é totalmente correlacionada (relação linear perfeita e positiva), ou seja se uma variável aumenta em 10 a outra também irá aumentar em 10. Quando o valor da correlação é -1, também temos variáveis totalmente correlacionda, só que de maneira negativa (relação linear perfeita negativa), neste caso, se uma variável aumenta em 10 a outra reduz em 10. Agora quando a correlação é 0 temos a inexistência de correlação, ou seja, uma variável não tem influêcia sobre a outra.

#Agora sim, entendido sobre a correlação vamos analisar as nossas. Veja que lucro e gross tem uma correlação alta, o que indica que quanto maior o orçamento maior o lucro (mas repare que a correlação não é perfeita), já o title_yers e lucro tem correlação negativa, mas muito perto de zero (ou seja quase não tem correlação). Viu como conseguimos analisar muitas coisas com a correlação?! Pense e tente analisar os outros casos também.

#Com isso chegamos ao final de mais uma aula da #quarentenadados. E aí, o que está achando, cada vez mais legal e ao mesmo tempo mais complexo né?

#O que importa é estar iniciando e entendendo o que fazemos para analisar os dados! Continue até o fim, garanto que vai valer a pena. Vamos praticar?

#Crie seu próprio notebook, reproduza nossa aula e resolva os desafios que deixamos para vocês.

#Até a próxima aula!

#P.S: A partir de agora teremos muitos desafios envolvendo mais análises e conclusões, então não haverá um "gabarito". O importante é você compartilhar suas soluções com os colegas e debater os seus resultados e das outras pessoas


####################################################Fim da Aula 03############################################################################################


####################################################Inicio da Aula 04#########################################################################################


#Aqui iremos explorar e conhecer uma pequena amostra da base de dados do ENEM 2018. Esse será o primeiro passo para construir os modelos de machine learning da aula 05. Se você quiser estudar o código utilizado para criar o dataset desta aula, pode acessar este link aqui.

#Vamos iniciar setando a precisão de casas decimais que o pandas irá exibir os dados (pd.options.display.float_format), depois lendo e conhecendo as informações contidas na base de dados.


import pandas as pd

%precision %.2f
pd.options.display.float_format = '{:,.2f}'.format

uri = "https://github.com/guilhermesilveira/enem-2018/blob/master/MICRODADOS_ENEM_2018_SAMPLE_43278.csv?raw=true"
dados = pd.read_csv(uri)
dados.head()


#Conheça todas as colunas do nosso dataframe:

print(dados.columns.values)


#Na videoaula tivemos uma discussão muito bacana sobre uma visão geral dos dados e sua organização, e sobre ética na IA. Se você não assistiu eu recomendo que veja, não cabe aqui no notebook reproduzir a conversa, então vamos seguir com o desenvolvimento.

#Conhecidas as informações, vamos chamar o describe() para analisá-las. Se atente ao detalhe que o describe só gera informação de dados numéricos!

dados.describe()


#A saída do describe traz várias estatísticas, de forma que algumas não fazem sentido ou não nos interessam neste momento. Entretanto, se você analisou as últimas colunas, viu que lá temos alguns dados relevantes: notas das provas e redação.

#Desafio você a entrar nos detalhes das análises de notas e diversos outros campos! Como nosso tempo aqui é restrito, vamos analisar apenas as notas entre si, mas reflita: Será que existe uma correlação entre as notas? Quem tira notas maiores em redação também vai bem em linguagens?

#Vamos analisar!


colunas_de_notas = ['NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT', 'NU_NOTA_REDACAO']
dados_notas = dados[colunas_de_notas].dropna()
dados_notas.columns = ['ciencias_naturais', 'ciencias_humanas', 'linguagem_codigo', 'matematica', 'redacao']
dados_notas.head()

len(dados_notas)


#Como queremos analisar as notas detalhadamente, no código acima separamos apenas os dados de interesse. Também removemos todos os valores vazios com o .dropna() e trocamos os nomes das colunas para ficar mais legível.

#Por fim, agora nosso DF tem 97270 linhas e 5 colunas.

#Agora sim, vamos calcular a correlação usando o .corr():

corr = dados_notas.corr()
corr


#Temos vários resultados interessantes por aqui: o primeiro é uma correlação considerável entre linguagem_codigo e ciencias_humanas, o que parece fazer sentido. Uma correlação que surpreende é entre linguagem_codigo e redacao. Embora haja uma correlação maior em relação às outras matérias e redação, eu esperava um valor ainda maior do que o existente.

#*Mais alguma correlação te chama a atenção? *

#Eu tenho mais uma análise das correlações em geral! Repare que as correlações com linguagem_codigos sempre são as maiores e isso me faz pensar em várias hipóteses!

#Será que se eu estudar mais português vou ter um desempenho melhor nas outras matérias? (lembre-se que o ENEM é uma prova que demanda interpretação de texto, então essa prerrogativa pode fazer sentido). Será que se eu considerar provas de anos anteriores e comparar as correlações com linguagem_códigos elas serão maiores?

#A verdade é que uma simples análise de correlação nos gera diversas hipóteses. Se tiver curiosidade e quiser fazer essas análises fica como um desafio extra!

#Na videoaula você viu que tentamos plotar diversos gráficos para visualizar a correlação de uma melhor forma. Abaixo seguem os códigos usados:


from string import ascii_letters
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Generate a mask for the upper triangle
mask = np.triu(np.ones_like(corr, dtype=np.bool))

# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(11, 9))

# Generate a custom diverging colormap
cmap = sns.diverging_palette(220, 10, as_cmap=True)

# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})


sns.heatmap(corr)



#Depois de apanhar tentando criar boas imagens, resolvemos deixar esse desafio para você kkkkk... Resolva e dê aquela cornetada em nosso time uahuahha...

#Ok, nós analisamos e conhecemos a base de dados, mas no final o que vou querer é construir um modelo de ML para fazer as predições de algumas notas. Para criar esse modelo de machine learning devemos analisar a distribuição dos nossos dados e verificar se existe alguma tendência entre eles, facilitando o processo preditivo.

#Então, vamos ao pairplot:

sns.pairplot(dados_notas)


#Embora existam alguns dados com maior dispersão, outros parecem obedecer uma certa tendência. Dessa forma, desenvolver um modelo de ML com resultados razoáveis será complexo, porém possível (para detalhes das análises, acompanhe a discussão na videoaula).

#Com isso chegamos ao final de mais uma aula da #quarentenadados. E aí, o que está achando?

#Agora iremos entrar em uma área totalmente nova: o desenvolvimento de modelos de machine learning! Espero que você esteja empolgado(a) para conhecer um pouquinho mais sobre esse assunto!

#Crie seu próprio notebook, reproduza nossa aula e resolva os desafios que deixamos para você.

#Até a próxima aula!

#P.S: A partir de agora você irá colocar a mão na massa, nossos desafios serão mais analítcos. Queremos que você vivencie o dia-a-dia de um ciêntista de dados, discutindo suas conclusões no Slack e estudando as análises de outros colegas, por isso não haverá gabarito.


####################################################Fim da Aula 04############################################################################################


####################################################Inicio da Aula 05#########################################################################################


#Nessa aula discutiremos o que é o processo de classificação e como as máquinas podem aprender esse processo. Após essa discussão iniciaremos o tratamento dos dados para criar nosso primeiro modelo de ML.

#A primeira coisa que devemos fazer é separar os dados que vamos usar como entrada do nosso modelo, dos que precisamos prever:


x_4_notas = dados_notas[['ciencias_naturais', 'ciencias_humanas', 'matematica', 'redacao']]
x_4_notas.head()


#Vamos usar as notas das provas de ciências naturais, ciências humanas, matemática e redação para prever as notas da prova de linguagem e códigos.

#Como separamos os dados de entrada, também devemos fazer o mesmo com aqueles que precisamos adivinhar.


y_adivinhar = dados_notas['linguagem_codigo']
y_adivinhar


#Agora temos os dados que precisamos classificar, mas repare que essa é toda nossa informação! Se eu treinar um modelo com todos esses dados, como eu vou conseguir medir a qualidade do modelo?

#Por isso precisamos dividir nossos dados em dois grupos, um para treino e outro para teste.

#Para fazer isso vamos usar métodos da biblioteca Scikit-learn, ela é uma das principais ferramentas no mundo do Machine Learning! Vale conferir e estudar um pouco mais sobre ela, aqui está o link para a documentação.

#Além do Sklearn, iremos utilizar o numpy para setar o seed dos números pseudo-aleatórios.


from sklearn.model_selection import train_test_split
import numpy as np

np.random.seed(43267)

# f(x) = y
x_treino, x_teste, y_treino, y_teste = train_test_split(x_4_notas, y_adivinhar)

print(x_treino.shape)
print(x_teste.shape)
print(y_treino.shape)
print(y_teste.shape)


x_treino.head()



#Feita a divisão dos nossos dados, chegou a hora de criar seu primeiro modelo de Regressão(Em aula discutimos a diferença entre regressão e classificação).

#Vamos utilizar o LinearSVR do scikit-learn:


from sklearn.svm import LinearSVR

modelo = LinearSVR()
modelo.fit(x_treino, y_treino)


#Até o momento nós treinamos o modelo apenas com o .fit(), mas falta fazer a predição dos resultados. Para realizar a predição chamamos o método .predict() do modelo.


predicoes_notas_linguagem = modelo.predict(x_teste)
predicoes_notas_linguagem[:5]


#Compare a saída da predição com os valores reais logo abaixo, parece que está fazendo sentido, certo?!

y_teste[:5]


#Nos próximos trechos de códigos vamos plotar alguns gráficos! As discussões e todas as análises sobre estas visualizações foram feitas de forma muito rica na videoaula, portanto recomendo fortemente acompanhá-las.


import matplotlib.pyplot as plt

plt.figure(figsize=(9,9))
sns.scatterplot(x=y_teste.values, y=predicoes_notas_linguagem)


import matplotlib.pyplot as plt

plt.figure(figsize=(9,9))
sns.scatterplot(x=y_teste.values, y=y_teste.values - predicoes_notas_linguagem)


import matplotlib.pyplot as plt

# minha predição TOSCA. Dummy!
plt.figure(figsize=(9,9))
sns.scatterplot(x=y_teste.values, y=y_teste - x_teste.mean(axis=1))

import matplotlib.pyplot as plt

# predição do paulo TOSCA. Dummy!
plt.figure(figsize=(9,9))
sns.scatterplot(x=y_teste.values, y=y_teste - y_treino.mean())


#Após discutir esses gráficos, vamos criar mais um modelo de machine learning basededo em "árvores":

from sklearn.tree import DecisionTreeRegressor

modelo = DecisionTreeRegressor()
modelo.fit(x_treino, y_treino)
predicoes_notas_linguagem = modelo.predict(x_teste)
plt.figure(figsize=(9,9))
sns.scatterplot(x=y_teste.values, y=predicoes_notas_linguagem)


plt.figure(figsize=(9,9))
sns.scatterplot(x=x_teste['matematica'].values, y=predicoes_notas_linguagem)
sns.scatterplot(x=x_teste['matematica'].values, y=y_teste.values)


#Após treinar o modelo e fazer as predições, plotamos duas imagens. A primeira é muito parecida com as os gráficos do primeiro classificador, mas a segunda mostra os valores reais e valores previstos!

#Essa figura é muito interessante e mostra uma sobreposição muito boa entre elas, indicando que nossos resultados fazem sentido.

#Avaliar os modelos por imagens é uma forma relevante, mas não resume a informação muito bem, por isso ficaria complexo avaliar dois ou três modelos apenas com gráficos.

#O que precisamos agora é de uma métrica capaz de nos dizer como nosso modelo está indo, aqui vamos usar o erro quadrático médio. Existem centenas de métricas de avaliação, tudo vai depender do que você precisa e o que você está prevendo.


from sklearn.metrics import mean_squared_error

mean_squared_error(y_teste, predicoes_notas_linguagem)


#Veja que nosso erro quadrático médio deu em torno dos 4186.22. Embora pelo gráfico nosso modelo pareça muito bom, pela métrica parece ser um pouco alto.

#O MSE, sigla em inglês para essá métrica, é uma medida que quanto mais perto de zero melhor. Veja o resultado quando calculamos o MSE de dois vetores iguais:

mean_squared_error(y_teste, y_teste)


#Nosso resultado é zero! Você deve estar se perguntando: meu modelo não está nem perto de zero, será que ele é tão ruim assim?

#Nós ainda não temos como te dar essa resposta, precisamos de um critério comparativo, pois assim conseguimos dizer como nosso modelo está indo. Por exemplo, que tal classificar os nossos dados de uma maneira "bobinha"? Para isso temos os chamados métodos Dummy.


from sklearn.dummy import DummyRegressor

modelo_dummy = DummyRegressor()
modelo_dummy.fit(x_treino, y_treino)
dummy_predicoes = modelo_dummy.predict(x_teste)

mean_squared_error(y_teste, dummy_predicoes)


#Finalmente conseguimos responder se nosso modelo é tão ruim assim! Na realidade nosso modelo não é um dos melhores, temos muito o que melhorar, mas já somos melhores que uma classificação ingênua.

#Com isso, encerramos nossa última aula. Espero que vocês tenham gostado!

#Participem também do nosso desafio final, valendo um Nintendo Switch.

#Bons estudos e boa sorte!

#Forte abraço!