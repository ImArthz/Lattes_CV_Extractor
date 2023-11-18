import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Leitura do arquivo CSV
df_idiomas = pd.read_csv('idiomas.csv')

# Separando os idiomas para contar a frequência
idiomas_separados = df_idiomas['Idioma'].str.split(', ', expand=True).stack()

# Contando a frequência de cada idioma
frequencia_idiomas = idiomas_separados.value_counts()

# Configurando o estilo do seaborn
sns.set(style="whitegrid")

# Criando o gráfico de barras
plt.figure(figsize=(12, 6))
sns.barplot(x=frequencia_idiomas.index, y=frequencia_idiomas.values, hue=frequencia_idiomas.index, palette="viridis", legend=False)
plt.title('Distribuição de Idiomas')
plt.xlabel('Idioma')
plt.ylabel('Frequência')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Salvando o gráfico como uma imagem
plt.savefig('grafico_idiomas.png')

# Exibindo o gráfico
plt.show()
