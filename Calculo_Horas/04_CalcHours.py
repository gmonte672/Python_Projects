import pandas as pd

# Caminho do arquivo Excel
caminho_arquivo_excel = "C:/Users/guimo/OneDrive/Área de Trabalho/Pasta.xlsx"

# Leitura do arquivo Excel
df = pd.read_excel(caminho_arquivo_excel)
df = df.sort_values(by=['DI', 'HI'])
# Converter as colunas de data e hora para o tipo correto
df['DI'] = pd.to_datetime(df['DI'], format='%d/%m/%Y') + pd.to_timedelta(df['HI'].astype(str))
df['DF'] = pd.to_datetime(df['DF'], format='%d/%m/%Y') + pd.to_timedelta(df['HF'].astype(str))

# Calcular a diferença entre os horários e armazenar na coluna 'IntervaloHF'
df['IntervaloHF'] = df['DF'] - df['DI']

# Função para formatar os intervalos de HF
def formatar_intervalos_hf(intervalos):
    intervalos_formatados = []
    intervalo_atual = intervalos[0]

    for i in range(1, len(intervalos)):
        if intervalos[i][0] > intervalo_atual[1]:
            intervalos_formatados.append(intervalo_atual)
            intervalo_atual = intervalos[i]
        else:
            intervalo_atual = (intervalo_atual[0], max(intervalo_atual[1], intervalos[i][1]))

    intervalos_formatados.append(intervalo_atual)

    return intervalos_formatados

# Calcular a quantidade de incidentes, soma das horas e intervalo de HF por dia
df_resultado = pd.DataFrame(columns=['DI', 'QTD', 'Total', 'IntervaloHF', 'X', 'Y'])

for dia in df['DI'].dt.date.unique():
    data_filtrada = df[df['DI'].dt.date == dia]
    qtd_incidentes = len(data_filtrada)
    total_horas = data_filtrada['DF'].max() - data_filtrada['DI'].min()

    intervalos_hf = [(row['DI'], row['DF']) for _, row in data_filtrada.iterrows()]
    intervalos_hf_formatados = formatar_intervalos_hf(intervalos_hf)
    intervalo_hf_formatado = ' & '.join([f"[{intervalo[0].time()}, {intervalo[1].time()}]" for intervalo in intervalos_hf_formatados])

    x_values = [(intervalo[1] - intervalo[0]) for intervalo in intervalos_hf_formatados]
    x_formatted = ' & '.join([f"[{intervalo.seconds // 3600}:{(intervalo.seconds % 3600) // 60:02d}]" for intervalo in x_values])

    total_formatado = '{:02d}:{:02d}:{:02d}'.format(total_horas.seconds // 3600, (total_horas.seconds % 3600) // 60, total_horas.seconds % 60)
    
    y_total_seconds = sum([intervalo.seconds for intervalo in x_values])
    y_hours = y_total_seconds // 3600
    y_minutes = (y_total_seconds % 3600) // 60
    y_formatted = '{:02d}:{:02d}'.format(y_hours, y_minutes)

    df_dia = pd.DataFrame({'DI': [dia], 'QTD': [qtd_incidentes], 'Total': [total_formatado], 'IntervaloHF': [intervalo_hf_formatado], 'X': [x_formatted], 'Y': [y_formatted]})
    df_resultado = pd.concat([df_resultado, df_dia], ignore_index=True)

# Salvar o DataFrame resultante em um arquivo Excel na pasta 2
caminho_arquivo_saida = "C:/Users/guimo/OneDrive/Área de Trabalho/Pasta2.xlsx"
df_resultado.to_excel(caminho_arquivo_saida, index=False)

# Exibir a tabela no prompt
print("Tabela de Quantidade de Incidentes, Soma das Horas e Intervalo de HF por Dia:")
print()
pd.set_option('display.max_colwidth', None)
print(df_resultado)

# Caminho para o arquivo Excel onde você deseja salvar os novos dados
caminho_arquivo_salvar = r'C:\Users\guimo\OneDrive\Área de Trabalho\Pasta.xlsx'

# Salvar o novo DataFrame de volta no arquivo Excel original
df_resultado.to_excel(caminho_arquivo_salvar, index=False)