import json
import pandas
import glob
import os
import re

if not os.path.exists("github_parsed_files"):
    os.mkdir("github_parsed_files")


df = pandas.DataFrame()



for json_file_name in glob.glob("json_files/*.json"):

	f = open(json_file_name,"r")
	json_data = json.load(f)
	f.close()

	base_name = os.path.basename(json_file_name) 
	name = re.findall('github_(.*).....', base_name)[0]
	try:
		login_id = json_data['login']
		repo_count = json_data['public_repos']
		avatar_url = json_data['avatar_url']
		url = json_data['url']
		number_of_following = json_data['following']
		number_of_follower = json_data['followers']
		full_name = json_data['name']
		company = json_data['company']
		blog = json_data['blog']
		location = json_data['location']
		email = json_data['email']
		hireable = json_data['hireable']
		bio = json_data['bio']
		starting_time = json_data['created_at']
		last_update_time = json_data['updated_at']
	except Exception as e:
		login_id = None
		repo_count = None
		avatar_url = None
		url = None
		number_of_following = None
		number_of_follower = None
		full_name = None
		company = None
		blog = None
		location = None
		email = None
		hireable = None
		bio = None
		starting_time = None
		last_update_time = None
		print(name,'does not exist')
		print(e)


	df = pandas.concat([df,

	  pandas.DataFrame.from_records([{
		'login_id': login_id,
		'repo_count': repo_count,
		'avatar_url': avatar_url,
		'url': url,
		'number_of_following': number_of_following,
		'number_of_follower' : number_of_follower,
		# 'number_of_starred': number_of_starred,
		'full_name': full_name,
		'company': company,
		'blog': blog,
		'location': location,
		'email': email,
		'hireable': hireable,		
		'bio': bio,
		'starting_time': starting_time,
		'last_update_time': last_update_time

		}])
	  ])

df2 = pandas.DataFrame()

for json_file_name_starred in glob.glob("json_files_starred/*.json"):
	base_name_starred = os.path.basename(json_file_name_starred) #only print the filename without path
	name_starred = re.findall('github_starred_(.*).....', base_name_starred)[0]

	f_starred = open(json_file_name_starred,"r")
	json_data_starred = json.load(f_starred)
	f_starred.close()

	try:
		repo_id = ";".join([str(item['id']) for item in json_data_starred])
		# print(repo_id)
		all_repo_id = repo_id.split(';')
		# print(all_repo_id)
		# print(len(all_repo_id))
		number_of_starred = str(len(all_repo_id))
		# print(number_of_starred)
		# print ('everything: ', json_data)
	except Exception as e:
		number_of_starred = 0
		print(name_starred)
		print(e)

	df2 = pandas.concat([df2,

	  pandas.DataFrame.from_records([{
		'login_id': name_starred,
		'number_of_starred': number_of_starred

		}])
	  ])
print(df)
print(df.describe())
print(df.isna().sum())

df = pandas.merge(df,df2,on='login_id')
print(df)
print(df.describe())
print(df.isna().sum())
print(df2.describe())
print(df2.isna().sum())

df = df.dropna(how='all')
print(df.isna().sum())


df.to_csv("github_parsed_files/github_dataset.csv",index=False)

print("done")