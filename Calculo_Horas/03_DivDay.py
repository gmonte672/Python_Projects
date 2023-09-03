import pandas as pd

# Caminho para o arquivo Excel
caminho_arquivo = r'C:\Users\guimo\OneDrive\Área de Trabalho\Pasta.xlsx'

# Carregar o arquivo Excel em um DataFrame
df = pd.read_excel(caminho_arquivo)
df = df.sort_values(by=['DI', 'HI'])

# Converter colunas de datas e horas para objetos de data e hora
df['DI'] = pd.to_datetime(df['DI'])
df['HI'] = pd.to_timedelta(df['HI'].astype(str))
df['DF'] = pd.to_datetime(df['DF'])
df['HF'] = pd.to_timedelta(df['HF'].astype(str))

# Criar uma lista de intervalos de datas e horas
intervalos = []
for index, row in df.iterrows():
    di = row['DI']
    hi = row['HI']
    df_date = row['DF']
    hf = row['HF']
    
    while di <= df_date:
        df_temp = df_date if di == df_date else di.replace(hour=23, minute=59, second=59)
        hf_temp = hf if di == df_date else df_temp.replace(hour=23, minute=59, second=59)
        intervalos.append({
            'DI': di.strftime('%d/%m/%Y'),
            'HI': str(hi).split()[-1],  # Extrair apenas o horário
            'DF': df_temp.strftime('%d/%m/%Y'),
            'HF': str(hf_temp).split()[-1]  # Extrair apenas o horário
        })
        di += pd.DateOffset(days=1)
        hi = pd.Timedelta(seconds=0)

# Criar um novo DataFrame a partir da lista de intervalos
novo_df = pd.DataFrame(intervalos, columns=['DI', 'HI', 'DF', 'HF'])

# Imprimir o novo DataFrame resultante
print(novo_df)

# Caminho para o arquivo Excel onde você deseja salvar os novos dados
caminho_arquivo_salvar = r'C:\Users\guimo\OneDrive\Área de Trabalho\Pasta.xlsx'

# Salvar o novo DataFrame de volta no arquivo Excel original
novo_df.to_excel(caminho_arquivo_salvar, index=False)
