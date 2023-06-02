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

dataset.to_csv('Output.csv')
