import pandas as pd

df = pd.read_csv('PKMN.csv')

PR_pokemon = df[(df['Type1'] == 'Rock') | (df['Type2'] == 'Poison'
                )]
print(df.to_string())