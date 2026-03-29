import pandas as pd
import matplotlib.pyplot as plt


df=pd.read_csv('india_gdp.csv')
print(df)
print(df.isnull().sum())
print(df.describe())

print("Average GDP:",df['GDP_Billion_USD'].mean())
print('____________________________________________')
print(df.loc[df['GDP_Billion_USD'].idxmax()])
print('____________________________________________')
print(df.loc[df['GDP_Billion_USD'].idxmin()])

plt.subplot(2,2,1)
plt.bar(df['Year'],df['GDP_Billion_USD'])
plt.title('India GDP Growth Over Time')


plt.subplot(2,2,2)
plt.bar(df['Year'],df['Growth_%'])
plt.title('Growth %')

plt.subplot(2,2,3)
plt.bar(df['Year'],df['Population_Million'])
plt.title('Population')

plt.subplot(2,2,4)
plt.bar(df['Year'],df['Inflation_%'])
plt.title('Inflation')

plt.show()


