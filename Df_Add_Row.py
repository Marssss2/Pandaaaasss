import pandas as pd

data = {'Name': ['Abe','Jelyn','Ashley'],
        'Age':[21, 22, 9]
        }

df = pd.DataFrame(data, index=['Employee 1','Employee 2','Employee 3'])

df['Job'] = ['Data Eng', 'Housewife', 'Student']


new_row = pd.DataFrame([{'Name': 'Jasmine', 'Age': 4, 'Job': 'Pasaway'}], index=['Employee 4']) 
df = pd.concat([df,new_row])

print(df)