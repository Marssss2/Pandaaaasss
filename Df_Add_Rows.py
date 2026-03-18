import pandas as pd

data = {'Name': ['Abe','Jelyn','Ashley'],
        'Age':[21, 22, 9]}
df = pd.DataFrame(data, index=['Employee 1','Employee 2','Employee 3'])

df['Job'] = ['Data Eng', 'Housewife', 'Student']

new_rows = pd.DataFrame([{'Name': 'Jasmine', 'Age': 4, 'Job': 'Pasaway'},
                         {'Name': 'Tonton', 'Age': 15, 'Job': 'Tambay'}], index=['Employee 4','Employee 5']) 
df = pd.concat([df,new_rows])

print(df)