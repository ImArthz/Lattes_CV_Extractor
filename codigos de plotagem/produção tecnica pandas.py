import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregando os dados do arquivo CSV
data_tecnicos = pd.read_csv("Produção tecnica.csv")

# Convertendo os anos para inteiros e removendo .0
data_tecnicos['Ano do Primeiro Trabalho técnico'] = data_tecnicos['Ano do Primeiro Trabalho técnico'].fillna(0).astype(int)
data_tecnicos['Ano do Último Trabalho técnico'] = data_tecnicos['Ano do Último Trabalho técnico'].fillna(0).astype(int)

# Gráfico 1: Número total de pessoas vs. Total de trabalhos técnicos
plt.figure(figsize=(12, 6))
bar_total_tecnicos = sns.barplot(x=['Total Pessoas', 'Total Trabalhos Técnicos'],
                                y=[len(data_tecnicos), data_tecnicos['Total de Trabalhos técnicos'].sum()],
                                palette=['lightblue', 'lightgreen'], hue=['Total Pessoas', 'Total Trabalhos Técnicos'],
                                legend=False)
plt.title('Número Total de Pessoas vs. Total de Trabalhos Técnicos')
plt.xlabel('Categorias')
plt.ylabel('Quantidade')
plt.savefig('bar_total_tecnicos.png')
plt.show()

# Gráfico 2: Top 10 pessoas com mais trabalhos técnicos
top10_tecnicos = data_tecnicos.sort_values(by='Total de Trabalhos técnicos', ascending=False).head(10)
plt.figure(figsize=(15, 6))
bar_top10_tecnicos = sns.barplot(x=top10_tecnicos['Nome'], y=top10_tecnicos['Total de Trabalhos técnicos'], color='lightblue')
plt.title('Top 10 Pessoas com Mais Trabalhos Técnicos')
plt.xlabel('Nome')
plt.ylabel('Quantidade de Trabalhos Técnicos')
plt.xticks(rotation=45, ha='right', fontsize=10)  # Ajuste do tamanho e rotação dos rótulos
plt.tight_layout()  # Ajuste para evitar corte
plt.savefig('bar_top10_tecnicos.png')
plt.show()

# Paleta de cores personalizada para os anos
cores_ano_inicio = sns.light_palette('green', as_cmap=True)
cores_ano_final = sns.light_palette('coral', as_cmap=True)

# Gráfico 3: Relacionando anos do primeiro trabalho técnico com a quantidade de pessoas
plt.figure(figsize=(12, 6))
sns.countplot(x='Ano do Primeiro Trabalho técnico', data=data_tecnicos, palette=cores_ano_inicio, hue='Ano do Primeiro Trabalho técnico', legend=False)
plt.title('Quantidade de Pessoas por Ano do Primeiro Trabalho Técnico')
plt.xlabel('Ano do Primeiro Trabalho Técnico')
plt.ylabel('Quantidade de Pessoas')
plt.xticks(rotation=45, ha='right')
plt.ylim(0, 100)  # Ajuste da escala do eixo y
plt.savefig('bar_anos_primeiro_tecnico.png')
plt.show()

# Gráfico 4: Relacionando anos do último trabalho técnico com a quantidade de pessoas
plt.figure(figsize=(12, 6))
sns.countplot(x='Ano do Último Trabalho técnico', data=data_tecnicos, palette=cores_ano_final, hue='Ano do Último Trabalho técnico', legend=False)
plt.title('Quantidade de Pessoas por Ano do Último Trabalho Técnico')
plt.xlabel('Ano do Último Trabalho Técnico')
plt.ylabel('Quantidade de Pessoas')
plt.xticks(rotation=45, ha='right')
plt.ylim(0, 100)  # Ajuste da escala do eixo y
plt.savefig('bar_anos_ultimo_tecnico.png')
plt.show()
