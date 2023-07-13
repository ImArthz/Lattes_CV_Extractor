import xml.etree.ElementTree as ET  # Importa a biblioteca ElementTree para trabalhar com XML
import csv  # Importa a biblioteca csv para manipular arquivos CSV
import os  # Importa a biblioteca os para operações de sistema
import zipfile  # Importa a biblioteca zipfile para trabalhar com arquivos ZIP

pasta_raiz = r'C:\Users\Arthur\Desktop\pyp\collectionn'  # Define a pasta raiz onde os arquivos serão pesquisados
arquivo_csv = "dadoszip.csv"  # Define o nome do arquivo CSV que será criado
arquivo2_csv = "informacoes.csv"  # Define o nome do segundo arquivo CSV que será criado
arquivo3_csv = "idiomas.csv"  # Define o nome do terceiro arquivo CSV que será criado

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

# Abre o arquivo CSV 'arquivo_csv' em modo de escrita e cria um objeto writer para escrever linhas no arquivo
with open(arquivo_csv, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Numero Identificador', 'Nome', 'Cidade de Nascimento', 'Nome em citações bibliográficas', 'Nome da instituição',
                    'Endereço profissional da instituição', 'Cep', 'Cidade', 'DDD', 'Telefone profissional', 'Nome do Curso de graduação', 'Nome da instituição',
                    'Ano de Início', 'Ano de conclusão', 'Mestrado Nome da instituiçao', 'mestrado nome do curso', 'mestrado ano inicio',
                    'mestrado ano conclusão', 'mestrado titulo da tese', 'doutorado nome da intituição', 'doutorado nome do curso',
                    'doutado ano de inicio', 'doutorado ano de conlusao', 'doutorado titulo da tese', 'formação complementar Nome do curso',
                    'formação complementar intituiçao', 'formação complementar ano inicio', 'formação complementar ano de conclusão'])

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

                            formacao_complementar_element = get_first_element(root, "./DADOS-COMPLEMENTARES/FORMACAO-COMPLEMENTAR/FORMACAO-COMPLEMENTAR-DE-EXTENSAO-UNIVERSITARIA")  # Obtém o elemento FORMACAO-COMPLEMENTAR-DE-EXTENSAO-UNIVERSITARIA do XML
                            if formacao_complementar_element is not None:
                                # Obtém informações da formação complementar, como nome do curso, nome da instituição, ano de início e ano de conclusão
                                formacaocompl_nome_curso = get_attrib_value(formacao_complementar_element, "NOME-CURSO")
                                formacaocompl_nome_instituicao = get_attrib_value(formacao_complementar_element, "NOME-INSTITUICAO")
                                formacaocompl_ano_inicio = get_attrib_value(formacao_complementar_element, "ANO-DE-INICIO")
                                formacaocompl_ano_conclusao = get_attrib_value(formacao_complementar_element, "ANO-DE-CONCLUSAO")
                            else:
                                formacaocompl_nome_curso = formacaocompl_nome_instituicao = formacaocompl_ano_inicio = formacaocompl_ano_conclusao = None

                            areas_de_atuacao = [area.get("NOME-DA-SUB-AREA-DO-CONHECIMENTO") for area in root.findall(".//AREA-DE-ATUACAO")]  # Obtém as áreas de atuação

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
                                            formacaocompl_ano_conclusao])

    print(f"Os dados foram convertidos e armazenados no arquivo '{arquivo_csv}'.")

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

                            # Conta a quantidade de membros de corpo editorial, revisores de periódico e revisores de projeto de fomento
                            quantidade_corpo_editorial = len(root.findall('.//ATUACAO-PROFISSIONAL[@ENQUADRAMENTO-FUNCIONAL="MEMBRO-DE-CORPO-EDITORIAL"]'))
                            quantidade_revisor_periodico = len(root.findall('.//ATUACAO-PROFISSIONAL[@ENQUADRAMENTO-FUNCIONAL="REVISOR-DE-PERIODICO"]'))
                            quantidade_revisor_projeto = len(root.findall('.//ATUACAO-PROFISSIONAL[@ENQUADRAMENTO-FUNCIONAL="REVISOR-DE-PROJETO-DE-FOMENTO"]'))

                            writer.writerow([numero_identificador, nome_individuo, ', '.join(linhas_de_pesquisa),
                                            quantidade_corpo_editorial, quantidade_revisor_periodico,
                                            quantidade_revisor_projeto, ', '.join(areas_de_atuacao)])

    print(f"Os dados foram convertidos e armazenados no arquivo '{arquivo2_csv}'.")

# Abre o arquivo CSV 'arquivo3_csv' em modo de escrita e cria um objeto writer para escrever linhas no arquivo
with open(arquivo3_csv, 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Identificador', 'Nome', 'Linhas de Pesquisa', 'Membros de Corpo Editorial', 'Revisores de Periódico', 'Revisores de Projeto de Fomento', 'Áreas de Atuação'])

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


                        6

                        Gerar outro arquivo .csv com identificador do currículo, o nome do indivíduo, e estes campos: Idiomas:
                        Pegar para cada idioma do sujeito qual é a proficiência em 1) Compreende, 2) Fala, 3) Lê, e 4) Escreve

                            7

                            Gerar outro arquivo .csv com identificador do currículo, o nome do indivíduo, e estes campos:
                            Total de Projetos de Pesquisa (ano de conclusão do primeiro e último projeto),
                            Total de Projetos de Extensão (ano de conclusão do primeiro e último projeto),
                            Total de Projetos de Desenvolvimento (ano de conclusão do primeiro e último projeto).

                                8

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