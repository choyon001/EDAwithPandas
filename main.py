import  pandas as pd
import os
current_dir = os.getcwd()
files = os.listdir(current_dir)
# creating empty DataFrame
dataset = pd.DataFrame()
for file in files:
    if 'Sales' in file:
        newdataset = pd.read_csv(f"{current_dir}/{file}")
        dataset = pd.concat([dataset,newdataset])
# print(dataset.shape)

# make a new csv file

dataset.to_csv('Output.csv',index=False)

# open the new csv dataset
dataset = pd.read_csv('Output.csv')

# deleting all the nan values from the dataset

dataset = dataset[dataset['Order Date'].str[:2] !='Or']
dataset.dropna(how='all',inplace =True)

#creating a new col named Month
dataset['Month'] = dataset['Order Date'].str[:2]

# creating a new col named Sales
dataset['Quantity Ordered'] = pd.to_numeric(dataset['Quantity Ordered'])
dataset['Price Each'] = pd.to_numeric(dataset['Price Each'])
dataset['Sales']=dataset['Quantity Ordered'] * dataset['Price Each']
# print(dataset.isnull().sum())

# finding out the first question
# Find out which month is best for sales

best_month = dataset.groupby('Month')['Sales'].sum().sort_values(ascending=False).index[0]
print('Best Month For Selling Product:',best_month)

# creating a new column named City which is basically splitted from another column

dataset['City'] = dataset['Purchase Address'].str.split(',').str[1]

# find out which city sold most product
best_city = dataset.groupby('City')['Sales'].sum().sort_values(ascending=False).index[0]
print('Best City For Selling Product:',best_city)

# which time is best for selling?
# creating a new column named Time
dataset['Time']=dataset['Order Date'].str[-5:-3]
# found the best time for selling product
best_time = dataset.groupby('Time')['Sales'].sum().sort_values(ascending=False).index[0]
print('Best Time For Selling Product:',best_time)
