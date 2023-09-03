import pandas as pd
from datetime import timedelta

# Caminho para o arquivo Excel
caminho_arquivo = "C:/Users/guimo/OneDrive/Área de Trabalho/Pasta.xlsx"

# Lê o arquivo Excel
dados_excel = pd.read_excel(caminho_arquivo)

# Cria uma nova DataFrame para armazenar os dados complementares
dados_complementares = []

# Converte a coluna DI para o tipo datetime
dados_excel['DI'] = pd.to_datetime(dados_excel['DI'], dayfirst=True)

# Itera pelas linhas da tabela
for index, row in dados_excel.iterrows():
    if index < len(dados_excel) - 1:
        date_diff = (dados_excel.loc[index + 1, 'DI'] - row['DI']).days
        if date_diff > 1:
            for i in range(1, date_diff):
                new_date = row['DI'] + timedelta(days=i)
                new_row = {'DI': new_date, 'QTD': 0, 'Total': 0, 'IntervaloHF': 0, 'X': 0, 'Y': 0}
                dados_complementares.append(new_row)

# Cria um DataFrame com os dados complementares
dados_complementares_df = pd.DataFrame(dados_complementares)

# Concatena os dados complementares à tabela original
dados_final = pd.concat([dados_excel, dados_complementares_df], ignore_index=True)

# Ordena a tabela pelas colunas DI e HI
dados_ordenados = dados_final.sort_values(by=['DI'])

# Exibe o conteúdo da tabela organizada
print(dados_ordenados)

# Caminho para o arquivo Excel onde você deseja salvar os novos dados
caminho_arquivo_salvar = r'C:\Users\guimo\OneDrive\Área de Trabalho\Pasta.xlsx'

# Salvar o novo DataFrame de volta no arquivo Excel original
dados_ordenados.to_excel(caminho_arquivo_salvar, index=False)