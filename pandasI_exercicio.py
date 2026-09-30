import pandas as pd 

dicionario = {"nome": ["alan", "douglas", "mario"], 
              "cargo": ["advogado", "arquiteto", "confeiteiro"],
              "salario": [7000, 5000, 3000]}

df = pd.DataFrame(dicionario)

print(df)

df.to_csv("pandas exercicio 1.csv", index=False, sep=";")