import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv("Emp.csv")

df = data.loc[[1,4],['EmpID','Education','Income']] # label

df1 = data.iloc[[1,4],[0,2,6]] #Position

df2 = data[(data['Education'] == 'UG') & (data['Income'] >= 5000)]['Age']
df3 = df2['Age']
df3 = df2.iloc[:,[0,5,2,6]]
df4 = data['Age'][data.Education == 'UG'][data.Income >= 5000]

data.sort_values('Income',inplace = True, ascending = False)

data['Income'].groupby([data.Gender,data.Dept]).mean()
data['Age'].groupby([data.Gender,data.Dept]).mean()


pd.pivot_table(data, index = ['Dept'],values = ['Age','Income'],columns = ['Gender'],aggfunc = [np.mean])

dict1 = {'EmpID':[13,14],'Dept':['Research','Sales'],'Education':['UG','PG'],'Gender':['F','M'],'Married':['No','Yes'],
         'Age':[25,np.nan],'Income':[3500,4500]}

df11 = pd.DataFrame(dict1)
df12 = pd.concat([data,df11],ignore_index = True)

city = ['Mumbai','Pune','Chennai','Delhi']
customers = [1200, 1000, 800, 1500]
plt.bar(city, customers,width = .5)
plt.xlabel('City')
plt.ylabel('Customers')
plt.title('City wise customers')

np.random.seed(1)
a1 = np.arrange(0,50,10)
a2 = np.random.randint(low = 100,high = 200, size = 5)
a12 = a1+a2
a12