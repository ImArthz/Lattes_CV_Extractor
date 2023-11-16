import xml.etree.ElementTree as ET  # Importa a biblioteca ElementTree para trabalhar com XML
import csv  # Importa a biblioteca csv para manipular arquivos CSV
import os  # Importa a biblioteca os para operações de sistema
import zipfile  # Importa a biblioteca zipfile para trabalhar com arquivos ZIP
import webbrowser # Importa a biblioteca para abrir navegadores web
import pathlib #importa biblioteca para lidar com path de arquivos


pasta_raiz = r'C:\Users\aluno\Desktop\base de dados Não excluir\Conversor\Base de Testes'  # Define a pasta raiz onde os arquivos serão pesquisados
linkpadrao = None
arquivo_csv = "dadoszip.csv"  # Define o nome do arquivo CSV que será criado
arquivo2_csv = "informacoes.csv"  # Define o nome do segundo arquivo CSV que será criado
arquivo3_csv = "idiomas.csv"  # Define o nome do terceiro arquivo CSV que será criado
arquivo4_csv = "projetos.csv" #Define o nome do quarto arquivo CSV que será criado
arquivo5_csv = "publicacoes.csv"  # Define o nome do quinto arquivo CSV que será criado
arquivo6_csv ="produção tecnica.csv" #Define o nome do sexto arquivo csv que será criado 
arquivo7_csv = "bancas doutorado & mestrado.csv"#Define o nome do setimo arquivo csv que será criado
arquivo8_csv ="orientações em andamento.csv"#Define o nome do oitavo arquivo csv que será criado



print(f"Iniciando o programa ...")
def abrir_repositorio_github():
    url = "https://github.com/ImArthz/Lattes_CV_Extractor"
    webbrowser.open(url)
    print(f"Repositório do GitHub aberto: {url}")
def definir_path_pasta():
    saida = False
    pasta_raiz = None

    while not saida:
        print("Modelo de pathing:\n")
        link = input("Cole o pathing da base de dados aqui:\n")
        escolha = input(f"Você digitou {link}. Está correto? (S/N)").lower()

        if escolha in ('nao', 'n', 'não', 'no'):
            continue  # Volte ao início do loop
        elif escolha in ('sim', 's', 'si'):
            if os.path.exists(link) and os.path.isdir(link):
                pasta_raiz = link
                saida = True
            else:
                print(f"O caminho '{link}' não é um diretório válido.")
        else:
            print(f"{escolha} não é uma escolha válida. Por favor, selecione sim ou não.")

    return pasta_raiz
    
    
def obter_ano(elemento):
    if elemento is not None:
        ano_elemento = elemento.attrib.get('ANO-DO-ARTIGO') or elemento.attrib.get('ANO') or elemento.attrib.get('ANO-DA-APRESENTACAO')
        if ano_elemento is not None:
            return ano_elemento.strip()
    return ""

def obter_ano_do_artigo(elemento):
    if elemento is not None:
        ano_artigo = elemento.find('DADOS-BASICOS-DO-ARTIGO').attrib.get('ANO-DO-ARTIGO')
        if ano_artigo is not None:
            return ano_artigo.strip()
    return ""

def obter_ano_da_apresentacao(elemento):
    if elemento is not None:
        ano_apresentacao = elemento.attrib.get('ANO-DA-APRESENTACAO')
        if ano_apresentacao is not None:
            return ano_apresentacao.strip()
    return ""

# Função auxiliar para obter o valor de um atributo de um elemento XML
def get_attrib_value(element, attribute):
    return element.attrib.get(attribute) if element is not None else None

# Função auxiliar para obter o primeiro elemento correspondente a um caminho XPath em um elemento raiz XML
def get_first_element(root, xpath):
    elements = root.findall(xpath)
    return elements[0] if elements else None

# Função auxiliar para obter o texto de um elemento XML
def get_element_text(element):
    return element.text if element is not None else None
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
def arquivo3():

    print(f"Iniciando extração para {arquivo3_csv} ... ")
    # Abre o arquivo CSV 'arquivo3_csv' em modo de escrita e cria um objeto writer para escrever linhas no arquivo
    with open(arquivo3_csv, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Número Identificador', 'Nome', 'Idioma', 'Proficiência de Compreensão', 'Proficiência de Fala', 'Proficiência de Leitura', 'Proficiência de Escrita'])
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
                                numero_identificador = root.attrib.get("NUMERO-IDENTIFICADOR")  # Obtém o número identificador do elemento raiz
                                nome_individuo = root.find('DADOS-GERAIS').attrib['NOME-COMPLETO']  # Obtém o nome do indivíduo
    
                                idiomas = root.findall("./DADOS-GERAIS/IDIOMAS/IDIOMA")  # Obtém os idiomas
    
                                idiomas_lista = []
                                for idioma in idiomas:
                                    # Obtém informações sobre cada idioma, como nome do idioma, proficiência de compreensão, proficiência de fala, proficiência de leitura e proficiência de escrita
                                    nome_idioma = get_attrib_value(idioma, 'DESCRICAO-DO-IDIOMA')
                                    proficiencia_compreensao = get_attrib_value(idioma, 'PROFICIENCIA-DE-COMPREENSAO')
                                    proficiencia_fala = get_attrib_value(idioma, 'PROFICIENCIA-DE-FALA')
                                    proficiencia_leitura = get_attrib_value(idioma, 'PROFICIENCIA-DE-LEITURA')
                                    proficiencia_escrita = get_attrib_value(idioma, 'PROFICIENCIA-DE-ESCRITA')
    
                                    idiomas_lista.append([nome_idioma, proficiencia_compreensao, proficiencia_fala, proficiencia_leitura, proficiencia_escrita])
    
                                # Escreve uma linha com as informações sobre idiomas no arquivo CSV
                                writer.writerow([numero_identificador, nome_individuo] + sum(idiomas_lista, []))
    
        print(f"Os dados foram convertidos e armazenados no arquivo '{arquivo3_csv}'.")
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
saida = False

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
        print(definir_path_pasta())10

    elif escolha == 11:
        abrir_repositorio_github()
        saida = True



'''   1 ( feito )
    inserir o numero indentificador que está nas primeiras linhas do xml 

        2
    writer.writerow(['Identificador', 'Nome', 'Idiomas', 'Proficiência de Compreensão', 'Proficiência de Fala', 'Proficiência de Leitura', 'Proficiência de Escrita'])

        inserir os dados da graduação( que ja tem ) os  de curso técnico, os dados de especialização,
        de mestrado e de doutorado. 
        Se tiver mais de um, pegar o primeiro registro que encontrar.(feito porem checar os de curso tecnico por que a grande maioria aparentemente não tem)

            3

            conferir os dados de citação por que talvez não esteja pegando (feito estava puxando o nome da tag errado )

                4

                verificar a codificação dos acentos(não esta tratando talvez) [pelo oq verifiquei ta normal]

                    5
                    
                    gerar um outro arquivo .csv com o identificador do currículo,
                    o nome do indivíduo, e estes campos aqui: Linhas de Pesquisa (Todas que tiver),
                    Se tem algum registro como Membro de corpo editorial na "atuação profissional" (pegar a quantidade),
                    Se tem algum registro como Revisor de periódico na "atuação profissional" (pegar a quantidade),
                    Se tem algum registro como Revisor de Projeto de Fomento na "atuação profissional" (pegar a quantidade),
                    Áreas de Atuação (Todas que tiver). 
                    [ so tem q verificar q acho q nao ta pegando a quantidade ta dando 0,0,0 mas os outros estão ok ( pode ser algum erro de digitação da tag)]


                        6 (feito)

                        Gerar outro arquivo .csv com identificador do currículo, o nome do indivíduo, e estes campos: Idiomas:
                        Pegar para cada idioma do sujeito qual é a proficiência em 1) Compreende, 2) Fala, 3) Lê, e 4) Escreve

                            7 ( feito porem nao consegui achar o projeto de extensão e desenvolvimento)

                            Gerar outro arquivo .csv com identificador do currículo, o nome do indivíduo, e estes campos:
                            Total de Projetos de Pesquisa (ano de conclusão do primeiro e último projeto),
                            Total de Projetos de Extensão (ano de conclusão do primeiro e último projeto),
                            Total de Projetos de Desenvolvimento (ano de conclusão do primeiro e último projeto).

                                8 ( feito mas muitos nao ta pegando e os anos tbm nao estao sendo pegos)

                                Gerar outro arquivo .csv com identificador do currículo, o nome do indivíduo, e estes campos:
                                Quantidade de artigos completos publicados em periódicos, ano do primeiro e do último,
                                Quantidade de livros publicados/organizados, ano do primeiro e do último,
                                Quantidade de capítulos de livros publicados, ano do primeiro e do último,
                                Quantidade de trabalhos completos publicados em anais de congressos, ano do primeiro e do último,
                                Quantidade de Resumos expandidos publicados em am anais de congressos, ano do primeiro e do último,
                                Quantidade de Resumos expandidos publicados em am anais de congressos, ano do primeiro e do último, Quantidade de Resumos publicados em am anais de congressos, ano do primeiro e do último,
                                Quantidade de Apresentação de trabalhos, ano do primeiro e do último

                                    9

                                    Gerar outro arquivo .csv com identificador do currículo, o nome do indivíduo, e estes campos:
                                    Total de Programas de computador sem registro (ano do primeiro e último),
                                    Total de Trabalhos técnicos (ano do primeiro e último),
                                    Total de Programas de computador com registro (ano do primeiro e último),
                                    Total de Programas de Patentes (ano do primeiro e último

                                        10

                                        Gerar outro arquivo .csv com identificador do currículo, o nome do indivíduo, e estes campos:
                                        Total de Participação em Bancas (Graduação, especialização,
                                        Qualificação de Mestrado, Mestrado,
                                        Qualificação de doutorado, doutorado.),
                                        quantidade de participação em Eventos (ano do primeiro e último). 

                                            11

                                            Gerar outro arquivo .csv com identificador do currículo, o nome do indivíduo, e estes campos:
                                            Quantidade de orientações em andamento
                                            (iniciação científica, Graduação, especialização,
                                            mestrado, doutorado, outra natureza) (Em andamento e concluídas).

link github: https://github.com/ImArthz/Lattes_CV_Extractor
'''
