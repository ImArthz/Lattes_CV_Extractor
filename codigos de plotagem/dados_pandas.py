import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar os dados do CSV
df_dados = pd.read_csv('dadoszip.csv')

# Análise 1: Top 10 cidades dos pesquisadores
plt.figure(figsize=(12, 6))
sns.countplot(x='Cidade de Nascimento', data=df_dados, order=df_dados['Cidade de Nascimento'].value_counts().head(10).index)
plt.title('Top 10 Cidades dos Pesquisadores')
plt.xlabel('Cidade')
plt.ylabel('Contagem')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('top_cidades_pesquisadores.png')
plt.show()

# Análise 2: Cursos de graduação mais comuns e instituições de graduação mais mencionadas
plt.figure(figsize=(12, 6))
sns.countplot(x='Nome do Curso de graduação', data=df_dados, order=df_dados['Nome do Curso de graduação'].value_counts().head(10).index)
plt.title('Cursos de Graduação Mais Comuns')
plt.xlabel('Curso de Graduação')
plt.ylabel('Contagem')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('cursos_graduacao_comuns.png')
plt.show()

plt.figure(figsize=(12, 6))
sns.countplot(x='Nome da instituição', data=df_dados, order=df_dados['Nome da instituição'].value_counts().head(10).index)
plt.title('Instituições de Graduação Mais Mencionadas')
plt.xlabel('Instituição de Graduação')
plt.ylabel('Contagem')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('instituicoes_graduacao_mencionadas.png')
plt.show()
# Análise 6: Especializações mais comuns
plt.figure(figsize=(12, 6))
sns.countplot(x='Quantidade De especializações', data=df_dados, order=df_dados['Quantidade De especializações'].value_counts().head(10).index)
plt.title('Quantidade de Especializações Por Pesquisador')
plt.xlabel('Quantidade de Especializações')
plt.ylabel('Contagem')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('quantidade_especializacoes.png')
plt.show()

'''
# Análise 3: Cursos de mestrado mais comuns e instituições de mestrado mais mencionadas
plt.figure(figsize=(12, 6))
sns.countplot(x='Mestrado Nome do curso', data=df_dados, order=df_dados['Mestrado Nome do curso'].value_counts().head(10).index)
plt.title('Cursos de Mestrado Mais Comuns')
plt.xlabel('Curso de Mestrado')
plt.ylabel('Contagem')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('cursos_mestrado_comuns.png')
plt.show()

plt.figure(figsize=(12, 6))
sns.countplot(x='Mestrado Nome da instituição', data=df_dados, order=df_dados['Mestrado Nome da instituição'].value_counts().head(10).index)
plt.title('Instituições de Mestrado Mais Mencionadas')
plt.xlabel('Instituição de Mestrado')
plt.ylabel('Contagem')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('instituicoes_mestrado_mencionadas.png')
plt.show()
'''
'''
# Análise 4: Cursos de doutorado mais comuns e instituições de doutorado mais mencionadas
plt.figure(figsize=(12, 6))
sns.countplot(x='Doutorado Nome do curso', data=df_dados, order=df_dados['Doutorado Nome do curso'].value_counts().head(10).index)
plt.title('Cursos de Doutorado Mais Comuns')
plt.xlabel('Curso de Doutorado')
plt.ylabel('Contagem')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('cursos_doutorado_comuns.png')
plt.show()

plt.figure(figsize=(12, 6))
sns.countplot(x='Doutorado Nome da instituição', data=df_dados, order=df_dados['Doutorado Nome da instituição'].value_counts().head(10).index)
plt.title('Instituições de Doutorado Mais Mencionadas')
plt.xlabel('Instituição de Doutorado')
plt.ylabel('Contagem')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('instituicoes_doutorado_mencionadas.png')
plt.show()
'''
'''
# Análise 5: Cursos de formação complementar mais comuns e instituições de formação complementar mais mencionadas
plt.figure(figsize=(12, 6))
sns.countplot(x='Formação Complementar Nome do curso', data=df_dados, order=df_dados['Formação Complementar Nome do curso'].value_counts().head(10).index)
plt.title('Cursos de Formação Complementar Mais Comuns')
plt.xlabel('Curso de Formação Complementar')
plt.ylabel('Contagem')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('cursos_formacao_complementar_comuns.png')
plt.show()

plt.figure(figsize=(12, 6))
sns.countplot(x='Formação Complementar Intituiçao', data=df_dados, order=df_dados['Formação Complementar Intituiçao'].value_counts().head(10).index)
plt.title('Instituições de Formação Complementar Mais Mencionadas')
plt.xlabel('Instituição de Formação Complementar')
plt.ylabel('Contagem')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('instituicoes_formacao_complementar_mencionadas.png')
plt.show()
'''
# Análise 6: Especializações mais comuns
plt.figure(figsize=(12, 6))
sns.countplot(x='Quantidade De especializações', data=df_dados, order=df_dados['Quantidade De especializações'].value_counts().head(10).index)
plt.title('Quantidade de Especializações Mais Comuns')
plt.xlabel('Quantidade de Especializações')
plt.ylabel('Contagem')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('quantidade_especializacoes_comuns.png')
plt.show()
