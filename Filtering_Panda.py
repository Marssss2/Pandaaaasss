import pandas as pd

df = pd.read_csv('PKMN.csv')

#tall_pokemon = df[df['Height'] >= 2]

#heavy_pokemon = df[df['Weight'] > 100]

#Legendary = df[df['Legendary'] == 1]

#water_pokemon = df[(df['Type1'] == 'Water') |
 #                  (df['Type2'] == 'Water')]

FF_pokemon = df[(df['Type1'] == 'Fire') | (df['Type2'] == 'Flying')]

print(FF_pokemon)