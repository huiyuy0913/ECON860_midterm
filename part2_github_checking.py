import pandas
import numpy

web_dataset = pandas.read_csv("parsed_files/github_users_clear.csv")
# print(web_dataset)


github_dataset = pandas.read_csv("github_parsed_files/github_dataset.csv",',', usecols=['login_id','repo_count','number_of_follower','starting_time'])
github_dataset['starting_time'] = github_dataset['starting_time'].str.extract(r'(\d{4}-\d+-\d+)')
github_dataset = github_dataset.rename({'number_of_follower':'follower_count', 'starting_time':'member_since'}, axis=1)
# print(github_dataset)
web_dataset['repo_count'] = (web_dataset['repo_count']).astype(int)
web_dataset['follower_count'] = (web_dataset['follower_count']).astype(int)


merge_data = github_dataset.merge(web_dataset, on=['login_id'], suffixes=['_github_dataset','_web_dataset'])


merge_data['repo_compare'] = numpy.where(merge_data['repo_count_web_dataset']==merge_data['repo_count_github_dataset'], 'yes', 'no')
merge_data['follower_compare'] = numpy.where(merge_data['follower_count_web_dataset']==merge_data['follower_count_github_dataset'], 'yes', 'no')

# print(merge_data.columns)
print(merge_data)
print('-----yes means the data in part1 is the same as the data in part2 while no means not')
print(merge_data.repo_compare.value_counts())
print(merge_data.follower_compare.value_counts())
print('-----users who have updated their repos')
print(merge_data['login_id'][(merge_data['repo_compare']=='no')])
print('-----users whose followers has changed')
print(merge_data['login_id'][(merge_data['follower_compare']=='no')])








