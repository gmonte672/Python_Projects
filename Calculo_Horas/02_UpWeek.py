import pandas as pd
from sqlalchemy import create_engine

# Configurações de conexão ao banco de dados
db_username = 'seu_usuario'
db_password = 'sua_senha'
db_host = 'localhost'
db_name = 'nome_do_banco'
table_name = 'nome_da_tabela'

# Caminho para o arquivo Excel
excel_file_path = 'caminho_para_o_arquivo.xlsx'

# Criar uma conexão com o banco de dados
db_uri = f'mysql://{db_username}:{db_password}@{db_host}/{db_name}'
engine = create_engine(db_uri)

# Ler o arquivo Excel usando o pandas
excel_data = pd.read_excel(excel_file_path)

# Carregar os dados do Excel para o banco de dados
excel_data.to_sql(table_name, engine, if_exists='replace', index=False)

print("Dados carregados com sucesso!")