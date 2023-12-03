from enum import unique
import pandas as pd
import random




lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

conv = pd.DataFrame()
unique_values = data['whoAmI'].unique()
for val in unique_values:
    conv[val] = (data['whoAmI'] == val).astype(int)
conv.head()
print(data)
print(conv)