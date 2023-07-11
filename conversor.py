import xml.etree.ElementTree as ET
import csv
import os
import zipfile

pasta_raiz = r'C:\Users\Arthur\Desktop\pyp\collectionn'
arquivo_csv = "dadoszip.csv"

with open(arquivo_csv, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Nome', 'Cidade de Nascimento', 'Nome em citações bibliográficas', 'Nome da instituição', 'Endereço profissional da instituição', 'Cep', 'Cidade', 'DDD', 'Telefone profissional', 'Nome do Curso de graduação', 'Nome da instituição', 'Ano de Início', 'Ano de conclusão'])

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
                            dadosgerais_elemente = root.find("./DADOS-GERAIS")
                            if dadosgerais_elemente is not None:
                                nome_completo = dadosgerais_elemente.attrib.get("NOME-COMPLETO")
                                cidade_nascimento = dadosgerais_elemente.attrib.get("CIDADE-NASCIMENTO")
                                nome_citacao = dadosgerais_elemente.attrib.get("NOME-EM-CITACOES-BIBLIOGRAFICA")
                            else:
                                nome_completo = cidade_nascimento = nome_citacao = None

                            endereco_element = root.find("./DADOS-GERAIS/ENDERECO/ENDERECO-PROFISSIONAL")
                            if endereco_element is not None:                   
                                endereco_nome = endereco_element.attrib.get("NOME-INSTITUICAO-EMPRESA")
                                endereco_logradouro = endereco_element.attrib.get("LOGRADOURO-COMPLEMENTO")
                                endereco_cidade = endereco_element.attrib.get("CIDADE")
                                endereco_cep = endereco_element.attrib.get("CEP")
                                endereco_telefone = endereco_element.attrib.get("TELEFONE")
                                endereco_telefone_ddd = endereco_element.attrib.get("DDD")
                            else:
                                endereco_nome = endereco_logradouro = endereco_cidade = endereco_cep = endereco_telefone = endereco_telefone_ddd = None

                            graduacao_element = root.find("./DADOS-GERAIS/FORMACAO-ACADEMICA-TITULACAO/GRADUACAO")
                            if graduacao_element is not None:
                                graduacao_nome_instituicao = graduacao_element.attrib.get("NOME-INSTITUICAO")
                                graduacao_nome_curso = graduacao_element.attrib.get("NOME-CURSO")
                                graduacao_ano_inicio = graduacao_element.attrib.get("ANO-DE-INICIO")
                                graduacao_ano_conclusao = graduacao_element.attrib.get("ANO-DE-CONCLUSAO")
                            else:
                                graduacao_nome_instituicao = graduacao_nome_curso = graduacao_ano_inicio = graduacao_ano_conclusao = None


                            writer.writerow([nome_completo, cidade_nascimento, nome_citacao ,endereco_nome,endereco_logradouro,endereco_cep,endereco_cidade,endereco_telefone_ddd,endereco_telefone,graduacao_nome_curso,graduacao_nome_instituicao,graduacao_ano_inicio,graduacao_ano_conclusao])

print(f"Os dados foram convertidos e armazenados no arquivo '{arquivo_csv}'.")
'''
    1

    inserir o numero indentificador que está nas primeiras linhas do xml 

        2

        inserir os dados da graduação( que ja tem ) os  de curso técnico, os dados de especialização, de mestrado e de doutorado. 
        Se tiver mais de um, pegar o primeiro registro que encontrar.

            3

            conferir os dados de citação por que talvez não esteja pegando 

                4

                verificar a codificação dos acentos(não esta tratando talvez)

                    5
                    
                    gerar um outro arquivo .csv com o identificador do currículo,
                    o nome do indivíduo, e estes campos aqui: Linhas de Pesquisa (Todas que tiver),
                    Se tem algum registro como Membro de corpo editorial na "atuação profissional" (pegar a quantidade),
                    Se tem algum registro como Revisor de periódico na "atuação profissional" (pegar a quantidade),
                    Se tem algum registro como Revisor de Projeto de Fomento na "atuação profissional" (pegar a quantidade),
                    Áreas de Atuação (Todas que tiver).

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