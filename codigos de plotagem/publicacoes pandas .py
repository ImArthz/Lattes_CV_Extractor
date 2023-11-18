import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregando os dados do arquivo CSV
data_publicacoes = pd.read_csv("publicacoes.csv")

# Gráfico 1: Quantidade de Artigos Completos em Periódicos vs Quantidade de Pessoas
plt.figure(figsize=(12, 6))
bar_artigos_completos = sns.barplot(x=['Total Pessoas', 'Total Artigos Completos em Periódicos'],
                                    y=[len(data_publicacoes), data_publicacoes['Artigos Completos em Periódicos'].sum()],
                                    palette=['lightblue', 'lightgreen'], hue=['Total Pessoas', 'Total Artigos Completos em Periódicos'],
                                    legend=False)
plt.title('Total de Pessoas vs. Total de Artigos Completos em Periódicos')
plt.xlabel('Categorias')
plt.ylabel('Quantidade')
plt.savefig('bar_artigos_completos.png')
plt.show()

# Gráfico 2: Ano do Primeiro Artigo vs Quantidade de Pessoas
plt.figure(figsize=(12, 6))
sns.countplot(x='Ano do Primeiro Artigo', data=data_publicacoes, palette='Blues')
plt.title('Quantidade de Pessoas por Ano do Primeiro Artigo')
plt.xlabel('Ano do Primeiro Artigo')
plt.ylabel('Quantidade de Pessoas')
plt.xticks(rotation=45, ha='right')
plt.savefig('bar_anos_primeiro_artigo.png')
plt.show()

# Gráfico 3: Ano do Último Artigo vs Quantidade de Pessoas
plt.figure(figsize=(12, 6))
sns.countplot(x='Ano do Último Artigo', data=data_publicacoes, palette='Blues')
plt.title('Quantidade de Pessoas por Ano do Último Artigo')
plt.xlabel('Ano do Último Artigo')
plt.ylabel('Quantidade de Pessoas')
plt.xticks(rotation=45, ha='right')
plt.savefig('bar_anos_ultimo_artigo.png')
plt.show()

# Gráfico 4: Top 10 Pessoas com Mais Artigos
top10_artigos = data_publicacoes.sort_values(by='Artigos Completos em Periódicos', ascending=False).head(10)
plt.figure(figsize=(15, 6))
bar_top10_artigos = sns.barplot(x=top10_artigos['Nome'], y=top10_artigos['Artigos Completos em Periódicos'], color='lightblue')
plt.title('Top 10 Pessoas com Mais Artigos Completos em Periódicos')
plt.xlabel('Nome')
plt.ylabel('Quantidade de Artigos Completos em Periódicos')
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.tight_layout()
plt.savefig('bar_top10_artigos.png')
plt.show()

# Gráfico 5: Livros Publicados/Organizados vs Quantidade de Pessoas
plt.figure(figsize=(12, 6))
bar_livros = sns.barplot(x=['Total Pessoas', 'Total Livros Publicados/Organizados'],
                        y=[len(data_publicacoes), data_publicacoes['Livros Publicados/Organizados'].sum()],
                        palette=['lightblue', 'lightgreen'], hue=['Total Pessoas', 'Total Livros Publicados/Organizados'],
                        legend=False)
plt.title('Total de Pessoas vs. Total de Livros Publicados/Organizados')
plt.xlabel('Categorias')
plt.ylabel('Quantidade')
plt.savefig('bar_livros.png')
plt.show()

# Gráfico 6: Quantidade de Pessoas com Primeiro Livro nos Ano do Primeiro Livro
plt.figure(figsize=(12, 6))
sns.countplot(x='Ano do Primeiro Livro', data=data_publicacoes, palette='Greens')
plt.title('Quantidade de Pessoas com Primeiro Livro nos Ano do Primeiro Livro')
plt.xlabel('Ano do Primeiro Livro')
plt.ylabel('Quantidade de Pessoas')
plt.xticks(rotation=45, ha='right')
plt.savefig('bar_anos_primeiro_livro.png')
plt.show()

# Gráfico 7: Quantidade de Pessoas com Primeiro Livro nos Ano do Último Livro
plt.figure(figsize=(12, 6))
sns.countplot(x='Ano do Último Livro', data=data_publicacoes, palette='Greens')
plt.title('Quantidade de Pessoas com Primeiro Livro nos Ano do Último Livro')
plt.xlabel('Ano do Último Livro')
plt.ylabel('Quantidade de Pessoas')
plt.xticks(rotation=45, ha='right')
plt.savefig('bar_anos_ultimo_livro.png')
plt.show()

# Gráfico 8: Top 10 Pessoas com Mais Livros Publicados/Organizados
top10_livros = data_publicacoes.sort_values(by='Livros Publicados/Organizados', ascending=False).head(10)
plt.figure(figsize=(15, 6))
bar_top10_livros = sns.barplot(x=top10_livros['Nome'], y=top10_livros['Livros Publicados/Organizados'], color='lightgreen')
plt.title('Top 10 Pessoas com Mais Livros Publicados/Organizados')
plt.xlabel('Nome')
plt.ylabel('Quantidade de Livros Publicados/Organizados')
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.tight_layout()
plt.savefig('bar_top10_livros.png')
plt.show()

# Gráfico 9: Capítulos de Livros Publicados vs Quantidade de Pessoas
plt.figure(figsize=(12, 6))
bar_capitulos = sns.barplot(x=['Total Pessoas', 'Total Capítulos de Livros Publicados'],
                            y=[len(data_publicacoes), data_publicacoes['Capítulos de Livros Publicados'].sum()],
                            palette=['lightblue', 'lightgreen'], hue=['Total Pessoas', 'Total Capítulos de Livros Publicados'],
                            legend=False)
plt.title('Total de Pessoas vs. Total de Capítulos de Livros Publicados')
plt.xlabel('Categorias')
plt.ylabel('Quantidade')
plt.savefig('bar_capitulos.png')
plt.show()

# Gráfico 10: Ano do Primeiro Capítulo e Pessoas com Primeiro Capítulo nesses Anos
plt.figure(figsize=(12, 6))
sns.countplot(x='Ano do Primeiro Capítulo', data=data_publicacoes, palette='Oranges')
plt.title('Quantidade de Pessoas por Ano do Primeiro Capítulo')
plt.xlabel('Ano do Primeiro Capítulo')
plt.ylabel('Quantidade de Pessoas')
plt.xticks(rotation=45, ha='right')
plt.savefig('bar_anos_primeiro_capitulo.png')
plt.show()

# Gráfico 11: Ano do Último Capítulo e Pessoas com Último Capítulo nesses Anos
plt.figure(figsize=(12, 6))
sns.countplot(x='Ano do Último Capítulo', data=data_publicacoes, palette='Oranges')
plt.title('Quantidade de Pessoas por Ano do Último Capítulo')
plt.xlabel('Ano do Último Capítulo')
plt.ylabel('Quantidade de Pessoas')
plt.xticks(rotation=45, ha='right')
plt.savefig('bar_anos_ultimo_capitulo.png')
plt.show()

# Gráfico 12: Top 10 Pessoas com Mais Capítulos de Livros Publicados
top10_capitulos = data_publicacoes.sort_values(by='Capítulos de Livros Publicados', ascending=False).head(10)
plt.figure(figsize=(15, 6))
bar_top10_capitulos = sns.barplot(x=top10_capitulos['Nome'], y=top10_capitulos['Capítulos de Livros Publicados'], color='orange')
plt.title('Top 10 Pessoas com Mais Capítulos de Livros Publicados')
plt.xlabel('Nome')
plt.ylabel('Quantidade de Capítulos de Livros Publicados')
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.tight_layout()
plt.savefig('bar_top10_capitulos.png')
plt.show()


# Gráfico 13: Trabalhos Completos em Anais de Congressos vs Quantidade de Pessoas
plt.figure(figsize=(12, 6))
bar_trabalhos_completos = sns.barplot(x=['Total Pessoas', 'Total Trabalhos Completos em Anais de Congressos'],
                                    y=[len(data_publicacoes), data_publicacoes['Trabalhos Completos em Anais de Congressos'].sum()],
                                    palette=['lightblue', 'lightgreen'], hue=['Total Pessoas', 'Total Trabalhos Completos em Anais de Congressos'],
                                    legend=False)
plt.title('Total de Pessoas vs. Total de Trabalhos Completos em Anais de Congressos')
plt.xlabel('Categorias')
plt.ylabel('Quantidade')
plt.savefig('bar_trabalhos_completos.png')
plt.show()

# Gráfico 14: Ano do Primeiro Trabalho e Pessoas com Primeiro Trabalho nesses Anos
plt.figure(figsize=(12, 6))
sns.countplot(x='Ano do Primeiro Trabalho', data=data_publicacoes, palette='Reds')
plt.title('Quantidade de Pessoas por Ano do Primeiro Trabalho')
plt.xlabel('Ano do Primeiro Trabalho')
plt.ylabel('Quantidade de Pessoas')
plt.xticks(rotation=45, ha='right')
plt.savefig('bar_anos_primeiro_trabalho.png')
plt.show()

# Gráfico 15: Ano do Último Trabalho e Pessoas com Último Trabalho nesses Anos
plt.figure(figsize=(12, 6))
sns.countplot(x='Ano do Último Trabalho', data=data_publicacoes, palette='Reds')
plt.title('Quantidade de Pessoas por Ano do Último Trabalho')
plt.xlabel('Ano do Último Trabalho')
plt.ylabel('Quantidade de Pessoas')
plt.xticks(rotation=45, ha='right')
plt.savefig('bar_anos_ultimo_trabalho.png')
plt.show()

# Gráfico 16: Top 10 Pessoas com Mais Trabalhos Completos em Anais de Congressos
top10_trabalhos_completos = data_publicacoes.sort_values(by='Trabalhos Completos em Anais de Congressos', ascending=False).head(10)
plt.figure(figsize=(15, 6))
bar_top10_trabalhos_completos = sns.barplot(x=top10_trabalhos_completos['Nome'], y=top10_trabalhos_completos['Trabalhos Completos em Anais de Congressos'], color='red')
plt.title('Top 10 Pessoas com Mais Trabalhos Completos em Anais de Congressos')
plt.xlabel('Nome')
plt.ylabel('Quantidade de Trabalhos Completos em Anais de Congressos')
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.tight_layout()
plt.savefig('bar_top10_trabalhos_completos.png')
plt.show()

# Gráfico 17: Resumos Expandidos em Anais de Congressos vs Quantidade de Pessoas
plt.figure(figsize=(12, 6))
bar_resumos_expandidos = sns.barplot(x=['Total Pessoas', 'Total Resumos Expandidos em Anais de Congressos'],
                                    y=[len(data_publicacoes), data_publicacoes['Resumos Expandidos em Anais de Congressos'].sum()],
                                    palette=['lightblue', 'lightgreen'], hue=['Total Pessoas', 'Total Resumos Expandidos em Anais de Congressos'],
                                    legend=False)
plt.title('Total de Pessoas vs. Total de Resumos Expandidos em Anais de Congressos')
plt.xlabel('Categorias')
plt.ylabel('Quantidade')
plt.savefig('bar_resumos_expandidos.png')
plt.show()

# Gráfico 18: Ano do Primeiro Resumo Expandido e Pessoas com Primeiro Resumo Expandido nesses Anos
plt.figure(figsize=(12, 6))
sns.countplot(x='Ano do Primeiro Resumo Expandido', data=data_publicacoes, palette='YlOrBr')
plt.title('Quantidade de Pessoas por Ano do Primeiro Resumo Expandido')
plt.xlabel('Ano do Primeiro Resumo Expandido')
plt.ylabel('Quantidade de Pessoas')
plt.xticks(rotation=45, ha='right')
plt.savefig('bar_anos_primeiro_resumo_expandido.png')
plt.show()

# Gráfico 19: Ano do Último Resumo Expandido e Pessoas com Último Resumo Expandido nesses Anos
plt.figure(figsize=(12, 6))
sns.countplot(x='Ano do Último Resumo Expandido', data=data_publicacoes, palette='YlOrBr')
plt.title('Quantidade de Pessoas por Ano do Último Resumo Expandido')
plt.xlabel('Ano do Último Resumo Expandido')
plt.ylabel('Quantidade de Pessoas')
plt.xticks(rotation=45, ha='right')
plt.savefig('bar_anos_ultimo_resumo_expandido.png')
plt.show()

# Gráfico 20: Top 10 Pessoas com Mais Resumos Expandidos em Anais de Congressos
top10_resumos_expandidos = data_publicacoes.sort_values(by='Resumos Expandidos em Anais de Congressos', ascending=False).head(10)
plt.figure(figsize=(15, 6))
bar_top10_resumos_expandidos = sns.barplot(x=top10_resumos_expandidos['Nome'], y=top10_resumos_expandidos['Resumos Expandidos em Anais de Congressos'], color='yellow')
plt.title('Top 10 Pessoas com Mais Resumos Expandidos em Anais de Congressos')
plt.xlabel('Nome')
plt.ylabel('Quantidade de Resumos Expandidos em Anais de Congressos')
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.tight_layout()
plt.savefig('bar_top10_resumos_expandidos.png')
plt.show()

# Gráfico 21: Resumos em Anais de Congressos vs Quantidade de Pessoas
plt.figure(figsize=(12, 6))
bar_resumos_anais = sns.barplot(x=['Total Pessoas', 'Total Resumos em Anais de Congressos'],
                                y=[len(data_publicacoes), data_publicacoes['Resumos em Anais de Congressos'].sum()],
                                palette=['lightblue', 'lightgreen'], hue=['Total Pessoas', 'Total Resumos em Anais de Congressos'],
                                legend=False)
plt.title('Total de Pessoas vs. Total de Resumos em Anais de Congressos')
plt.xlabel('Categorias')
plt.ylabel('Quantidade')
plt.savefig('bar_resumos_anais.png')
plt.show()

# Gráfico 22: Ano do Primeiro Resumo e Pessoas com Primeiro Resumo nesses Anos
plt.figure(figsize=(12, 6))
sns.countplot(x='Ano do Primeiro Resumo', data=data_publicacoes, palette='Purples')
plt.title('Quantidade de Pessoas por Ano do Primeiro Resumo')
plt.xlabel('Ano do Primeiro Resumo')
plt.ylabel('Quantidade de Pessoas')
plt.xticks(rotation=45, ha='right')
plt.savefig('bar_anos_primeiro_resumo.png')
plt.show()

# Gráfico 23: Ano do Último Resumo e Pessoas com Último Resumo nesses Anos
plt.figure(figsize=(12, 6))
sns.countplot(x='Ano do Último Resumo', data=data_publicacoes, palette='Purples')
plt.title('Quantidade de Pessoas por Ano do Último Resumo')
plt.xlabel('Ano do Último Resumo')
plt.ylabel('Quantidade de Pessoas')
plt.xticks(rotation=45, ha='right')
plt.savefig('bar_anos_ultimo_resumo.png')
plt.show()

# Gráfico 24: Top 10 Pessoas com Mais Resumos em Anais de Congressos
top10_resumos = data_publicacoes.sort_values(by='Resumos em Anais de Congressos', ascending=False).head(10)
plt.figure(figsize=(15, 6))
bar_top10_resumos = sns.barplot(x=top10_resumos['Nome'], y=top10_resumos['Resumos em Anais de Congressos'], color='purple')
plt.title('Top 10 Pessoas com Mais Resumos em Anais de Congressos')
plt.xlabel('Nome')
plt.ylabel('Quantidade de Resumos em Anais de Congressos')
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.tight_layout()
plt.savefig('bar_top10_resumos.png')
plt.show()

# Gráfico 25: Apresentação de Trabalhos vs Quantidade de Pessoas
plt.figure(figsize=(12, 6))
bar_apresentacao_trabalhos = sns.barplot(x=['Total Pessoas', 'Total Apresentação de Trabalhos'],
                                y=[len(data_publicacoes), data_publicacoes['Apresentação de Trabalhos'].sum()],
                                palette=['lightblue', 'lightgreen'], hue=['Total Pessoas', 'Total Apresentação de Trabalhos'],
                                legend=False)
plt.title('Total de Pessoas vs. Total de Apresentação de Trabalhos')
plt.xlabel('Categorias')
plt.ylabel('Quantidade')
plt.savefig('bar_apresentacao_trabalhos.png')
plt.show()

# Gráfico 26: Ano da Primeira Apresentação e Pessoas com Primeira Apresentação nesses Anos
plt.figure(figsize=(12, 6))
sns.countplot(x='Ano da Primeira Apresentação', data=data_publicacoes, palette='Oranges')
plt.title('Quantidade de Pessoas por Ano da Primeira Apresentação')
plt.xlabel('Ano da Primeira Apresentação')
plt.ylabel('Quantidade de Pessoas')
plt.xticks(rotation=45, ha='right')
plt.savefig('bar_anos_primeira_apresentacao.png')
plt.show()

# Gráfico 27: Ano da Última Apresentação e Pessoas com Última Apresentação nesses Anos
plt.figure(figsize=(12, 6))
sns.countplot(x='Ano da Última Apresentação', data=data_publicacoes, palette='Oranges')
plt.title('Quantidade de Pessoas por Ano da Última Apresentação')
plt.xlabel('Ano da Última Apresentação')
plt.ylabel('Quantidade de Pessoas')
plt.xticks(rotation=45, ha='right')
plt.savefig('bar_anos_ultima_apresentacao.png')
plt.show()

# Gráfico 28: Top 10 Pessoas com Mais Apresentações
top10_apresentacoes = data_publicacoes.sort_values(by='Apresentação de Trabalhos', ascending=False).head(10)
plt.figure(figsize=(15, 6))
bar_top10_apresentacoes = sns.barplot(x=top10_apresentacoes['Nome'], y=top10_apresentacoes['Apresentação de Trabalhos'], color='orange')
plt.title('Top 10 Pessoas com Mais Apresentações')
plt.xlabel('Nome')
plt.ylabel('Quantidade de Apresentações')
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.tight_layout()
plt.savefig('bar_top10_apresentacoes.png')
plt.show()
