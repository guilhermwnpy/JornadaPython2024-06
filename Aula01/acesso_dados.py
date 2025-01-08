import pandas as pd

tabela = pd.read_csv("Aula01/produtos.csv")

# print(tabela)

codigo = tabela["codigo"]
marca = tabela["marca"]
tipo = tabela["tipo"]
categoria = tabela["categoria"]
preco = tabela["preco_unitario"]
custo = tabela["custo"]
obs = tabela["obs"]

for linha in tabela.index:
    tabela.loc[linha, "codigo"]