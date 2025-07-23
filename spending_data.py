import pandas as pd
import matplotlib.pyplot as plt

#load data
#df = pd.read_csv('spending_data.csv')
df = pd.read_csv('/Users/ayoosh/Desktop/python/spending_data.csv')
#preview data
df.head()
df.info()

#calculate totalspending
total = df['Amount'].sum() 
print(f"Total Spending: {total} EGP")

#Analyze Spending by category:
df.columns = df.columns.str.strip()

by_category = df.groupby('Category')['Amount'].sum() 
print(by_category) 

#visulization pie chart
by_category.plot.pie(autopct='%1.1f%%', figsize=(6,6))
plt.title('Spending By Category')
plt.ylabel('')
plt.show()