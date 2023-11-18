import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregando os dados do arquivo CSV
data_bancas = pd.read_csv("bancas doutorado & mestrado.csv")

# Gráfico 1: Total de Participação em Bancas vs Quantidade de Pessoas
plt.figure(figsize=(12, 6))
bar_participacao_bancas = sns.barplot(x=['Total Pessoas', 'Total Participação em Bancas'],
                                    y=[len(data_bancas), data_bancas['Total de Participação em Bancas'].sum()],
                                    palette=['lightblue', 'lightgreen'], hue=['Total Pessoas', 'Total Participação em Bancas'],
                                    legend=False)
plt.title('Total de Pessoas vs. Total de Participação em Bancas')
plt.xlabel('Categorias')
plt.ylabel('Quantidade')
plt.savefig('bar_participacao_bancas.png')
plt.show()

# Gráfico 2: Top 10 Pessoas com Mais Participação em Bancas
top10_participacao_bancas = data_bancas.sort_values(by='Total de Participação em Bancas', ascending=False).head(10)
plt.figure(figsize=(15, 6))
bar_top10_participacao_bancas = sns.barplot(x=top10_participacao_bancas['Nome'], y=top10_participacao_bancas['Total de Participação em Bancas'], color='lightblue')
plt.title('Top 10 Pessoas com Mais Participação em Bancas')
plt.xlabel('Nome')
plt.ylabel('Quantidade de Participação em Bancas')
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.tight_layout()
plt.savefig('bar_top10_participacao_bancas.png')
plt.show()

# Gráfico 3: Total de Participação em Eventos vs Quantidade de Pessoas
plt.figure(figsize=(12, 6))
bar_participacao_eventos = sns.barplot(x=['Total Pessoas', 'Total Participação em Eventos'],
                                    y=[len(data_bancas), data_bancas['Total de Participação em Eventos'].sum()],
                                    palette=['lightblue', 'lightgreen'], hue=['Total Pessoas', 'Total Participação em Eventos'],
                                    legend=False)
plt.title('Total de Pessoas vs. Total de Participação em Eventos')
plt.xlabel('Categorias')
plt.ylabel('Quantidade')
plt.savefig('bar_participacao_eventos.png')
plt.show()

# Gráfico 4: Pessoas com o Primeiro Evento em cada Ano do Primeiro Evento
plt.figure(figsize=(12, 6))
sns.countplot(x='Ano do Primeiro Evento', data=data_bancas, palette='Blues')
plt.title('Quantidade de Pessoas por Ano do Primeiro Evento')
plt.xlabel('Ano do Primeiro Evento')
plt.ylabel('Quantidade de Pessoas')
plt.xticks(rotation=45, ha='right')
plt.savefig('bar_anos_primeiro_evento.png')
plt.show()

# Gráfico 5: Pessoas com o Último Evento em cada Ano do Último Evento
plt.figure(figsize=(12, 6))
sns.countplot(x='Ano do Último Evento', data=data_bancas, palette='Blues')
plt.title('Quantidade de Pessoas por Ano do Último Evento')
plt.xlabel('Ano do Último Evento')
plt.ylabel('Quantidade de Pessoas')
plt.xticks(rotation=45, ha='right')
plt.savefig('bar_anos_ultimo_evento.png')
plt.show()

# Gráfico 6: Top 10 Pessoas com Mais Eventos
top10_participacao_eventos = data_bancas.sort_values(by='Total de Participação em Eventos', ascending=False).head(10)
plt.figure(figsize=(15, 6))
bar_top10_participacao_eventos = sns.barplot(x=top10_participacao_eventos['Nome'], y=top10_participacao_eventos['Total de Participação em Eventos'], color='lightgreen')
plt.title('Top 10 Pessoas com Mais Participação em Eventos')
plt.xlabel('Nome')
plt.ylabel('Quantidade de Participação em Eventos')
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.tight_layout()
plt.savefig('bar_top10_participacao_eventos.png')
plt.show()
