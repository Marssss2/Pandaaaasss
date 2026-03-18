import pandas as pd

df = pd.read_csv('PKMN.csv', index_col='Name')

print(df.to_string())