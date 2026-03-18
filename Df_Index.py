import pandas as pd

data = {'Name': ['Abe','Jelyn','Ashley'],
        'Age':[21, 22, 9]
        }

df = pd.DataFrame(data, index=['Employee 1','Employee 2','Employee 3'])

print(df)