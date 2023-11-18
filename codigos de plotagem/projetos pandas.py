import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregando os dados do arquivo CSV
data_projetos = pd.read_csv("projetos.csv")

# Gráfico 1: Total de Pessoas vs. Total de Projetos de Pesquisa
plt.figure(figsize=(12, 6))
bar_total_pesquisa = sns.barplot(x=['Total Pessoas', 'Total Projetos de Pesquisa'],
                                y=[len(data_projetos), data_projetos['Total de Projetos de Pesquisa'].sum()],
                                palette=['lightblue', 'lightgreen'], hue=['Total Pessoas', 'Total Projetos de Pesquisa'],
                                legend=False)
plt.title('Total de Pessoas vs. Total de Projetos de Pesquisa')
plt.xlabel('Categorias')
plt.ylabel('Quantidade')
plt.savefig('bar_total_pesquisa.png')
plt.show()



# Gráfico 2: Ano do Primeiro Projeto de Pesquisa vs. Quantidade de Pessoas
plt.figure(figsize=(12, 6))
my_palette = sns.color_palette("Blues", as_cmap=True)
sns.countplot(x='Ano de Conclusão do Primeiro Projeto de Pesquisa', data=data_projetos, palette=my_palette, hue='Ano de Conclusão do Primeiro Projeto de Pesquisa', legend=False)
plt.title('Quantidade de Pessoas por Ano do Primeiro Projeto de Pesquisa')
plt.xlabel('Ano do Primeiro Projeto de Pesquisa')
plt.ylabel('Quantidade de Pessoas')
plt.xticks(rotation=45, ha='right')
plt.savefig('bar_anos_primeiro_pesquisa.png')
plt.show()

# Gráfico 3: Ano do Último Projeto de Pesquisa vs. Quantidade de Pessoas
plt.figure(figsize=(12, 6))
sns.countplot(x='Ano de Conclusão do Último Projeto de Pesquisa', data=data_projetos, palette='Blues')
plt.title('Quantidade de Pessoas por Ano do Último Projeto de Pesquisa')
plt.xlabel('Ano do Último Projeto de Pesquisa')
plt.ylabel('Quantidade de Pessoas')
plt.xticks(rotation=45, ha='right')
plt.savefig('bar_anos_ultimo_pesquisa.png')
plt.show()

# Gráfico 4: Top 10 Pessoas com Mais Projetos de Pesquisa
top10_pesquisa = data_projetos.sort_values(by='Total de Projetos de Pesquisa', ascending=False).head(10)
plt.figure(figsize=(15, 6))
bar_top10_pesquisa = sns.barplot(x=top10_pesquisa['Nome'], y=top10_pesquisa['Total de Projetos de Pesquisa'], color='lightblue')
plt.title('Top 10 Pessoas com Mais Projetos de Pesquisa')
plt.xlabel('Nome')
plt.ylabel('Quantidade de Projetos de Pesquisa')
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.tight_layout()
plt.savefig('bar_top10_pesquisa.png')
plt.show()

# Gráfico 5: Total de Projetos de Extensão vs. Total de Pessoas
plt.figure(figsize=(12, 6))
bar_total_extensao = sns.barplot(x=['Total Pessoas', 'Total Projetos de Extensão'],
                                y=[len(data_projetos), data_projetos['Total de Projetos de Extensão'].sum()],
                                palette=['lightblue', 'lightgreen'], hue=['Total Pessoas', 'Total Projetos de Extensão'],
                                legend=False)
plt.title('Total de Pessoas vs. Total de Projetos de Extensão')
plt.xlabel('Categorias')
plt.ylabel('Quantidade')
plt.savefig('bar_total_extensao.png')
plt.show()

# Gráfico 6: Ano do Primeiro Projeto de Extensão vs. Quantidade de Pessoas
plt.figure(figsize=(12, 6))
sns.countplot(x='Ano de Conclusão do Primeiro Projeto de Extensão', data=data_projetos, palette='Greens')
plt.title('Quantidade de Pessoas por Ano do Primeiro Projeto de Extensão')
plt.xlabel('Ano do Primeiro Projeto de Extensão')
plt.ylabel('Quantidade de Pessoas')
plt.xticks(rotation=45, ha='right')
plt.savefig('bar_anos_primeiro_extensao.png')
plt.show()

# Gráfico 7: Ano do Último Projeto de Extensão vs. Quantidade de Pessoas
plt.figure(figsize=(12, 6))
sns.countplot(x='Ano de Conclusão do Último Projeto de Extensão', data=data_projetos, palette='Greens')
plt.title('Quantidade de Pessoas por Ano do Último Projeto de Extensão')
plt.xlabel('Ano do Último Projeto de Extensão')
plt.ylabel('Quantidade de Pessoas')
plt.xticks(rotation=45, ha='right')
plt.savefig('bar_anos_ultimo_extensao.png')
plt.show()

# Gráfico 8: Top 10 Pessoas com Mais Projetos de Extensão
top10_extensao = data_projetos.sort_values(by='Total de Projetos de Extensão', ascending=False).head(10)
plt.figure(figsize=(15, 6))
bar_top10_extensao = sns.barplot(x=top10_extensao['Nome'], y=top10_extensao['Total de Projetos de Extensão'], color='lightgreen')
plt.title('Top 10 Pessoas com Mais Projetos de Extensão')
plt.xlabel('Nome')
plt.ylabel('Quantidade de Projetos de Extensão')
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.tight_layout()
plt.savefig('bar_top10_extensao.png')
plt.show()

# Gráfico 9: Total de Projetos de Desenvolvimento vs. Total de Pessoas
plt.figure(figsize=(12, 6))
bar_total_desenvolvimento = sns.barplot(x=['Total Pessoas', 'Total Projetos de Desenvolvimento'],
                                        y=[len(data_projetos), data_projetos['Total de Projetos de Desenvolvimento'].sum()],
                                        palette=['lightblue', 'lightgreen'], hue=['Total Pessoas', 'Total Projetos de Desenvolvimento'],
                                        legend=False)
plt.title('Total de Pessoas vs. Total de Projetos de Desenvolvimento')
plt.xlabel('Categorias')
plt.ylabel('Quantidade')
plt.savefig('bar_total_desenvolvimento.png')
plt.show()

# Gráfico 10: Ano do Primeiro Projeto de Desenvolvimento vs. Quantidade de Pessoas
plt.figure(figsize=(12, 6))
sns.countplot(x='Ano de Conclusão do Primeiro Projeto de Desenvolvimento', data=data_projetos, palette='Oranges')
plt.title('Quantidade de Pessoas por Ano do Primeiro Projeto de Desenvolvimento')
plt.xlabel('Ano do Primeiro Projeto de Desenvolvimento')
plt.ylabel('Quantidade de Pessoas')
plt.xticks(rotation=45, ha='right')
plt.savefig('bar_anos_primeiro_desenvolvimento.png')
plt.show()

# Gráfico 11: Ano do Último Projeto de Desenvolvimento vs. Quantidade de Pessoas
plt.figure(figsize=(12, 6))
sns.countplot(x='Ano de Conclusão do Último Projeto de Desenvolvimento', data=data_projetos, palette='Oranges')
plt.title('Quantidade de Pessoas por Ano do Último Projeto de Desenvolvimento')
plt.xlabel('Ano do Último Projeto de Desenvolvimento')
plt.ylabel('Quantidade de Pessoas')
plt.xticks(rotation=45, ha='right')
plt.savefig('bar_anos_ultimo_desenvolvimento.png')
plt.show()

# Gráfico 12: Top 10 Pessoas com Mais Projetos de Desenvolvimento
top10_desenvolvimento = data_projetos.sort_values(by='Total de Projetos de Desenvolvimento', ascending=False).head(10)
plt.figure(figsize=(15, 6))
bar_top10_desenvolvimento = sns.barplot(x=top10_desenvolvimento['Nome'], y=top10_desenvolvimento['Total de Projetos de Desenvolvimento'], color='orange')
plt.title('Top 10 Pessoas com Mais Projetos de Desenvolvimento')
plt.xlabel('Nome')
plt.ylabel('Quantidade de Projetos de Desenvolvimento')
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.tight_layout()
plt.savefig('bar_top10_desenvolvimento.png')
plt.show()
