import pandas as pd

df = pd.read_csv(r"C:\Users\pedro.rrocha\Downloads\funcionarios.csv")

print(df) 

df_funcionarios_com_lucro = df[(df["lucro"] != 0) & (df["ativo"] == True)]

print(df_funcionarios_com_lucro)