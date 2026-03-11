import pandas as pd

df = pd.read_csv("quales/classificacoes_publicadas_computacao_2026.csv", sep=";")

print(df.info())

print(df.head(10))


ordem = ["A1","A2","A3","A4","B1","B2","B3","B4","C"]

count_estrato = df["Estrato"].value_counts().reindex(ordem)
print(count_estrato)