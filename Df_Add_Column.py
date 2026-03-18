import pandas as pd

data = {'Name': ['Abe','Jelyn','Ashley'],
        'Age':[21, 22, 9]
        }

df = pd.DataFrame(data)

df['Job'] = ['Data Eng', 'Housewife', 'Student']

print(df)