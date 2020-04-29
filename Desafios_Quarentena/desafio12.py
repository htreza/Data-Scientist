# Developed by Henrique Treza

#Desafio 12


#Calcular moda, média e mediana dos filmes. Explore filmes com notas mais próximas de 0.5, 3 e 5.


def explora_filme(filme_id):
    filme = filmes.query(f'filmeId == {filme_id}')
    notas = avaliacoes.query(f'filmeId == {filme_id}')['nota']

    print(f'Filme: {filme.iloc[0, 1]}')
    print()

    print(f'Moda: {notas.mode().values}')
    print(f'Média: {notas.mean()}')
    print(f'Mediana: {notas.median()}')
    print('------------')

    explora_filme(8387)
    explora_filme(89386)
    explora_filme(3774)

    explora_filme(2041)
    explora_filme(7541)
    explora_filme(160080)

    explora_filme(177593)
    explora_filme(1178)
    explora_filme(4334)