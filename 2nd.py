"""import numpy as np
import pandas as pd
labels= ['a','b','c']
my_list = [10,20,30]
arr = np.array(my_list)
d = {1:10,2:20,3:30}

print(pd.Series(my_list, index=labels))
print(arr)
print(d)"""
import numpy as np
import pandas as pd
data = {
  'name': ['Alice', 'Bob', 'Charlie', 'David'],
  'age': [25, 30, 35, 40],
  'city': ['New York', 'Los Angeles', 'Chicago', 'Houston'],
  'salary': [50000, 60000, 70000, 80000]

}
print(pd.DataFrame(data))