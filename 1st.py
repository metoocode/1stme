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
print (df.isnull().mean()* 100)"""
from sklearn.preprocessing import LabelEncoder
import pandas as pd
df = pd.read_excel("Book1.xlsx")
df_label =df.copy()
le =LabelEncoder()
df_label['Gender_Encoded'] = le.fit_transform(df_label[''])
