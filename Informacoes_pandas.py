import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download das stopwords e punkt do NLTK
import nltk
nltk.download('stopwords')
nltk.download('punkt')

# Leitura do arquivo CSV
df = pd.read_csv('informacoes.csv')

# Função para processar o texto e gerar a nuvem de palavras
def generate_wordcloud(data, column, title, save_as):
    text = ' '.join(data[column].dropna().astype(str).values)
    
    # Tokenização e remoção de stopwords
    stop_words = set(stopwords.words('portuguese'))
    words = word_tokenize(text.lower())
    words = [word for word in words if word.isalpha() and word not in stop_words]
    cleaned_text = ' '.join(words)
    
    # Geração da nuvem de palavras
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(cleaned_text)
    
    # Plotagem do gráfico
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(title)
    plt.savefig(save_as)
    plt.show()

# Gráfico para 'Linhas de Pesquisa'
generate_wordcloud(df, 'Linhas de Pesquisa', 'Palavras mais comuns em Linhas de Pesquisa', 'wordcloud_linhas_pesquisa.png')

# Gráfico para 'Áreas de Atuação'
generate_wordcloud(df, 'Áreas de Atuação', 'Palavras mais comuns em Áreas de Atuação', 'wordcloud_areas_atuacao.png')
