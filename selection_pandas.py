import pandas as pd

df = pd.read_csv('PKMN.csv')

print(df[['Name', 'Legendary', 'Height']].to_string())