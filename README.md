# Projeto de Análise de Currículos Lattes - Cefet-MG

Este projeto, desenvolvido por Arthur De Oliveira Mendonça, é uma iniciativa da instituição Cefet-MG que visa facilitar a análise de currículos Lattes por meio da automação utilizando a linguagem de programação Python. O objetivo principal é extrair informações relevantes desses currículos, disponíveis em formato XML, e apresentá-las de maneira mais acessível por meio de gráficos gerados com a biblioteca Pandas.

## Objetivo do Projeto

O propósito central deste projeto é proporcionar uma maneira eficiente e prática de analisar currículos acadêmicos, com foco na comunidade do Cefet-MG. O processo envolve a conversão de currículos Lattes em formato XML para arquivos CSV, seguido pela criação de gráficos informativos e visuais. Essa abordagem permite uma compreensão mais clara e eficaz das informações presentes nos currículos.

## Pré-requisitos

Antes de executar o projeto, certifique-se de atender aos seguintes pré-requisitos:

1. **Python:** Certifique-se de ter o Python instalado em seu sistema. Você pode baixar a versão mais recente em [python.org](https://www.python.org/downloads/).

2. **Bibliotecas Python:** Instale as bibliotecas necessárias usando o seguinte comando no terminal:

   ```bash
   pip install pandas
   ```
## Estrutura de Diretórios

  O projeto possui uma estrutura específica de diretórios que deve ser seguida para garantir o funcionamento adequado:

1 **codigos de_plotagem/**: Esta pasta contém os códigos em Pandas utilizados para a plotagem de gráficos. Extraia os arquivos desta pasta antes de executar o código principal.

2 **csv's/**: Nesta pasta, serão armazenados os arquivos CSV gerados pelo código principal. Certifique-se de extrair os CSVs para o mesmo diretório do código de plotagem antes de executá-lo.

3 **collectionn/**: Este é o diretório padrão onde os arquivos XML dos currículos Lattes serão pesquisados. Modifique a variável pasta_raiz no código para o caminho desejado antes de executar o projeto. 
```bash
pasta_raiz = r'C:\Users\Arthur\Desktop\pyp\collectionn'
```
### exemplo
```bash
pasta_raiz = r'c:\Users\Seu_usuario\Pathing\Nome_da_pasta_geral\Nome_da_pasta_da_base_de_dados'
```
# Conversor

## explicando o codigo
### Definindo variavel para as pastas csv que vão ser geradas 
```bash
pasta_raiz = r'C:\Users\Arthur\Desktop\pyp\collectionn'  # Define a pasta raiz onde os arquivos serão pesquisados
linkpadrao = None
arquivo_csv = "dadoszip.csv"  # Define o nome do arquivo CSV que será criado
arquivo2_csv = "informacoes.csv"  # Define o nome do segundo arquivo CSV que será criado
arquivo3_csv = "idiomas.csv"  # Define o nome do terceiro arquivo CSV que será criado
arquivo4_csv = "projetos.csv" #Define o nome do quarto arquivo CSV que será criado
arquivo5_csv = "publicacoes.csv"  # Define o nome do quinto arquivo CSV que será criado
arquivo6_csv ="produção tecnica.csv" #Define o nome do sexto arquivo csv que será criado 
arquivo7_csv = "bancas doutorado & mestrado.csv"#Define o nome do setimo arquivo csv que será criado
arquivo8_csv ="orientações em andamento.csv"#Define o nome do oitavo arquivo csv que será criado
```
### funções gerais 
#### obter ano
obter_ano(elemento): Esta função recebe um elemento XML como argumento. Ela verifica se o elemento não é nulo e, se não for, tenta obter o ano do artigo a partir dos atributos do elemento. A prioridade é dada aos atributos 'ANO-DO-ARTIGO', 'ANO' e 'ANO-DA-APRESENTACAO'. Se um desses atributos estiver presente, o ano é retornado após remover espaços em branco. Se nenhum atributo estiver presente, a função retorna uma string vazia.
```bash
def obter_ano(elemento):
    if elemento is not None:
        ano_elemento = elemento.attrib.get('ANO-DO-ARTIGO') or elemento.attrib.get('ANO') or elemento.attrib.get('ANO-DA-APRESENTACAO')
        if ano_elemento is not None:
            return ano_elemento.strip()
    return ""
```
#### obter ano do artigo
obter_ano_do_artigo(elemento): Semelhante à primeira função, esta também recebe um elemento XML como argumento. Ela verifica se o elemento não é nulo e, em seguida, tenta obter o ano do artigo específico. Neste caso, ela procura o elemento 'DADOS-BASICOS-DO-ARTIGO' e extrai o atributo 'ANO-DO-ARTIGO'. Se o atributo estiver presente, o ano é retornado após remover espaços em branco. Caso contrário, uma string vazia é retornada.

```bash
def obter_ano_do_artigo(elemento):
    if elemento is not None:
        ano_artigo = elemento.find('DADOS-BASICOS-DO-ARTIGO').attrib.get('ANO-DO-ARTIGO')
        if ano_artigo is not None:
            return ano_artigo.strip()
    return ""
```
#### obter ano da apresentação
obter_ano_da_apresentacao(elemento): Esta função também recebe um elemento XML como argumento. Ela verifica se o elemento não é nulo e tenta obter o ano da apresentação a partir do atributo 'ANO-DA-APRESENTACAO'. Se o atributo estiver presente, o ano é retornado após remover espaços em branco. Caso contrário, uma string vazia é retornada.
```bash
def obter_ano_da_apresentacao(elemento):
    if elemento is not None:
        ano_apresentacao = elemento.attrib.get('ANO-DA-APRESENTACAO')
        if ano_apresentacao is not None:
            return ano_apresentacao.strip()
    return ""
```
#### get atrrib value ( obter valor do atributo)
get_attrib_value(element, attribute): Esta função é uma função auxiliar que recebe um elemento XML e um nome de atributo como argumentos. Ela retorna o valor do atributo se o elemento não for nulo, caso contrário, retorna None.
```bash
def get_attrib_value(element, attribute):
    return element.attrib.get(attribute) if element is not None else None
```
#### get first element( obter primeiro elemento)

get_first_element(root, xpath): Outra função auxiliar que recebe um elemento raiz XML e um caminho XPath como argumentos. Ela encontra todos os elementos correspondentes ao caminho XPath no elemento raiz e retorna o primeiro elemento encontrado, ou None se nenhum elemento for encontrado.
```bash
def get_first_element(root, xpath):
    elements = root.findall(xpath)
    return elements[0] if elements else None
```
#### get element text ( obter texto do elemento) 
get_element_text(element): A última função auxiliar recebe um elemento XML como argumento e retorna o texto contido nesse elemento, removendo espaços em branco. Se o elemento for nulo, retorna None.
```bash
def get_element_text(element):
    return element.text if element is not None else None
```
Essas funções são úteis para extrair informações específicas de elementos XML, como anos de artigos, anos de apresentação e valores de atributos. Elas são utilizadas no  código principal para obter informações relevantes dos currículos Lattes e facilitar a reutilização do delas .
### coversão para os arquivos 
#### dados.zip
```bash
def arquivo1():
    print(f"Iniciando extração para {arquivo_csv} ... ")
    # Abre o arquivo CSV 'arquivo_csv' em modo de escrita e cria um objeto writer para escrever linhas no arquivo
    with open(arquivo_csv, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Numero Identificador', 'Nome', 'Cidade de Nascimento', 'Nome em citações bibliográficas', 'Nome da instituição',
                        'Endereço profissional da instituição', 'Cep', 'Cidade', 'DDD', 'Telefone profissional', 'Nome do Curso de graduação', 'Nome da instituição',
                        'Ano de Início', 'Ano de conclusão', 'Mestrado Nome da instituiçao', 'mestrado nome do curso', 'mestrado ano inicio',
                        'mestrado ano conclusão', 'mestrado titulo da tese', 'doutorado nome da intituição', 'doutorado nome do curso',
                        'doutado ano de inicio', 'doutorado ano de conlusao', 'doutorado titulo da tese', 'formação complementar Nome do curso',
                        'formação complementar intituiçao', 'formação complementar ano inicio', 'formação complementar ano de conclusão','Quantidade De especializações'])
    
        # Percorre recursivamente todas as pastas e arquivos na árvore de diretórios a partir da pasta raiz (pasta_raiz)
        for pasta, subpastas, arquivos in os.walk(pasta_raiz):
            for arquivo in arquivos:
                if arquivo.endswith(".zip"):  # Verifica se o arquivo possui a extensão ".zip"
                    arquivo_zip = os.path.join(pasta, arquivo)  # Caminho completo para o arquivo ZIP
    
                    # Abre o arquivo ZIP e itera sobre as entradas do arquivo
                    with zipfile.ZipFile(arquivo_zip, 'r') as zf:
                        for entry in zf.infolist():
                            if entry.filename.endswith(".xml"):  # Verifica se a entrada do arquivo é um arquivo XML
                                xml_file = zf.extract(entry, path=pasta)  # Extrai o arquivo XML para a pasta atual
    
                                tree = ET.parse(xml_file)  # Faz o parse do arquivo XML
                                root = tree.getroot()  # Obtém o elemento raiz do XML
                                numero_identificador = root.attrib.get("NUMERO-IDENTIFICADOR")  # Obtém o número identificador do elemento raiz
    
                                dadosgerais_element = root.find("./DADOS-GERAIS")  # Obtém o elemento DADOS-GERAIS do XML
                                if dadosgerais_element is not None:
                                    # Obtém informações do elemento DADOS-GERAIS, como nome completo, cidade de nascimento e nome em citações bibliográficas
                                    nome_completo = get_attrib_value(dadosgerais_element, "NOME-COMPLETO")
                                    cidade_nascimento = get_attrib_value(dadosgerais_element, "CIDADE-NASCIMENTO")
                                    nome_citacao = get_attrib_value(dadosgerais_element, "NOME-EM-CITACOES-BIBLIOGRAFICAS")
                                else:
                                    nome_completo = cidade_nascimento = nome_citacao = None
    
                                endereco_element = get_first_element(root, "./DADOS-GERAIS/ENDERECO/ENDERECO-PROFISSIONAL")  # Obtém o elemento ENDERECO-PROFISSIONAL do XML
                                if endereco_element is not None:
                                    # Obtém informações do endereço profissional, como nome da instituição, logradouro, cidade, cep, telefone e ddd
                                    endereco_nome = get_attrib_value(endereco_element, "NOME-INSTITUICAO-EMPRESA")
                                    endereco_logradouro = get_attrib_value(endereco_element, "LOGRADOURO-COMPLEMENTO")
                                    endereco_cidade = get_attrib_value(endereco_element, "CIDADE")
                                    endereco_cep = get_attrib_value(endereco_element, "CEP")
                                    endereco_telefone = get_attrib_value(endereco_element, "TELEFONE")
                                    endereco_telefone_ddd = get_attrib_value(endereco_element, "DDD")
                                else:
                                    endereco_nome = endereco_logradouro = endereco_cidade = endereco_cep = endereco_telefone = endereco_telefone_ddd = None
    
                                graduacao_element = get_first_element(root, "./DADOS-GERAIS/FORMACAO-ACADEMICA-TITULACAO/GRADUACAO")  # Obtém o elemento GRADUACAO do XML
                                if graduacao_element is not None:
                                    # Obtém informações da graduação, como nome do curso, nome da instituição, ano de início e ano de conclusão
                                    graduacao_nome_instituicao = get_attrib_value(graduacao_element, "NOME-INSTITUICAO")
                                    graduacao_nome_curso = get_attrib_value(graduacao_element, "NOME-CURSO")
                                    graduacao_ano_inicio = get_attrib_value(graduacao_element, "ANO-DE-INICIO")
                                    graduacao_ano_conclusao = get_attrib_value(graduacao_element, "ANO-DE-CONCLUSAO")
                                else:
                                    graduacao_nome_instituicao = graduacao_nome_curso = graduacao_ano_inicio = graduacao_ano_conclusao = None
    
                                mestrado_element = get_first_element(root, "./DADOS-GERAIS/FORMACAO-ACADEMICA-TITULACAO/MESTRADO")  # Obtém o elemento MESTRADO do XML
                                if mestrado_element is not None:
                                    # Obtém informações do mestrado, como nome da instituição, nome do curso, ano de início, ano de conclusão e título da tese
                                    mestrado_nome_instituicao = get_attrib_value(mestrado_element, "NOME-INSTITUICAO")
                                    mestrado_nome_curso = get_attrib_value(mestrado_element, "NOME-CURSO")
                                    mestrado_ano_inicio = get_attrib_value(mestrado_element, "ANO-DE-INICIO")
                                    mestrado_ano_conclusao = get_attrib_value(mestrado_element, "ANO-DE-CONCLUSAO")
                                    mestrado_titulo_tese = get_attrib_value(mestrado_element, "TITULO-DA-DISSERTACAO-TESE")
                                else:
                                    mestrado_nome_instituicao = mestrado_nome_curso = mestrado_ano_inicio = mestrado_ano_conclusao = mestrado_titulo_tese = None
    
                                doutorado_element = get_first_element(root, "./DADOS-GERAIS/FORMACAO-ACADEMICA-TITULACAO/DOUTORADO")  # Obtém o elemento DOUTORADO do XML
                                if doutorado_element is not None:
                                    # Obtém informações do doutorado, como nome da instituição, nome do curso, ano de início, ano de conclusão e título da tese
                                    doutorado_nome_instituicao = get_attrib_value(doutorado_element, "NOME-INSTITUICAO")
                                    doutorado_nome_curso = get_attrib_value(doutorado_element, "NOME-CURSO")
                                    doutorado_ano_inicio = get_attrib_value(doutorado_element, "ANO-DE-INICIO")
                                    doutorado_ano_conclusao = get_attrib_value(doutorado_element, "ANO-DE-CONCLUSAO")
                                    doutorado_titulo_tese = get_attrib_value(doutorado_element, "TITULO-DA-DISSERTACAO-TESE")
                                else:
                                    doutorado_nome_instituicao = doutorado_nome_curso = doutorado_ano_inicio = doutorado_ano_conclusao = doutorado_titulo_tese = None
    
                                formacao_complementar_element = get_first_element(root, "./DADOS-COMPLEMENTARES/FORMACAO-COMPLEMENTAR/FORMACAO-COMPLEMENTAR-CURSO-DE-CURTA-DURACAO")  # Obtém o elemento FORMACAO-COMPLEMENTAR-DE-EXTENSAO-UNIVERSITARIA do XML
                                if formacao_complementar_element is not None:
                                    # Obtém informações da formação complementar, como nome do curso, nome da instituição, ano de início e ano de conclusão
                                    formacaocompl_nome_curso = get_attrib_value(formacao_complementar_element, "NOME-CURSO")
                                    formacaocompl_nome_instituicao = get_attrib_value(formacao_complementar_element, "NOME-INSTITUICAO")
                                    formacaocompl_ano_inicio = get_attrib_value(formacao_complementar_element, "ANO-DE-INICIO")
                                    formacaocompl_ano_conclusao = get_attrib_value(formacao_complementar_element, "ANO-DE-CONCLUSAO")
                                else:
                                    formacaocompl_nome_curso = formacaocompl_nome_instituicao = formacaocompl_ano_inicio = formacaocompl_ano_conclusao = None
                                #Obtém informações sobre os cursos de especialização
                                especializacao_element = root.findall('./DADOS-COMPLEMENTARES/INFORMACOES-ADICIONAIS-CURSOS/INFORMACAO-ADICIONAL-CURSO[@NIVEL-CURSO="ESPECIALIZACAO"]')
                                if especializacao_element is not None:
                                    quantidade_especializacoes = len(especializacao_element)
                                else:
                                    quantidade_especializacoes = None                                    
    
                                # Escreve uma linha com as informações extraídas no arquivo CSV
                                writer.writerow([numero_identificador, nome_completo, cidade_nascimento,
                                                nome_citacao, endereco_nome, endereco_logradouro, endereco_cep,
                                                endereco_cidade, endereco_telefone_ddd, endereco_telefone,
                                                graduacao_nome_curso, graduacao_nome_instituicao,
                                                graduacao_ano_inicio, graduacao_ano_conclusao, mestrado_nome_instituicao,
                                                mestrado_nome_curso, mestrado_ano_inicio, mestrado_ano_conclusao,
                                                mestrado_titulo_tese, doutorado_nome_instituicao,
                                                doutorado_nome_curso, doutorado_ano_inicio, doutorado_ano_conclusao,
                                                doutorado_titulo_tese, formacaocompl_nome_curso,
                                                formacaocompl_nome_instituicao, formacaocompl_ano_inicio,
                                                formacaocompl_ano_conclusao,quantidade_especializacoes])
    
        print(f"Os dados foram convertidos e armazenados no arquivo '{arquivo_csv}'.")
```
A função inicia imprimindo uma mensagem indicando que a extração está começando para o arquivo CSV (arquivo_csv).
##### Abertura do Arquivo CSV:

Abre o arquivo CSV em modo de escrita (mode='w').
Cria um objeto writer usando a biblioteca csv para escrever linhas no arquivo.
Escreve a primeira linha no arquivo CSV, que contém os cabeçalhos das colunas.

##### Iteração sobre os Arquivos XML:

Utiliza a biblioteca os.walk para percorrer recursivamente todas as pastas e arquivos na árvore de diretórios a partir da pasta raiz (pasta_raiz).
Para cada arquivo encontrado, verifica se possui a extensão ".zip".
Se sim, abre o arquivo ZIP e itera sobre suas entradas.

##### Extração das Informações dos Currículos:

Para cada entrada no arquivo ZIP, verifica se é um arquivo XML (entry.filename.endswith(".xml")).
Se sim, extrai o arquivo XML para a pasta atual.
Faz o parse do arquivo XML utilizando a biblioteca xml.etree.ElementTree e obtém o elemento raiz (root).

##### Extração de Dados Específicos:

Utiliza diversas funções auxiliares para extrair informações específicas do currículo, como número identificador, dados gerais, endereço, formação acadêmica, etc.
**Exemplos**
1 **get_attrib_value**: Obtém o valor de um atributo de um elemento XML.
2 **get_first_element**: Obtém o primeiro elemento correspondente a um caminho XPath em um elemento raiz XML.

##### Escrita no Arquivo CSV:

Escreve uma linha no arquivo CSV contendo as informações extraídas do currículo.
As informações são organizadas conforme os cabeçalhos definidos anteriormente.

##### Feedback ao Usuário:

Imprime uma mensagem indicando que os dados foram convertidos e armazenados no arquivo CSV.

Resumidamente, a função percorre uma árvore de diretórios, identifica arquivos ZIP e XML, extrai informações específicas dos currículos Lattes contidos nesses arquivos XML e escreve essas informações em um arquivo CSV para análises posteriores.

#### informacoes.csv
```bash
def arquivo2():
    print(f"Iniciando extração para {arquivo2_csv} ... ")
    # Abre o arquivo CSV 'arquivo2_csv' em modo de escrita e cria um objeto writer para escrever linhas no arquivo
    with open(arquivo2_csv, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Identificador', 'Nome', 'Linhas de Pesquisa', 'Membros de Corpo Editorial', 'Revisores de Periódico', 'Revisores de Projeto de Fomento', 'Áreas de Atuação'])
    
        # Repete o processo de pesquisa de arquivos ZIP, extração de arquivos XML e processamento dos XMLs para gerar informações adicionais
        for pasta, subpastas, arquivos in os.walk(pasta_raiz):
            for arquivo in arquivos:
                if arquivo.endswith(".zip"):  # Verifica se o arquivo possui a extensão ".zip"
                    arquivo_zip = os.path.join(pasta, arquivo)  # Caminho completo para o arquivo ZIP
    
                    # Abre o arquivo ZIP e itera sobre as entradas do arquivo
                    with zipfile.ZipFile(arquivo_zip, 'r') as zf:
                        for entry in zf.infolist():
                            if entry.filename.endswith(".xml"):  # Verifica se a entrada do arquivo é um arquivo XML
                                xml_file = zf.extract(entry, path=pasta)  # Extrai o arquivo XML para a pasta atual
                                tree = ET.parse(xml_file)  # Faz o parse do arquivo XML
                                root = tree.getroot()  # Obtém o elemento raiz do XML
                                numero_identificador = root.attrib.get("NUMERO-IDENTIFICADOR")  # Obtém o número identificador do elemento raiz
                                nome_individuo = root.find('DADOS-GERAIS').attrib['NOME-COMPLETO']  # Obtém o nome do indivíduo
    
                                linhas_de_pesquisa = [linha.attrib['TITULO-DA-LINHA-DE-PESQUISA'] for linha in root.iter('LINHA-DE-PESQUISA')]  # Obtém as linhas de pesquisa
                                #areas_de_atuacao = [linha.attrib['NOME-DA-SUB-AREA-DO-CONHECIMENTO'] for linha in root.iter('AREAS-DE-ATUACAO')]  # Obtém as areas de atuacao
                                areas_de_atuacao = [area.get("NOME-DA-SUB-AREA-DO-CONHECIMENTO") for area in root.findall(".//AREA-DE-ATUACAO")]
                                areas_de_atuacao = [area for area in areas_de_atuacao if area is not None]  # Filtrar os valores None
                                # Conta a quantidade de membros de corpo editorial, revisores de periódico e revisores de projeto de fomento
                                quantidade_corpo_editorial = len(root.findall('.//ATUACAO-PROFISSIONAL[@OUTRO-ENQUADRAMENTO-FUNCIONAL-INFORMADO="Membro de corpo editorial"]'))
                                quantidade_revisor_periodico = len(root.findall('.//ATUACAO-PROFISSIONAL[@OUTRO-ENQUADRAMENTO-FUNCIONAL-INFORMADO="Revisor de periódico"]'))
                                quantidade_revisor_projeto = len(root.findall('.//ATUACAO-PROFISSIONAL[@OUTRO-ENQUADRAMENTO-FUNCIONAL-INFORMADO="Revisor de Projeto de Fomento"]'))
    
                                writer.writerow([numero_identificador, nome_individuo, ', '.join(linhas_de_pesquisa),
                                                quantidade_corpo_editorial, quantidade_revisor_periodico,
                                                quantidade_revisor_projeto, ', '.join(areas_de_atuacao)])
    
        print(f"Os dados foram convertidos e armazenados no arquivo '{arquivo2_csv}'.")
```
A função arquivo2() realiza a extração de informações específicas dos currículos Lattes relacionadas a atividades de pesquisa, corpo editorial, revisão de periódicos e áreas de atuação.
##### Vamos resumir o funcionamento dessa função:

A função começa imprimindo uma mensagem indicando que a extração está começando para o arquivo CSV (arquivo2_csv).
##### Abertura do Arquivo CSV:

Abre o arquivo CSV em modo de escrita (mode='w').
Cria um objeto writer usando a biblioteca csv para escrever linhas no arquivo.
Escreve a primeira linha no arquivo CSV, que contém os cabeçalhos das colunas.

##### Iteração sobre os Arquivos XML:

Utiliza a biblioteca os.walk para percorrer recursivamente todas as pastas e arquivos na árvore de diretórios a partir da pasta raiz (pasta_raiz).
Para cada arquivo encontrado, verifica se possui a extensão ".zip".
Se sim, abre o arquivo ZIP e itera sobre suas entradas.

##### Extração de Dados Específicos:

Para cada entrada no arquivo ZIP, verifica se é um arquivo XML (entry.filename.endswith(".xml")).
Se sim, extrai o arquivo XML para a pasta atual.
Faz o parse do arquivo XML utilizando a biblioteca xml.etree.ElementTree e obtém o elemento raiz (root).

##### Extração de Informações:

Obtém o número identificador e o nome do indivíduo diretamente do elemento raiz.
Obtém as linhas de pesquisa a partir dos elementos LINHA-DE-PESQUISA.
Obtém as áreas de atuação a partir dos elementos AREA-DE-ATUACAO.
Conta a quantidade de membros de corpo editorial, revisores de periódico e revisores de projeto de fomento.

##### Escrita no Arquivo CSV:

Escreve uma linha no arquivo CSV contendo as informações extraídas.
As informações são organizadas conforme os cabeçalhos definidos anteriormente.

##### Feedback ao Usuário:

Imprime uma mensagem indicando que os dados foram convertidos e armazenados no arquivo CSV.

####idiomas.csv
```bash
def arquivo3():
    print(f"Iniciando extração para {arquivo3_csv} ... ")

    # Abre o arquivo CSV 'arquivo3_csv' em modo de escrita e cria um objeto writer para escrever linhas no arquivo
    with open(arquivo3_csv, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Número Identificador', 'Nome', 'Idioma'])

        # Repete o processo de pesquisa de arquivos ZIP, extração de arquivos XML e processamento dos XMLs para gerar informações sobre idiomas
        for pasta, subpastas, arquivos in os.walk(pasta_raiz):
            for arquivo in arquivos:
                if arquivo.endswith(".zip"):  # Verifica se o arquivo possui a extensão ".zip"
                    arquivo_zip = os.path.join(pasta, arquivo)  # Caminho completo para o arquivo ZIP

                    # Abre o arquivo ZIP e itera sobre as entradas do arquivo
                    with zipfile.ZipFile(arquivo_zip, 'r') as zf:
                        for entry in zf.infolist():
                            if entry.filename.endswith(".xml"):  # Verifica se a entrada do arquivo é um arquivo XML
                                xml_file = zf.extract(entry, path=pasta)  # Extrai o arquivo XML para a pasta atual
                                tree = ET.parse(xml_file)  # Faz o parse do arquivo XML
                                root = tree.getroot()  # Obtém o elemento raiz do XML
                                numero_identificador = root.attrib.get("NUMERO-IDENTIFICADOR", 'NAO_INFORMADO')  # Obtém o número identificador do elemento raiz
                                nome_individuo = root.find('DADOS-GERAIS').attrib.get('NOME-COMPLETO', 'NAO_INFORMADO')  # Obtém o nome do indivíduo
                                area_idioma = [area.get('DESCRICAO-DO-IDIOMA') for area in root.findall("./DADOS-GERAIS/IDIOMAS/IDIOMA")]
                                area_idioma = [area for area in area_idioma if area is not None]# Filtrar os valores None
                                # Escreve uma linha com as informações sobre idiomas no arquivo CSV
                                
                                writer.writerow([numero_identificador, nome_individuo,', ' .join(area_idioma)])

        print(f"Os dados foram convertidos e armazenados no arquivo '{arquivo3_csv}'.")
```
A função arquivo3() realiza a extração de informações específicas dos currículos Lattes relacionadas a idiomas. Aqui está uma explicação mais concisa:

A função começa imprimindo uma mensagem indicando que a extração está começando para o arquivo CSV (arquivo3_csv).
##### Abertura do Arquivo CSV:

Abre o arquivo CSV em modo de escrita (mode='w').
Cria um objeto writer usando a biblioteca csv para escrever linhas no arquivo.
Escreve a primeira linha no arquivo CSV, que contém os cabeçalhos das colunas.
##### Iteração sobre os Arquivos XML:

Utiliza a biblioteca os.walk para percorrer recursivamente todas as pastas e arquivos na árvore de diretórios a partir da pasta raiz (pasta_raiz).
Para cada arquivo encontrado, verifica se possui a extensão ".zip".
##### Extração de Dados Específicos:

Para cada entrada no arquivo ZIP, verifica se é um arquivo XML (entry.filename.endswith(".xml")).
Se sim, extrai o arquivo XML para a pasta atual.
Faz o parse do arquivo XML utilizando a biblioteca xml.etree.ElementTree e obtém o elemento raiz (root).
##### Extração de Informações:

Obtém o número identificador e o nome do indivíduo diretamente do elemento raiz.
Obtém a descrição dos idiomas a partir dos elementos IDIOMAS.
Os idiomas são organizados em uma lista, e valores None são filtrados.
##### Escrita no Arquivo CSV:

Escreve uma linha no arquivo CSV contendo as informações extraídas.
As informações são organizadas conforme os cabeçalhos definidos anteriormente.
##### Feedback ao Usuário:
Imprime uma mensagem indicando que os dados foram convertidos e armazenados no arquivo CSV
####projetos.csv
```bash
def arquivo4():
    print(f"Iniciando extração para {arquivo4_csv} ... ")
    with open(arquivo4_csv, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Número Identificador', 'Nome', 'Total de Projetos de Pesquisa',
                        'Ano de Conclusão do Primeiro Projeto de Pesquisa', 'Ano de Conclusão do Último Projeto de Pesquisa',
                        'Total de Projetos de Extensão', 'Ano de Conclusão do Primeiro Projeto de Extensão',
                        'Ano de Conclusão do Último Projeto de Extensão',
                        'Total de Projetos de Desenvolvimento', 'Ano de Conclusão do Primeiro Projeto de Desenvolvimento',
                        'Ano de Conclusão do Último Projeto de Desenvolvimento'])
    
        for pasta, subpastas, arquivos in os.walk(pasta_raiz):
            for arquivo in arquivos:
                if arquivo.endswith(".zip"):
                    arquivo_zip = os.path.join(pasta, arquivo)
    
                    with zipfile.ZipFile(arquivo_zip, 'r') as zf:
                        for entry in zf.infolist():
                            if entry.filename.endswith(".xml"):
                                xml_file = zf.extract(entry, path=pasta)
                                tree = ET.parse(xml_file)
                                root = tree.getroot()
                                numero_identificador = root.attrib.get("NUMERO-IDENTIFICADOR")
                                nome_individuo = root.find('DADOS-GERAIS').attrib['NOME-COMPLETO']
    
                                projetos_pesquisa = root.findall('.//PROJETO-DE-PESQUISA')#ou [@NATUREZA="PESQUISA"]
    
                                projetos_extensao = root.findall('.//PROJETO-DE-PESQUISA[@NATUREZA="EXTENSAO"]')
                                projetos_desenvolvimento = root.findall('.//PROJETO-DE-PESQUISA[@NATUREZA="DESENVOLVIMENTO"]')
    
                                total_projetos_pesquisa = len(projetos_pesquisa)
                                primeiro_projeto_pesquisa = projetos_pesquisa[0].attrib.get('ANO-FIM') if projetos_pesquisa else None
                                ultimo_projeto_pesquisa = projetos_pesquisa[-1].attrib.get('ANO-FIM') if projetos_pesquisa else None
    
                                total_projetos_extensao = len(projetos_extensao)
                                primeiro_projeto_extensao = projetos_extensao[0].attrib.get('ANO-FIM') if projetos_extensao else None
                                ultimo_projeto_extensao = projetos_extensao[-1].attrib.get('ANO-FIM') if projetos_extensao else None
    
                                total_projetos_desenvolvimento = len(projetos_desenvolvimento)
                                primeiro_projeto_desenvolvimento = projetos_desenvolvimento[0].attrib.get('ANO-FIM') if projetos_desenvolvimento else None
                                ultimo_projeto_desenvolvimento = projetos_desenvolvimento[-1].attrib.get('ANO-FIM') if projetos_desenvolvimento else None
    
                                writer.writerow([numero_identificador, nome_individuo, total_projetos_pesquisa,
                                                primeiro_projeto_pesquisa, ultimo_projeto_pesquisa,
                                                total_projetos_extensao, primeiro_projeto_extensao, ultimo_projeto_extensao,
                                                total_projetos_desenvolvimento, primeiro_projeto_desenvolvimento, ultimo_projeto_desenvolvimento])
    
        print(f"Os dados foram convertidos e armazenados no arquivo '{arquivo4_csv}'.")
```
A função arquivo4() extrai informações sobre projetos de pesquisa, projetos de extensão e projetos de desenvolvimento dos currículos Lattes, resumidamente:

A função começa imprimindo uma mensagem indicando que a extração está começando para o arquivo CSV (arquivo4_csv).
##### Abertura do Arquivo CSV:

Abre o arquivo CSV em modo de escrita (mode='w').
Cria um objeto writer usando a biblioteca csv para escrever linhas no arquivo.
Escreve a primeira linha no arquivo CSV, que contém os cabeçalhos das colunas.
##### Iteração sobre os Arquivos XML:

Utiliza a biblioteca os.walk para percorrer recursivamente todas as pastas e arquivos na árvore de diretórios a partir da pasta raiz (pasta_raiz).
Para cada arquivo encontrado, verifica se possui a extensão ".zip".
##### Extração de Dados Específicos:

Para cada entrada no arquivo ZIP, verifica se é um arquivo XML (entry.filename.endswith(".xml")).
Se sim, extrai o arquivo XML para a pasta atual.
Faz o parse do arquivo XML utilizando a biblioteca xml.etree.ElementTree e obtém o elemento raiz (root).
##### Extração de Informações:

Obtém o número identificador e o nome do indivíduo diretamente do elemento raiz.
Utiliza XPath para encontrar elementos relacionados a projetos de pesquisa, extensão e desenvolvimento.
Conta o total de projetos em cada categoria e obtém o ano de conclusão do primeiro e do último projeto em cada categoria.
##### Escrita no Arquivo CSV:

Escreve uma linha no arquivo CSV contendo as informações extraídas.
As informações são organizadas conforme os cabeçalhos definidos anteriormente.
##### Feedback ao Usuário:

Imprime uma mensagem indicando que os dados foram convertidos e armazenados no arquivo CSV.
#### publicacoes.csv
```bash
def arquivo5():
    print(f"Iniciando extração para {arquivo5_csv} ... ")
    with open(arquivo5_csv, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Número Identificador', 'Nome', 'Artigos Completos em Periódicos', 'Ano do Primeiro Artigo', 'Ano do Último Artigo',
                        'Livros Publicados/Organizados', 'Ano do Primeiro Livro', 'Ano do Último Livro',
                        'Capítulos de Livros Publicados', 'Ano do Primeiro Capítulo', 'Ano do Último Capítulo',
                        'Trabalhos Completos em Anais de Congressos', 'Ano do Primeiro Trabalho', 'Ano do Último Trabalho',
                        'Resumos Expandidos em Anais de Congressos', 'Ano do Primeiro Resumo Expandido', 'Ano do Último Resumo Expandido',
                        'Resumos em Anais de Congressos', 'Ano do Primeiro Resumo', 'Ano do Último Resumo',
                        'Apresentação de Trabalhos', 'Ano da Primeira Apresentação', 'Ano da Última Apresentação'])
    
        for pasta, subpastas, arquivos in os.walk(pasta_raiz):
            for arquivo in arquivos:
                if arquivo.endswith(".zip"):
                    arquivo_zip = os.path.join(pasta, arquivo)
    
                    with zipfile.ZipFile(arquivo_zip, 'r') as zf:
                        for entry in zf.infolist():
                            if entry.filename.endswith(".xml"):
                                xml_file = zf.extract(entry, path=pasta)
                                tree = ET.parse(xml_file)
                                root = tree.getroot()
                                numero_identificador = root.attrib.get("NUMERO-IDENTIFICADOR")
                                nome_individuo = root.find('DADOS-GERAIS').attrib.get('NOME-COMPLETO')
    
                                artigos_completos = root.findall('.//ARTIGO-PUBLICADO/DADOS-BASICOS-DO-ARTIGO[@NATUREZA="COMPLETO"]')
                                primeiro_artigo = artigos_completos[0].attrib.get('ANO-DO-ARTIGO') if artigos_completos else ""
                                ultimo_artigo = artigos_completos[-1].attrib.get('ANO-DO-ARTIGO') if artigos_completos else ""
    
                                livros_publicados = root.findall('.//LIVRO-PUBLICADO-OU-ORGANIZADO/DADOS-BASICOS-DO-LIVRO')#OU //livro-publicado-ou-organizado
                                primeiro_livro = livros_publicados[0].attrib.get('ANO') if livros_publicados else ""
                                ultimo_livro = livros_publicados[-1].attrib.get('ANO') if livros_publicados else ""
    
                                capitulos_livros = root.findall('.//CAPITULO-DE-LIVRO-PUBLICADO/DADOS-BASICOS-DO-CAPITULO')
                                primeiro_capitulo = capitulos_livros[0].attrib.get('ANO') if capitulos_livros else ""
                                ultimo_capitulo = capitulos_livros[-1].attrib.get('ANO') if capitulos_livros else ""
    
                                trabalhos_completos = root.findall('.//TRABALHO-EM-EVENTOS/DADOS-BASICOS-DO-TRABALHO[@NATUREZA="COMPLETO"]')
                                primeiro_trabalho = trabalhos_completos[0].attrib.get('ANO-DO-TRABALHO') if trabalhos_completos else ""
                                ultimo_trabalho = trabalhos_completos[-1].attrib.get('ANO-DO-TRABALHO') if trabalhos_completos else ""
    
                                resumos_expandidos = root.findall('.//TRABALHO-EM-EVENTOS/DADOS-BASICOS-DO-TRABALHO[@NATUREZA="RESUMO"]')#ou RESUMO-EXPANDIDO=EM-EVENTOS 
                                primeiro_resumo_expandido = resumos_expandidos[0].attrib.get('ANO-DO-TRABALHO') if resumos_expandidos else ""
                                ultimo_resumo_expandido = resumos_expandidos[-1].attrib.get('ANO-DO-TRABALHO') if resumos_expandidos else ""
    
                                resumos = root.findall('.//TRABALHO-EM-EVENTOS/DADOS-BASICOS-DO-TRABALHO[@NATUREZA="RESUMO_EXPANDIDO"]')#ou RESUMO-DE-TRABALHO-PUBLICADO
                                primeiro_resumo = resumos[0].attrib.get('ANO-DO-TRABALHO') if resumos else ""
                                ultimo_resumo = resumos[-1].attrib.get('ANO-DO-TRABALHO') if resumos else ""
    
                                apresentacao_trabalhos = root.findall('.//APRESENTACAO-DE-TRABALHO/DADOS-BASICOS-DA-APRESENTACAO-DE-TRABALHO')
                                primeira_apresentacao = apresentacao_trabalhos[0].attrib.get('ANO') if apresentacao_trabalhos else ""
                                ultima_apresentacao = apresentacao_trabalhos[-1].attrib.get('ANO') if apresentacao_trabalhos else ""
    
                                writer.writerow([numero_identificador, nome_individuo, len(artigos_completos), primeiro_artigo, ultimo_artigo,
                                                len(livros_publicados), primeiro_livro, ultimo_livro,
                                                len(capitulos_livros), primeiro_capitulo, ultimo_capitulo,
                                                len(trabalhos_completos), primeiro_trabalho, ultimo_trabalho,
                                                len(resumos_expandidos), primeiro_resumo_expandido, ultimo_resumo_expandido,
                                                len(resumos), primeiro_resumo, ultimo_resumo,
                                                len(apresentacao_trabalhos), primeira_apresentacao, ultima_apresentacao])
    
        print(f"Os dados foram convertidos e armazenados no arquivo '{arquivo5_csv}'.")
```
#####
A função arquivo5() realiza a extração de informações relacionadas a atividades acadêmicas específicas dos currículos Lattes. Aqui está um resumo mais conciso do que a função faz:

A função começa imprimindo uma mensagem indicando que a extração está começando para o arquivo CSV (arquivo5_csv).
##### Abertura do Arquivo CSV:

Abre o arquivo CSV em modo de escrita (mode='w').
Cria um objeto writer usando a biblioteca csv para escrever linhas no arquivo.
Escreve a primeira linha no arquivo CSV, que contém os cabeçalhos das colunas.
##### Iteração sobre os Arquivos XML:

Utiliza a biblioteca os.walk para percorrer recursivamente todas as pastas e arquivos na árvore de diretórios a partir da pasta raiz (pasta_raiz).
Para cada arquivo encontrado, verifica se possui a extensão ".zip".
##### Extração de Dados Específicos:

Para cada entrada no arquivo ZIP, verifica se é um arquivo XML (entry.filename.endswith(".xml")).
Se sim, extrai o arquivo XML para a pasta atual.
Faz o parse do arquivo XML utilizando a biblioteca xml.etree.ElementTree e obtém o elemento raiz (root).
##### Extração de Informações:

Obtém o número identificador e o nome do indivíduo diretamente do elemento raiz.
Utiliza XPath para encontrar elementos relacionados a diferentes tipos de atividades acadêmicas, como artigos, livros, capítulos de livros, etc.
Conta o número total de cada tipo de atividade e obtém o ano do primeiro e do último evento em cada categoria.
##### Escrita no Arquivo CSV:

Escreve uma linha no arquivo CSV contendo as informações extraídas.
As informações são organizadas conforme os cabeçalhos definidos anteriormente.
##### Feedback ao Usuário:

Imprime uma mensagem indicando que os dados foram convertidos e armazenados no arquivo CSV.
#### produção tecnica.csv
```bash
def arquivo6():
    print(f"Iniciando extração para {arquivo6_csv} ... ")

    with open(arquivo6_csv, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Número Identificador', 'Nome', 'Total de Programas de computador sem registro',
                        'Ano do Primeiro Programa de computador sem registro', 'Ano do Último Programa de computador sem registro',
                        'Total de Trabalhos técnicos', 'Ano do Primeiro Trabalho técnico', 'Ano do Último Trabalho técnico',
                        'Total de Programas de computador com registro', 'Ano do Primeiro Programa de computador com registro',
                        'Ano do Último Programa de computador com registro',
                        'Total de Programas de Patentes', 'Ano do Primeiro Programa de Patentes', 'Ano do Último Programa de Patentes'])
    
        for pasta, subpastas, arquivos in os.walk(pasta_raiz):
            for arquivo in arquivos:
                if arquivo.endswith(".zip"):
                    arquivo_zip = os.path.join(pasta, arquivo)
    
                    with zipfile.ZipFile(arquivo_zip, 'r') as zf:
                        for entry in zf.infolist():
                            if entry.filename.endswith(".xml"):
                                xml_file = zf.extract(entry, path=pasta)
                                tree = ET.parse(xml_file)
                                root = tree.getroot()
                                numero_identificador = root.attrib.get("NUMERO-IDENTIFICADOR")
                                nome_individuo = root.find('DADOS-GERAIS').attrib.get('NOME-COMPLETO', '')
                                programas_sem_registro = root.findall('.//PROGRAMA-DE-COMPUTADOR[@TIPO="Sem registro"]')
                                programas_com_registro = root.findall('.//PROGRAMA-DE-COMPUTADOR[@TIPO="Com registro"]')
                                programas_patentes = root.findall('.//REGISTRO-OU-PATENTE[@TIPO-PATENTE="PROGRAMA_DE_COMPUTADOR_PC"]')
    
                                primeiro_programa_sem_registro = min(int(p.attrib.get('ANO', '9999')) for p in programas_sem_registro) if programas_sem_registro else None
                                ultimo_programa_sem_registro = max(int(p.attrib.get('ANO', '0')) for p in programas_sem_registro) if programas_sem_registro else None
                                primeiro_programa_com_registro = min(int(p.find('DADOS-BASICOS-DO-PROGRAMA').attrib.get('ANO', '9999')) for p in programas_com_registro) if programas_com_registro else None
                                ultimo_programa_com_registro = max(int(p.find('DADOS-BASICOS-DO-PROGRAMA').attrib.get('ANO', '0')) for p in programas_com_registro) if programas_com_registro else None
                                primeiro_programa_patentes = None
                                ultimo_programa_patentes = None
    
                                if programas_patentes and any(p.attrib.get('DATA-PEDIDO-DE-DEPOSITO') for p in programas_patentes):
                                    primeiro_programa_patentes = min(int(p.attrib.get('DATA-PEDIDO-DE-DEPOSITO', '99991231')[-4:]) for p in programas_patentes if p.attrib.get('DATA-PEDIDO-DE-DEPOSITO'))
                                    ultimo_programa_patentes = max(int(p.attrib.get('DATA-PEDIDO-DE-DEPOSITO', '00000000')[-4:]) for p in programas_patentes if p.attrib.get('DATA-PEDIDO-DE-DEPOSITO'))
    
    
                                # Counting the number of trabalho-tecnico elements
                                trabalhos_tecnicos = root.findall('.//TRABALHO-TECNICO')
                                total_trabalhos_tecnicos = len(trabalhos_tecnicos)
    
                                # Extracting first and last years of trabalho-tecnico elements
                                primeiro_trabalho_tecnico = (
                                    int(trabalhos_tecnicos[0].find('DADOS-BASICOS-DO-TRABALHO-TECNICO').attrib.get('ANO')) if trabalhos_tecnicos else None
                                )
                                ultimo_trabalho_tecnico = (
                                    int(trabalhos_tecnicos[-1].find('DADOS-BASICOS-DO-TRABALHO-TECNICO').attrib.get('ANO')) if trabalhos_tecnicos else None
                                )
    
                                # Writing the row with variables
                                row_data = [numero_identificador, nome_individuo, len(programas_sem_registro),
                                            primeiro_programa_sem_registro, ultimo_programa_sem_registro,
                                            total_trabalhos_tecnicos, primeiro_trabalho_tecnico, ultimo_trabalho_tecnico,
                                            len(programas_com_registro),
                                            primeiro_programa_com_registro, ultimo_programa_com_registro,
                                            len(programas_patentes), primeiro_programa_patentes, ultimo_programa_patentes]
    
                                writer.writerow(row_data)
    
        print(f"Os dados foram convertidos e armazenados no arquivo '{arquivo6_csv}'.")
```
A função arquivo6() realiza a extração de informações relacionadas a programas de computador, trabalhos técnicos e programas de patentes. Aqui está um resumo mais conciso do que a função faz:

A função começa imprimindo uma mensagem indicando que a extração está começando para o arquivo CSV (arquivo6_csv).
##### Abertura do Arquivo CSV:

Abre o arquivo CSV em modo de escrita (mode='w').
Cria um objeto writer usando a biblioteca csv para escrever linhas no arquivo.
Escreve a primeira linha no arquivo CSV, que contém os cabeçalhos das colunas.
##### Iteração sobre os Arquivos XML:

Utiliza a biblioteca os.walk para percorrer recursivamente todas as pastas e arquivos na árvore de diretórios a partir da pasta raiz (pasta_raiz).
Para cada arquivo encontrado, verifica se possui a extensão ".zip".
##### Extração de Dados Específicos:

Para cada entrada no arquivo ZIP, verifica se é um arquivo XML (entry.filename.endswith(".xml")).
Se sim, extrai o arquivo XML para a pasta atual.
Faz o parse do arquivo XML utilizando a biblioteca xml.etree.ElementTree e obtém o elemento raiz (root).
##### Extração de Informações:

Obtém o número identificador e o nome do indivíduo diretamente do elemento raiz.
Utiliza XPath para encontrar elementos relacionados a diferentes tipos de programas de computador, trabalhos técnicos e programas de patentes.
Calcula estatísticas, como o total de cada tipo de programa e os anos do primeiro e último evento em cada categoria.
##### Escrita no Arquivo CSV:

Escreve uma linha no arquivo CSV contendo as informações extraídas.
As informações são organizadas conforme os cabeçalhos definidos anteriormente.
##### Feedback ao Usuário:

Imprime uma mensagem indicando que os dados foram convertidos e armazenados no arquivo CSV.
#### bancas doutorado & mestrado.csv
```bash
def arquivo7():
    print(f"Iniciando extração para {arquivo7_csv} ... ")
    with open(arquivo7_csv, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
    
        writer.writerow(['Número Identificador', 'Nome', 'Total de Participação em Bancas',
                        'Total de Participação em Eventos', 'Ano do Primeiro Evento', 'Ano do Último Evento'])
        for pasta, subpastas, arquivos in os.walk(pasta_raiz):
            for arquivo in arquivos:
                if arquivo.endswith(".zip"):
                    arquivo_zip = os.path.join(pasta, arquivo)
                    with zipfile.ZipFile(arquivo_zip, 'r') as zf:
                        for entry in zf.infolist():
                            if entry.filename.endswith(".xml"):
                                xml_file = zf.extract(entry, path=pasta)
                                tree = ET.parse(xml_file)
                                root = tree.getroot()
                                # Código para extrair informações dos trabalhos em eventos e bancas
                                participacao_em_bancas = root.findall('.//PARTICIPACAO-EM-BANCA-DE-APERFEICOAMENTO-ESPECIALIZACAO')
                                total_participacao_em_bancas = len(participacao_em_bancas)
                                trabalhos_em_eventos = root.findall('.//TRABALHO-EM-EVENTOS')
                                total_participacao_em_eventos = len(trabalhos_em_eventos)
                                primeiro_evento = min(int(e.find('DADOS-BASICOS-DO-TRABALHO').attrib.get('ANO-DO-TRABALHO', '9999')) for e in trabalhos_em_eventos) if trabalhos_em_eventos else None
                                ultimo_evento = max(int(e.find('DADOS-BASICOS-DO-TRABALHO').attrib.get('ANO-DO-TRABALHO', '0')) for e in trabalhos_em_eventos) if trabalhos_em_eventos else None
                                numero_identificador = root.attrib.get("NUMERO-IDENTIFICADOR")
                                nome_individuo = root.find('DADOS-GERAIS').attrib.get('NOME-COMPLETO', '')
                                # Escrever a linha de dados no CSV
                                row_data = [numero_identificador, nome_individuo, total_participacao_em_bancas,
                                            total_participacao_em_eventos, primeiro_evento, ultimo_evento]
    
                                writer.writerow(row_data)
        print(f"Os dados foram convertidos e armazenados no arquivo '{arquivo7_csv}'.")
```
A função arquivo6() realiza a extração de informações relacionadas a programas de computador, trabalhos técnicos e programas de patentes. Aqui está um resumo mais conciso do que a função faz:

A função começa imprimindo uma mensagem indicando que a extração está começando para o arquivo CSV (arquivo6_csv).
##### Abertura do Arquivo CSV:

Abre o arquivo CSV em modo de escrita (mode='w').
Cria um objeto writer usando a biblioteca csv para escrever linhas no arquivo.
Escreve a primeira linha no arquivo CSV, que contém os cabeçalhos das colunas.
##### Iteração sobre os Arquivos XML:

Utiliza a biblioteca os.walk para percorrer recursivamente todas as pastas e arquivos na árvore de diretórios a partir da pasta raiz (pasta_raiz).
Para cada arquivo encontrado, verifica se possui a extensão ".zip".
##### Extração de Dados Específicos:

Para cada entrada no arquivo ZIP, verifica se é um arquivo XML (entry.filename.endswith(".xml")).
Se sim, extrai o arquivo XML para a pasta atual.
Faz o parse do arquivo XML utilizando a biblioteca xml.etree.ElementTree e obtém o elemento raiz (root).
##### Extração de Informações:

Obtém o número identificador e o nome do indivíduo diretamente do elemento raiz.
Utiliza XPath para encontrar elementos relacionados a diferentes tipos de programas de computador, trabalhos técnicos e programas de patentes.
Calcula estatísticas, como o total de cada tipo de programa e os anos do primeiro e último evento em cada categoria.
##### Escrita no Arquivo CSV:

Escreve uma linha no arquivo CSV contendo as informações extraídas.
As informações são organizadas conforme os cabeçalhos definidos anteriormente.
##### Feedback ao Usuário:

Imprime uma mensagem indicando que os dados foram convertidos e armazenados no arquivo CSV.
#### orientações em andamento.csv
```bash
def arquivo8():
    print(f"Iniciando extração para {arquivo8_csv} ... ")
    with open(arquivo8_csv, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
    
        writer.writerow(['Número Identificador', 'Nome', 'Orientações em Andamento','Orientações concluidas'])
    
        for pasta, subpastas, arquivos in os.walk(pasta_raiz):
            for arquivo in arquivos:
                if arquivo.endswith(".zip"):
                    arquivo_zip = os.path.join(pasta, arquivo)
                    with zipfile.ZipFile(arquivo_zip, 'r') as zf:
                        for entry in zf.infolist():
                            if entry.filename.endswith(".xml"):
                                xml_file = zf.extract(entry, path=pasta)
                                tree = ET.parse(xml_file)
                                root = tree.getroot()
                                numero_identificador = root.attrib.get("NUMERO-IDENTIFICADOR")
                                nome_individuo = root.find('DADOS-GERAIS').attrib.get('NOME-COMPLETO', '')
                                # Contagem das orientações em andamento e concluídas
                                orientacoes_andamento = len(root.findall('.//ORIENTACOES-EM-ANDAMENTO/'))
                                oritenacoes_concluidas = len(root.findall('.//ORIENTACOES-CONCLUIDAS/'))
    
                                # Writing the row with variables
                                row_data = [numero_identificador, nome_individuo,
                                            orientacoes_andamento, oritenacoes_concluidas]
                                writer.writerow(row_data)
        print(f"Os dados foram convertidos e armazenados no arquivo '{arquivo8_csv}'.")
```
A função arquivo8() realiza a extração de informações relacionadas às orientações acadêmicas (em andamento e concluídas) de currículos Lattes. Aqui está um resumo mais conciso do que a função faz:

A função começa imprimindo uma mensagem indicando que a extração está começando para o arquivo CSV (arquivo8_csv).
##### Abertura do Arquivo CSV:

Abre o arquivo CSV em modo de escrita (mode='w').
Cria um objeto writer usando a biblioteca csv para escrever linhas no arquivo.
Escreve a primeira linha no arquivo CSV, que contém os cabeçalhos das colunas.
##### Iteração sobre os Arquivos XML:

Utiliza a biblioteca os.walk para percorrer recursivamente todas as pastas e arquivos na árvore de diretórios a partir da pasta raiz (pasta_raiz).
Para cada arquivo encontrado, verifica se possui a extensão ".zip".
##### Extração de Dados Específicos:

Para cada entrada no arquivo ZIP, verifica se é um arquivo XML (entry.filename.endswith(".xml")).
Se sim, extrai o arquivo XML para a pasta atual.
Faz o parse do arquivo XML utilizando a biblioteca xml.etree.ElementTree e obtém o elemento raiz (root).
##### Extração de Informações:

Utiliza XPath para encontrar elementos relacionados às orientações em andamento (ORIENTACOES-EM-ANDAMENTO) e orientações concluídas (ORIENTACOES-CONCLUIDAS).
Calcula a quantidade de orientações em andamento e concluídas.
##### Escrita no Arquivo CSV:

Escreve uma linha no arquivo CSV contendo as informações extraídas.
As informações são organizadas conforme os cabeçalhos definidos anteriormente.
##### Feedback ao Usuário:

Imprime uma mensagem indicando que os dados foram convertidos e armazenados no arquivo CSV.
### menu principal
```bash
while not saida:
    print("--------------Menu-----------------\n")
    print("1- extrair e converter dados do Arquivo-1")
    print("2- extrair e converter dados do Arquivo-2")
    print("3- extrair e converter dados do Arquivo-3")
    print("4- extrair e converter dados do Arquivo-4")
    print("5- extrair e converter dados do Arquivo-5")
    print("6- extrair e converter dados do Arquivo-6")
    print("7- extrair e converter dados do Arquivo-7")
    print("8- extrair e converter dados do Arquivo-8")
    print("9 -extrair e coverter todos os arquivos ")
    print("10- Mudar Pathing da pasta raiz")
    print("11- Sair")
    print("-----------------------------------\n")
    try:
        escolha = int(input("Digite o numero da opcao desejada: \n->"))
        if escolha not in range(1, 13):
            raise ValueError("Opção inválida")
    except ValueError as e:
        print(f"Erro: {e}")
        continue  # Volte ao início do loop
    if escolha==1:
        arquivo1()
    elif escolha ==2:
        arquivo2()
    elif escolha==3:
        arquivo3()
    elif escolha==4:
        arquivo4()
    elif escolha==5:
        arquivo5()
    elif escolha==6:
        arquivo6()
    elif escolha == 7:
        arquivo7()
    elif escolha == 8:
        arquivo8()
    elif escolha==9:
        saida = False
        while not saida:
            print("---WARNING ---\n está ação pode ser demorado e não recomendada visto que \n a base de dados é grande e não é de rapida leitura")
            print("Continuar mesmo assim ?")
            warningescolha=input("").lower()
            if warningescolha in ('nao', 'n', 'não','no'):
                continue  # Volte ao início do loop
            elif warningescolha in ('sim','s','si'):
                saida = True
            else:
                print(f"{escolha}não é uma escolha valida por favor selecione sim ou não ")
        arquivo1()
        arquivo2()
        arquivo3()
        arquivo4()
        arquivo5()
        arquivo6()
        arquivo7()
        arquivo8()
    elif escolha ==10:
        print(definir_path_pasta())

    elif escolha == 11:
        abrir_repositorio_github()
        saida = True
```
Esse trecho de código apresenta um menu interativo em um loop que permite ao usuário escolher entre várias opções relacionadas à extração e conversão de dados de diferentes arquivos. Aqui está uma explicação resumida do que cada parte faz:

#### Menu Interativo:

Um loop while (while not saida) é utilizado para manter o menu ativo até que o usuário escolha sair (escolha == 11).
Um menu é exibido na tela, listando várias opções numeradas de 1 a 11, incluindo extrair dados de arquivos específicos, extrair todos os arquivos, mudar o caminho da pasta raiz, sair, etc.
#### Obtenção da Escolha do Usuário:

O código solicita ao usuário que digite o número da opção desejada.
Há uma tentativa (try) de converter a entrada do usuário para um número inteiro (int).
Se a entrada não for um número válido, é gerada uma exceção (ValueError), e uma mensagem de erro é exibida.
#### Execução da Opção Escolhida:

Se a entrada do usuário estiver dentro do intervalo de 1 a 11 (inclusive), a escolha é avaliada para determinar qual ação executar.
Cada opção (de 1 a 11) corresponde a uma função específica (por exemplo, arquivo1(), arquivo2()).
Se o usuário escolher a opção 9, ele recebe um aviso sobre a possível demora da ação e tem a opção de continuar ou não.
#### Execução de Funções:

Dependendo da escolha do usuário, a função correspondente é executada.
Se a escolha for 9, todas as funções (arquivo1() a arquivo8()) são executadas sequencialmente.
#### Aviso e Confirmação:

Se o usuário escolher extrair todos os arquivos (opção 9), ele recebe um aviso sobre a possível demora da ação.
O usuário é solicitado a confirmar se deseja continuar.
Se a resposta for positiva (sim), o loop interno é encerrado (saida = True), e todas as funções são executadas.
#### Outras Opções:

Se o usuário escolher a opção 10, a função definir_path_pasta() é chamada para mudar o caminho da pasta raiz.
Se o usuário escolher a opção 11, a função abrir_repositorio_github() é chamada para abrir um repositório GitHub, e a variável saida é definida como True, encerrando o loop principal.
O código fornece uma interface interativa para o usuário interagir com as funções de extração e conversão de dados de arquivos XML.
# Link para os csv's
[![Pasta CSV](https://img.shields.io/badge/Pasta%20CSV-Dados%20Gerados-yellow)](https://github.com/ImArthz/Lattes_CV_Extractor/tree/main/csv's)

Este link levará  diretamente para a pasta "csv's" no repositório no GitHub.

Esse link direcionará os usuários para a pasta que contém os códigos de plotagem no repositório no GitHub.
# codigos de plotagem 
[![Pasta de Códigos](https://img.shields.io/badge/Pasta%20de%20C%C3%B3digos-Pandas%20%26%20Seaborn-orange)](https://github.com/ImArthz/Lattes_CV_Extractor/tree/main/codigos%20de%20plotagem)
## Descrição do Uso de Pandas e Seaborn para Plotagem de Gráficos
O código   utiliza a biblioteca Pandas em conjunto com elementos do Seaborn para realizar a análise e visualização dos dados extraídos dos arquivos CSV gerados. Pandas, conhecido por sua eficiência em manipulação de dados tabulares, é empregado para carregar e organizar as informações contidas nos CSVs.

Além disso, o código   aproveita as capacidades visuais do Seaborn, uma biblioteca baseada em Matplotlib, para criar gráficos informativos e esteticamente agradáveis. Essa combinação permite uma exploração mais aprofundada das tendências e padrões presentes nos dados, oferecendo uma abordagem visual para a compreensão das informações contidas nos currículos Lattes processados pelo script.
# link para pasta de gráficos 
[![Pasta de Gráficos](https://img.shields.io/badge/Gr%C3%A1ficos-Ver%20Gr%C3%A1ficos-brightgreen)](https://github.com/ImArthz/Lattes_CV_Extractor/tree/main/graficos)
Ao clicar no link ou no botão, você será redirecionado para a pasta de gráficos no repositório do GitHub.
# gráficos
![bar_anos_primeira_apresentacao.png](https://github.com/ImArthz/Lattes_CV_Extractor/blob/main/graficos/bar_anos_primeira_apresentacao.png)
![bar_anos_primeiro_artigo.png](https://github.com/ImArthz/Lattes_CV_Extractor/blob/main/graficos/bar_anos_primeiro_artigo.png)
![bar_anos_primeiro_capitulo.png](https://github.com/ImArthz/Lattes_CV_Extractor/blob/main/graficos/bar_anos_primeiro_capitulo.png)
![bar_anos_primeiro_desenvolvimento.png](https://github.com/ImArthz/Lattes_CV_Extractor/blob/main/graficos/bar_anos_primeiro_desenvolvimento.png)
![bar_anos_primeiro_evento.png](https://github.com/ImArthz/Lattes_CV_Extractor/blob/main/graficos/bar_anos_primeiro_evento.png)
![bar_anos_primeiro_extensao.png](https://github.com/ImArthz/Lattes_CV_Extractor/blob/main/graficos/bar_anos_primeiro_extensao.png)
![bar_anos_primeiro_livro.png](https://github.com/ImArthz/Lattes_CV_Extractor/blob/main/graficos/bar_anos_primeiro_livro.png)
![bar_anos_primeiro_pesquisa.png](https://github.com/ImArthz/Lattes_CV_Extractor/blob/main/graficos/bar_anos_primeiro_pesquisa.png)
![bar_anos_primeiro_resumo.png](https://github.com/ImArthz/Lattes_CV_Extractor/blob/main/graficos/bar_anos_primeiro_resumo.png)
![bar_anos_primeiro_resumo_expandido.png](https://github.com/ImArthz/Lattes_CV_Extractor/blob/main/graficos/bar_anos_primeiro_resumo_expandido.png)
![bar_anos_primeiro_tecnico.png](https://github.com/ImArthz/Lattes_CV_Extractor/blob/main/graficos/bar_anos_primeiro_tecnico.png)
![bar_anos_primeiro_trabalho.png](https://github.com/ImArthz/Lattes_CV_Extractor/blob/main/graficos/bar_anos_primeiro_trabalho.png)
![bar_anos_ultima_apresentacao.png](https://github.com/ImArthz/Lattes_CV_Extractor/blob/main/graficos/bar_anos_ultima_apresentacao.png)
![bar_anos_ultimo_artigo.png](https://github.com/ImArthz/Lattes_CV_Extractor/blob/main/graficos/bar_anos_ultimo_artigo.png)
![bar_anos_ultimo_capitulo.png](https://github.com/ImArthz/Lattes_CV_Extractor/blob/main/graficos/bar_anos_ultimo_capitulo.png)
![bar_anos_ultimo_desenvolvimento.png](https://github.com/ImArthz/Lattes_CV_Extractor/blob/main/graficos/bar_anos_ultimo_desenvolvimento.png)
![bar_anos_ultimo_evento.png](https://github.com/ImArthz/Lattes_CV_Extractor/blob/main/graficos/bar_anos_ultimo_evento.png)
![bar_anos_ultimo_extensao.png](https://github.com/ImArthz/Lattes_CV_Extractor/blob/main/graficos/bar_anos_ultimo_extensao.png)
![bar_anos_ultimo_livro.png](https://github.com/ImArthz/Lattes_CV_Extractor/blob/main/graficos/bar_anos_ultimo_livro.png)
![bar_anos_ultimo_pesquisa.png](https://github.com/ImArthz/Lattes_CV_Extractor/blob/main/graficos/bar_anos_ultimo_pesquisa.png)
![bar_anos_ultimo_resumo.png](https://github.com/ImArthz/Lattes_CV_Extractor/blob/main/graficos/bar_anos_ultimo_resumo.png)
![bar_anos_ultimo_resumo_expandido.png](https://github.com/ImArthz/Lattes_CV_Extractor/blob/main/graficos/bar_anos_ultimo_resumo_expandido.png)
![bar_anos_ultimo_tecnico.png](https://github.com/ImArthz/Lattes_CV_Extractor/blob/main/graficos/bar_anos_ultimo_tecnico.png)
![bar_anos_ultimo_trabalho.png](https://github.com/ImArthz/Lattes_CV_Extractor/blob/main/graficos/bar_anos_ultimo_trabalho.png)
![bar_apresentacao_trabalhos.png](https://github.com/ImArthz/Lattes_CV_Extractor/blob/main/graficos/bar_apresentacao_trabalhos.png)
![bar_artigos_completos.png](https://github.com/ImArthz/Lattes_CV_Extractor/blob/main/graficos/bar_artigos_completos.png)
![bar_capitulos.png](https://github.com/ImArthz/Lattes_CV_Extractor/blob/main/graficos/bar_capitulos.png)
![bar_livros.png](https://github.com/ImArthz/Lattes_CV_Extractor/blob/main/graficos/bar_livros.png)
![bar_participacao_bancas.png](https://github.com/ImArthz/Lattes_CV_Extractor/blob/main/graficos/bar_participacao_bancas.png)
![bar_participacao_eventos.png](https://github.com/ImArthz/Lattes_CV_Extractor/blob/main/graficos/bar_participacao_eventos.png)
![bar_resumo_geral.png](https://github.com/ImArthz/Lattes_CV_Extractor/blob/main/graficos/bar_resumo_geral.png)
![bar_resumos_anais.png](https://github.com/ImArthz/Lattes_CV_Extractor/blob/main/graficos/bar_resumos_anais.png)
![bar_resumos_expandidos.png](https://github.com/ImArthz/Lattes_CV_Extractor/blob/main/graficos/bar_resumos_expandidos.png)
![bar_top10_apresentacoes.png](https://github.com/ImArthz/Lattes_CV_Extractor/blob/main/graficos/bar_top10_apresentacoes.png)
![bar_top10_artigos.png](https://github.com/ImArthz/Lattes_CV_Extractor/blob/main/graficos/bar_top10_artigos.png)
![bar_top10_capitulos.png](https://github.com/ImArthz/Lattes_CV_Extractor/blob/main/graficos/bar_top10_capitulos.png)
![bar_top10_desenvolvimento.png](https://github.com/ImArthz/Lattes_CV_Extractor/blob/main/graficos/bar_top10_desenvolvimento.png)
![bar_top10_extensao.png](https://github.com/ImArthz/Lattes_CV_Extractor/blob/main/graficos/bar_top10_extensao.png)
![bar_top10_livros.png](https://github.com/ImArthz/Lattes_CV_Extractor/blob/main/graficos/bar_top10_livros.png)
![bar_top10_participacao_bancas.png](https://github.com/ImArthz/Lattes_CV_Extractor/blob/main/graficos/bar_top10_participacao_bancas.png)
![bar_top10_participacao_eventos.png](https://github.com/ImArthz/Lattes_CV_Extractor/blob/main/graficos/bar_top10_participacao_eventos.png)
![bar_top10_pesquisa.png](https://github.com/ImArthz/Lattes_CV_Extractor/blob/main/graficos/bar_top10_pesquisa.png)
![bar_top10_resumos.png](https://github.com/ImArthz/Lattes_CV_Extractor/blob/main/graficos/bar_top10_resumos.png)
![bar_top10_resumos_expandidos.png](https://github.com/ImArthz/Lattes_CV_Extractor/blob/main/graficos/bar_top10_resumos_expandidos.png)
![bar_top10_tecnicos.png](https://github.com/ImArthz/Lattes_CV_Extractor/blob/main/graficos/bar_top10_tecnicos.png)
![bar_top10_trabalhos_completos.png](https://github.com/ImArthz/Lattes_CV_Extractor/blob/main/graficos/bar_top10_trabalhos_completos.png)
![bar_total_desenvolvimento.png](https://github.com/ImArthz/Lattes_CV_Extractor/blob/main/graficos/bar_total_desenvolvimento.png)
![bar_total_extensao.png](https://github.com/ImArthz/Lattes_CV_Extractor/blob/main/graficos/bar_total_extensao.png)
![bar_total_pesquisa.png](https://github.com/ImArthz/Lattes_CV_Extractor/blob/main/graficos/bar_total_pesquisa.png)
![bar_total_tecnicos.png](https://github.com/ImArthz/Lattes_CV_Extractor/blob/main/graficos/bar_total_tecnicos.png)
![bar_trabalhos_completos.png](https://github.com/ImArthz/Lattes_CV_Extractor/blob/main/graficos/bar_trabalhos_completos.png)
![cursos_graduacao_comuns.png](https://github.com/ImArthz/Lattes_CV_Extractor/blob/main/graficos/cursos_graduacao_comuns.png)
![cursos_mestrado_comuns.png](https://github.com/ImArthz/Lattes_CV_Extractor/blob/main/graficos/cursos_mestrado_comuns.png)
![grafico_idiomas.png](https://github.com/ImArthz/Lattes_CV_Extractor/blob/main/graficos/grafico_idiomas.png)
![instituicoes_graduacao_mencionadas.png](https://github.com/ImArthz/Lattes_CV_Extractor/blob/main/graficos/instituicoes_graduacao_mencionadas.png)
![quantidade_especializacoes.png](https://github.com/ImArthz/Lattes_CV_Extractor/blob/main/graficos/quantidade_especializacoes.png)
![top_cidades_pesquisadores.png](https://github.com/ImArthz/Lattes_CV_Extractor/blob/main/graficos/top_cidades_pesquisadores.png)
![wordcloud_areas_atuacao.png](https://github.com/ImArthz/Lattes_CV_Extractor/blob/main/graficos/wordcloud_areas_atuacao.png)
![wordcloud_linhas_pesquisa.png](https://github.com/ImArthz/Lattes_CV_Extractor/blob/main/graficos/wordcloud_linhas_pesquisa.png)
# Contribuições

Se você deseja contribuir para o projeto, sinta-se à vontade para abrir uma issue ou enviar um pull request. Seu feedback e colaboração são muito bem-vindos!

# Sobre o Autor
Meu Nome é Arthur atualmente tenho 23 anos e sou estudante do CEFET-MG estudante de ENGENHARIA DA COMPUTAÇÃO para mais informações sinta-se livre para me contatar nas redes sociais :
[![Instagram](https://img.shields.io/badge/Instagram-ImArthz-purple?style=flat&logo=instagram)](https://www.instagram.com/mendonca_arth/)
[![Twitter](https://img.shields.io/badge/Twitter-ImArthz-lightblue?style=flat&logo=twitter)](https://twitter.com/Im_Arthz)
[![Discord](https://img.shields.io/badge/Discord-ImArthz%230000-green?style=flat&logo=discord)](https://discordapp.com/users/imarthz)
[![WhatsApp](https://img.shields.io/badge/WhatsApp-ImArthz-green?style=flat&logo=whatsapp)](https://api.whatsapp.com/send?phone=37988528423)

Feito com ❤️ e ☕ por Arthur [![Github](https://img.shields.io/badge/GitHub-ImArthz-blue?style=flat&logo=github)](https://github.com/ImArthz) 🚀


