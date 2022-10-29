import pandas
import numpy

import matplotlib.pyplot as plt

dataset = pandas.read_csv("parsed_files/github_users.csv") 

print(dataset.describe())
print("----------remove None cells----------")
# print(dataset.isna().sum())
dataset = dataset.dropna()
# print(dataset.isna().sum())
# print(dataset.describe())
print("----------remove invalid IDs----------")
print(min(dataset['member_since']))
print(max(dataset['member_since']))
print(dataset.describe())
sub_dataset = dataset[(dataset['repo_count']>=0) & (dataset['follower_count']>=0) & (dataset['member_since'] != min(dataset['member_since']))]

print(sub_dataset.describe())
# print((sub_dataset['member_since'] == min(sub_dataset['member_since'])).sum())
# print(min(sub_dataset['member_since']))
# print(max(sub_dataset['member_since']))

print("----------remove duplicate IDs----------")
pandas.options.mode.chained_assignment = None 
sub_dataset['duplicate_id'] = sub_dataset.duplicated()
# print(sub_dataset)

rd_sub_dataset = sub_dataset[(sub_dataset['duplicate_id']==False)]
# print(rd_sub_dataset)
rd_sub_dataset = rd_sub_dataset.drop(columns=['duplicate_id'])
print(rd_sub_dataset)
rd_sub_dataset.to_csv("parsed_files/github_users_clear.csv",index=False)

print("done")

