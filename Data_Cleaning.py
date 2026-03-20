import pandas as pd

df = pd.read_csv('PKMN.csv')

#df = df.drop(columns=['Legendary', 'No'])

#Handdle missing data

#df = df.dropna(subset=['Type2'])
#df = df.fillna({'Type2': 'None'})

#3.Fix inconsistent data
 
#df['Type1'] = df['Type1'].replace({'Grass': 'GRASS'})
#4Standarize Text

#df['Name'] = df['Name'].str.upper()
#df['Name'] = df['Name'].str.lower()

#Fix Data Types

#df['Legendary'] = df['Legendary'].astype(bool)

#6 Remove Duplicate values

#df = df.drop_duplicates()
print(df.to_string())