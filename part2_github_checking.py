import pandas
import numpy
from decimal import Decimal


# web_dataset = pandas.read_csv("parsed_files/github_users_clear.csv")
# print(web_dataset)

# for i in web_dataset['repo_count']:
# 	i = Decimal('i').to_integral()
# web_dataset['member_since'] = web_dataset['member_since'].replace(" ", "") #replace the space to nothing in price

# print(web_dataset)
github_dataset = pandas.read_csv("github_parsed_files/github_dataset.csv",',', usecols=['login_id','repo_count','number_of_follower','starting_time'])
print(github_dataset)
github_dataset['starting_time'] = github_dataset['starting_time'].str.extract(r'(\d{4}-\d+-\d+)')
github_dataset = github_dataset.rename({'number_of_follower':'follower_count', 'starting_time':'member_since'}, axis=1)
# print(github_dataset)

# web_dataset.compare(github_dataset)


github_dataset.to_csv("github_parsed_files/part_github_dataset.csv",index=False)

# github_dataset = pandas.read_csv("github_parsed_files/part_github_dataset.csv")
# print(github_dataset)

# web_dataset = open("parsed_files/github_users_clear.csv","r",encoding='UTF-8')
# github_dataset = open("github_parsed_files/part_github_dataset.csv","r",encoding='UTF-8')
# lines1 = github_dataset.readlines()
# lines2 = web_dataset.readlines()
# print(web_dataset)
# print(github_dataset)

# for i,lines2 in enumerate(web_dataset):
#     if lines2 != lines1[i]:
#         print("line ", i, " in web_dataset is different \n")
#         print(lines2)
#     else:
#         print("same")





# with open('update.csv', 'w') as outFile:
#     for line in df_web:
#         if line not in df_github:
#             outFile.write(line)

  
# print(df_web['CoulumnsMatch'].describe())

# github_dataset_id = github_dataset['login_id']
# github_dataset_repo = github_dataset['repo_count']
# github_dataset_follower = github_dataset['number_of_follower']
# github_dataset_start = github_dataset['starting_time'].str.extract(r'(\d{4}-\d+-\d+)')

# for name in web_dataset_id:
# 	if name in github_dataset_id:
# 		web_dataset['IDexist'] = True
# 	else:
# 		web_dataset['IDexist'] = False
# print(web_dataset['IDexist'])
# # web_dataset['IDexist'] = numpy.where(web_dataset_id == github_dataset_id, 'True', 'False')
# new_web_dataset = web_dataset[web_dataset['IDexist'] == 'True']
# print(new_web_dataset.describe())
# 2_web_dataset_repo = 2_web_dataset['repo_count']
# 2_web_dataset_follower = 2_web_dataset['follower_count']
# 2_web_dataset_start = 2_web_dataset['member_since']

# 2_web_dataset['CoulumnsMatch'] = numpy.where(2_web_dataset_repo == github_dataset_repo & 2_web_dataset_follower == github_dataset_follower & 2_web_dataset_start == github_dataset_start, 'True', 'False')
	
# 	# price = price.replace(" ", "") #replace the space to nothing in price

# 2_web_dataset['repo_count'] = web_dataset['repo_count'][2_web_dataset['CoulumnsMatch'] == 'False']