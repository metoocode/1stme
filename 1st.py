"""import pandas as pd
#s = pd.Series([1,2,3], index =["q","qw","wqd"])
#df = pd.DataFrame({"names":["amit", "rohan","harsh"], "marks":[10097,865,98765]})


#print(df)
#print(s)
dt= pd.read_excel("Book1.xlsx")
#df.describe()
dt.info()
print((dt["w"]))
len(dt)
# def fr(a):
  #  return a +1
#dt["zeros + 1"]  = dt["zeros"].apply()
    
#print(dt) 


import pandas as pd
data = {
  'Name':['pavan', 'kapil','amit','ishan','harsh'],
  'Age':[25, None, 44, 23, None],
  'salary':[50000,60000,70000,None,None]
}
df = pd.DataFrame(data)
print("original dataframe ")
print(df)
print(df.isnull().sum())
df_drop =df.dropna()
print(df_drop)
df['Age'].fillna(df['Age'].mean(),inplace= True)
df['salary'].fillna(df['salary'].mean(), inplace=True)
print(df)
print (df.isnull().mean()* 100)
from sklearn.preprocessing import LabelEncoder
import pandas as pd
df = pd.read_excel("Book1.xlsx")
df_label =df.copy()
le =LabelEncoder()
df_label['Gender_Encoded'] = le.fit_transform(df_label[''])
print("hi")
print(df_label,"hello")
import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

print(numbers)
print(type(numbers))

import numpy as np
import numpy as np

marks = np.array([78, 85, 91, 67, 88])

print(marks)
print(marks[0])
print(marks[2])
print(marks + 5)


matrix = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(matrix)
print(matrix.shape)
print(matrix[0, 0])
print(matrix[1, 2])
print(matrix[:, 1])
marks = np.array([70, 80, 90, 60, 100])


print(np.sum(marks))
print(np.mean(marks))
print(np.max(marks))
print(np.min(marks))
import numpy as np
data = np.array([10, 20, 30, 40, 50, 60, 70, 80,100,120,234,567,343,5453,35,34,54,167])
a =len(data)
print(a)
c,d=0
while c*d == a:

  i=+1

matrix = data.reshape()

print(matrix)
print(matrix.shape)"""
import numpy as np

data = np.array([
    10, 20, 30, 40, 50, 60, 70, 80,
    100, 120, 234, 567, 343, 5453, 35, 34,23,33
])

a = len(data)

best_rows = 1
best_cols = a

for i in range(1, int(np.sqrt(a)) + 1):
    if a % i == 0:
        best_rows = i
        best_cols = a // i

matrix = data.reshape(best_rows, best_cols)

print("Number of elements:", a)
print("Shape:", matrix.shape)
print(matrix)