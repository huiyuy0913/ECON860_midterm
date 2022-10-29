import json
import pandas
import glob
import os
import re

if not os.path.exists("github_bonus_parsed_files"):
    os.mkdir("github_bonus_parsed_files")

df = pandas.DataFrame()

for json_file_name in glob.glob("json_files_bonus/*.json"):
	base_name = os.path.basename(json_file_name) 
	name = re.findall('github_bonus_(.*).....', base_name)[0]

	f = open(json_file_name,"r")
	json_data = json.load(f)
	f.close()

	try:
		total_stargazers_count = 0

		stargazers_count = ";".join([str(item['stargazers_count']) for item in json_data])
		# print(repo_id)
		all_stargazers_count = stargazers_count.split(';')
		# print(all_repo_id)
		# print(len(all_repo_id))
		for element in range(0, len(all_stargazers_count)):
			total_stargazers_count = total_stargazers_count + int(all_stargazers_count[element])
	except Exception as e:
		total_stargazers_count = 0
		print('this user does not have any repository')
		print(name)
		# print(e)

	df = pandas.concat([df,

	  pandas.DataFrame.from_records([{
		'login_id': name,
		'total_stargazers_count': total_stargazers_count

		}])
	  ])

print(df)
df.to_csv("github_bonus_parsed_files/github_bonus_dataset.csv",index=False)

print("done")
