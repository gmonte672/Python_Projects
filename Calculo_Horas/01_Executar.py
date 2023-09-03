import subprocess

caminho_codigo1 = r"C:\Users\guimo\OneDrive\Área de Trabalho\03_DivDay.py"
caminho_codigo2 = r"C:\Users\guimo\OneDrive\Área de Trabalho\04_CalcHours.py"
caminho_codigo3 = r"C:\Users\guimo\OneDrive\Área de Trabalho\05_FillDays.py"

def execute_codigo(caminho):
    try:
        resultado = subprocess.run(['python', caminho], capture_output=True, text=True, check=True)
        return resultado.stdout
    except subprocess.CalledProcessError as e:
        return f"Erro: {e.stderr}"

resultado_codigo1 = execute_codigo(caminho_codigo1)
resultado_codigo2 = execute_codigo(caminho_codigo2)
resultado_codigo3 = execute_codigo(caminho_codigo3)

print("Resultado da execução do código 1:")
print(resultado_codigo1)

print("\nResultado da execução do código 2:")
print(resultado_codigo2)

print("\nResultado da execução do código 3:")
print(resultado_codigo3)