import pandas
from bs4 import BeautifulSoup

import os
import re
import glob

if not os.path.exists("parsed_files"):
    os.mkdir("parsed_files")


df = pandas.DataFrame()

for file_name in glob.glob("html_files/*.html"):

	f = open(file_name, "r")
	soup = BeautifulSoup(f.read(),"html.parser")
	f.close() 



	login_list = soup.find("div",{"class": "text-gray-700 text-sm"})
	login_row_box_list = login_list.find_all("div",{"class": "grid grid-cols-4 gap-4"})
	for login_row in login_row_box_list:
		# login_id = login_row.find("div",{"class": "userid"}).text if login_row.find("div",{"class": "userid"}) else None
		# print(login_id)
		middle_id = login_row.find("div",{"class": "userid"})
		# login_id = login_row.find("div",{"class": "userid"}).text if login_row.find("div",{"class": "userid"}) is not None
		if middle_id is not None:
			login_id = middle_id['ghid']
			# print(login_id)
			# login_id = middle_id.text
			login_id = login_id.replace(" ", "")
			# login_id = login_id.replace("\n", "")


		else:
			login_id = None	

		# print(login_id)
		middle_repo = login_row.find("div",{"class": "repocount"})
		if middle_repo is not None:
			repo_count = middle_repo.text
			# print(repo_count)
		else:
			repo_count = None


		middle_follower = login_row.find("div",{"class": "followercount"})
		if middle_follower is not None:
			follower_count = middle_follower.text
			follower_count = follower_count.replace("*  ", "")
			# print(follower_count)
		else:
			follower_count = None

		middle_member = login_row.find("div",{"class": "membersince"})
		if middle_member is not None:
			member_since = middle_member.text
			member_since = member_since.replace("( ", "")
			member_since = member_since.replace(" )", "")
		else:	
			member_since = None


		df = pandas.concat([df,  
		pandas.DataFrame.from_records([{
			"login_id": login_id,
			"repo_count": repo_count,
			"follower_count": follower_count,
			"member_since": member_since
			}])
	    ])

df.to_csv("parsed_files/github_users.csv",index=False)

print("done")
