import pandas as pd

# 1. Carregando os dados
caminho = r"C:\Users\Administrador\Documents\Python 2026\Pandas\athlete_events.csv"
tabela = pd.read_csv(caminho)

print("--- 4 Primeiras linhas do dataset original ---")
print(tabela.head(4))

print("\n--- Formato da tabela original (Linhas, Colunas) ---")
print(tabela.shape)

# 2. Exemplo: Removendo todas as linhas com valores nulos
tabela_sem_nulos = tabela.dropna()
print("\n--- Formato após remover todas as linhas com nulos ---")
print(tabela_sem_nulos.shape)

# 3. Verificando a quantidade de dados nulos por coluna
print("\n--- Quantidade de dados nulos por coluna ---")
dados_nulos_soma = tabela.isnull().sum()
print(dados_nulos_soma)

# 4. Tratando dados nulos nas colunas específicas
tabela["Medal"] = tabela["Medal"].fillna("Zero")

media_altura = tabela["Height"].mean()
tabela["Height"] = tabela["Height"].fillna(media_altura)

# 5. Conferencia final
print("\n--- Verificação de nulos após o tratamento ---")
print(tabela.isnull().sum())

print("\n--- Primeiras linhas da tabela tratada ---")
print(tabela.head())