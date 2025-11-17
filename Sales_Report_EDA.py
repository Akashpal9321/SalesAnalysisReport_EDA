import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv("Sale Report.csv")
print(df.head)
print(df.info)
print(df.describe)
print(df.columns)


#Delete every NaN from whole dataFrame
df=df.dropna()


#Delete NaN for specific columns
#df=df.dropna(subset=['Stock','Category'])

print(df.isnull().sum())

print(df.columns)

print(df['Stock'])


#Steps how find trends golden

color_trend = df.groupby('Color')['Stock'].sum()

color_trend.plot(kind='bar', figsize=(10,5))
plt.title("Total Stock by Color")
plt.xlabel("Color")
plt.ylabel("Demanding color")
plt.savefig('Demanding color', dpi=300)
plt.show()


#Size

size_trend=df.groupby('Size')['Stock'].sum()
size_trend.plot(kind='bar', figsize=(6,5) , color='orange')
plt.xlabel('Size')
plt.grid()
plt.ylabel('Stocks')
plt.title('Sizes available')
plt.savefig('Sizes available', dpi=300)
plt.show()


#Sku code stock

SKU=df.groupby('SKU Code')['Stock'].sum()
SKU.sort_values(ascending=False).head(10).plot(kind='bar' , figsize=(6,5))
plt.xlabel('SKU Code')
plt.ylabel('Stocks')
plt.title('Top 10 SKU code available in inventory')
plt.savefig('Top 10 10 stocks by SKU code', dpi=300)
plt.show()

# Design

design_t=df.groupby('Design No.')['Stock'].sum()
design_t.sort_values(ascending=False).head(10).plot(kind='bar', figsize=(6,5))
plt.xlabel('Design')
plt.ylabel('Stocks')
plt.title('Top 10 least selling designs ')
plt.savefig('10 designed stocks', dpi=300)
plt.show()


#Category V Stock

#Selling category or Lowest

S_category=df.groupby('Category')['Stock'].sum().sort_values(ascending=False)
S_category.plot(kind='bar',figsize=(6,5),color='violet')
plt.xlabel('Category')
plt.ylabel('Stocks')
plt.title('Category available')
plt.savefig('Category V Stock', dpi=300)
plt.show()


import seaborn as sns

print(df.columns)

#box plot

plt.figure(figsize=(10,12))
sns.barplot(data=df, x='Color',y='Stock', estimator=np.sum)
plt.title("Stock distributaion by Color")
plt.xticks(rotation=60,ha='right')
plt.savefig('Stock distribution by color', dpi=300)
plt.show()


print(df.head())

#Countplot

sns.countplot(data=df, x='Color')
plt.title('Count of each Color')
plt.xticks(rotation=45, ha='right')
plt.savefig('Total Color Stocks', dpi=300)
plt.show()

p1_color = df.groupby(['Color', 'Category'])['Stock'].sum().unstack().fillna(0)
#Heatmap
plt.figure(figsize=(16, 10))
sns.heatmap(
    p1_color,
    cmap='viridis',
    linewidths=0.05,
    linecolor='grey'
)

plt.title("Stock Heatmap: Color vs Category", fontsize=16)
plt.xlabel("Category", fontsize=12)
plt.ylabel("Color", fontsize=12)

# Rotate category names for readability
plt.xticks(rotation=45, ha='right')

plt.tight_layout()
plt.savefig('05_heatmap_color_size.png',dpi=300)
plt.show()
