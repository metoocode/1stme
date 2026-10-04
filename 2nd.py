"""import numpy as np
import pandas as pd
labels= ['a','b','c']
my_list = [10,20,30]
arr = np.array(my_list)
d = {1:10,2:20,3:30}

print(pd.Series(my_list, index=labels))
print(arr)
print(d)
import numpy as np
import pandas as pd
data = {
  'name': ['Alice', 'Bob', 'Charlie', 'David'],
  'age': [25, 30, 35, 40],
  'city': ['New York', 'Los Angeles', 'Chicago', 'Houston'],
  'salary': [50000, 60000, 70000, 80000]

}
columns = ['name', 'age', 'city', 'salary']

df = pd.DataFrame(data, columns=columns)
print(df['name'])
print(df[0:2])
df ["kk"] = ["dog","cat","rat","bat"]
print(df)
df.drop(columns=['kk'], inplace=True)
print(df)
print(df.loc[1:2])

import numpy as np
import pandas as pd
data = {
  'A':[1,2,np.nan,4,5],
  'B':[10,20,30,np.nan,50],
  'C':[100,200,300,400,np.nan],
  'D':[1000,2000,3000,4000,5000]
}

df = pd.DataFrame(data)
print(df)
print(df.isna().sum())
df.fillna(0, inplace=True)
print(df)
df.dropna(inplace=True)
print(df)

import numpy as np
import pandas as pd
employee_data = {
  'Employee ID': [101, 102, 103, 104, 105],
  'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],  
  'Department': ['HR', 'Finance', 'IT', 'Marketing', 'Sales']
  
}
salaries = {
  'Employee ID': [101, 102, 103, 104, 105], 
  'Salary': [50000, 60000, 70000, 80000, 90000],
  'bonus': [5000, 6000, 7000, 8000, 9000]
}
sa =pd.DataFrame(salaries)
em=pd.DataFrame(employee_data)
print(em)
print(sa)
merged_df = pd.merge(em, sa, on='Employee ID', how='inner')
print(merged_df)
"""
import numpy as np
import pandas as pd
from sklearn import tests
from sympy import false, true
"""
data = {
  'category': ['A', 'B', 'A', 'C', 'B', 'A'],
  'store': [10, 20, 30, 40, 50,60],
  'sales': [100, 200, 300, 400, 500,600],
  'quantity': [1, 2, 3, 4, 5,6],
  'date': pd.date_range('2023-01-01', periods=6, freq='2D')
}
am =pd.DataFrame(data)
v=am.groupby('category').agg({'sales':'sum','quantity':'mean'})
print(am)
print(v) 
m= pd.pivot_table(am, values='sales', index='category', columns='store', aggfunc='sum', fill_value=0)
print(m)
df=pd.DataFrame({
    'A':[1,2,3,4,5],
    'B':[10,20,30,40,50],
    'c':[100,200,300,400,500]
})
p=df.shape
q=df.size
w=df.columns
def square(x):
    return x**2
df['B'] = df['B'].apply(square)


h=df.describe()
print(h)
print(df)
print(q)
print(w)
print(p)
import pandas as pd
import numpy as np  
df = pd.read_csv('anime.csv')
#print(df)
#a=df.loc[2]
#print(a)
def extract_epidoes(txt):
  check= False 
  data =""
  for i in txt:
    if i == ')':
      check = False
      break
    if   i == '(':
      check = True
    if check == True:
      data += i
  return data
df['Episodes'] = df['Episodes'].str.replace("eps","")
df["Episodes"]=df["Title"].apply(extract_epidoes)
print(df)
"""
#import matplotlib.pyplot as plt

#marks = [45, 16, 7, 80, 9]
#test = [1, 2, 3, 4, 5]

#plt.plot(test ,marks)

#plt.show()
#import matplotlib.pyplot as plt

#days = [1, 2, 3, 4, 5, 6, 7]
#hours = [3, 5, 4, 6, 7, 5, 8]

#plt.plot(days, hours,marker="o")

#plt.title("My Weekly Study")
#plt.xlabel("Day")
#plt.ylabel("Study Hours")

#
# plt.show()
"""
import matplotlib.pyplot as plt

languages = ["Python", "C++", "Java", "JavaScript"]
hours = [20, 15, 8, 12]

plt.bar(languages, hours)

plt.title("Programming Learning Hours")
plt.xlabel("Language")
plt.ylabel("Hours")

plt.show()
import matplotlib.pyplot as plt

subjects = ["Physics", "Chemistry", "Maths"]
marks = [75, 82, 68]

plt.barh(subjects, marks)

plt.title("Subject-wise Marks")
plt.xlabel("Marks")
plt.ylabel("Subjects")

plt.show()
import matplotlib.pyplot as plt

hours = [1, 2, 3, 4, 5, 6]
marks = [35, 42, 50, 61, 70, 78]

plt.scatter(hours, marks)
#plt.plot()       # line/trend
#plt.bar()        # category comparison
#plt.barh()       # horizontal comparison
#plt.scatter()    # relationship between variables
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")

plt.show()

import matplotlib.pyplot as plt

marks = [45, 52, 55, 61, 63, 65, 67, 68, 70, 72,
         74, 75, 77, 80, 82, 84, 86, 89, 92, 95]

plt.hist(marks,bins=5)

plt.title("Distribution of Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")

plt.show()
import matplotlib.pyplot as plt
days = [1, 2, 3, 4, 5]
hours = [3, 5, 4, 7, 6]
plt.plot(
    days,
    hours,
    marker="o",
    linewidth=2,
    markersize=7,
    alpha=0.3
)
plt.title("Study Hours")
plt.xlabel("Day")
plt.ylabel("Hours")
plt.show()"""
import matplotlib.pyplot as plt

tests = [1, 2, 3, 4, 5]

physics = [60, 65, 72, 78, 85]
maths = [45, 55, 62, 70, 80]

plt.plot(tests, physics, marker="o", label="Physics")
plt.plot(tests, maths, marker="o", label="Maths")

plt.title("Physics vs Maths")
plt.xlabel("Test Number")
plt.ylabel("Marks")

plt.legend()

plt.show()