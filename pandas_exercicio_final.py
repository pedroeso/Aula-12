import pandas as pd

df = pd.read_csv(r"C:\Users\pedro.rrocha\Downloads\funcionarios.csv")

print(df) 

df_funcionarios_ativos = df[df["ativo"] == True]

df_funcionarios_ativos.to_csv("funcionarios ativos.csv", index=False, sep=";")

df_funcionarios_lucro_maior_5000 = df[df["lucro"] > 5000]

df_funcionarios_lucro_maior_5000.to_csv("funcionarios com lucro maior que 5000.csv", index=False, sep=";")

df_funcionarios_inativo = df[df["ativo"] == False]

df_funcionarios_inativo.to_csv("funcionarios inativo.csv", index=False, sep=";")