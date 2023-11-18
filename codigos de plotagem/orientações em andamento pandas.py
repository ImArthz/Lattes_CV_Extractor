import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregando os dados do arquivo CSV
data = pd.read_csv("orientações em andamento.csv")

# Calculando a quantidade total de pessoas
total_pessoas = len(data)

# Calculando a quantidade total de orientações em andamento
total_orientacoes_andamento = data['Orientações em Andamento'].sum()

# Calculando a quantidade total de orientações concluídas
total_orientacoes_concluidas = data['Orientações concluidas'].sum()

# Ajustando o estilo e as cores do Seaborn
sns.set(style="whitegrid")
colors = ['lightblue', 'lightgreen', 'lightcoral']

# Criando o gráfico de barras
plt.figure(figsize=(10, 6))
bar_total = sns.barplot(x=['Total Pessoas', 'Total Orientações em Andamento', 'Total Orientações Concluídas'],
                        y=[total_pessoas, total_orientacoes_andamento, total_orientacoes_concluidas],
                        palette=colors)
plt.title('Resumo Geral: Pessoas, Orientações em Andamento e Orientações Concluídas')
plt.xlabel('Categorias')
plt.ylabel('Quantidade')
plt.tight_layout()
plt.savefig('bar_resumo_geral.png')
plt.show()
