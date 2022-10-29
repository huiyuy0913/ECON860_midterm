import json
import os
import time
import pandas

import requests
import json

if not os.path.exists("json_files_starred"):
  os.mkdir("json_files_starred")


f = open("github_token","r")
github_token = f.read()
f.close()

github_session = requests.Session()
github_session.auth = ( "huiyuy0913", github_token)



github_users_clear = pandas.read_csv("parsed_files/github_users_clear.csv")

for index,row  in github_users_clear.iterrows():
    login_id = row["login_id"]
    # print(login_id)

    file_name = "json_files_starred/github_starred_" + login_id
    if os.path.exists(file_name + ".json"):
        print("file exists", login_id) 
    else:
        try:
            print("downloading:", login_id)
            response_text = github_session.get("https://api.github.com/users/" + login_id + "/starred").text
            json_text = json.loads(response_text)
            print(json_text)


            f = open(file_name + ".tmp", "w")
            f.write(json.dumps(json_text))
            f.close()

            # time.sleep(1)
            os.rename(file_name + ".tmp", file_name + ".json")
        except Exception as e:
            print(e)

        print("waiting 1 seconds")
        time.sleep(1)
