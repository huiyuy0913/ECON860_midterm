import pandas
import numpy
import statistics 

github_dataset = pandas.read_csv("github_parsed_files/github_dataset.csv")
print('----------')
print('the mean, standard deviation, median(50%), min, max and quantiles for repository counts, number of starred, number of followings and number of followers are')
print(github_dataset.describe())
print('----------')
print('minumum of starting time is', min(github_dataset['starting_time']))
print('maxumum of starting time is', max(github_dataset['starting_time']))
print('minumum of last updated time is', min(github_dataset['last_update_time']))
print('maxumum of last updated time is', max(github_dataset['last_update_time']))
print('----------')
print('modes of repo count, number of starred, number of following and number of follower are')
print(github_dataset.mode(numeric_only=True))

# print(statistics.mode(github_dataset['number_of_follower']))

