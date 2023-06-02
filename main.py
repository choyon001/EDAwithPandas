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

# dataset.to_csv('Output.csv')

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
