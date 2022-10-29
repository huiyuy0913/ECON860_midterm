# ECON860 midterm

I divided my codes into three parts according to the midterm exam questions. 

## Part 1

### [part1_webpage_request.py](https://github.com/huiyuy0913/ECON860_midterm/blob/main/part1_webpage_request.py)

With this code above, I got the html file, named [github_user.html](https://github.com/huiyuy0913/ECON860_midterm/blob/main/html_files/github_users.html), from this [webpage](http://45.56.117.197/index.html) and saved it in the [html_files](https://github.com/huiyuy0913/ECON860_midterm/tree/main/html_files) repository.

### [part1_webpage_parse.py](https://github.com/huiyuy0913/ECON860_midterm/blob/main/part1_webpage_parse.py)

Then, using this code above, I started to parse the login names, number of repositories, number of followers, and the date they become a Github user from the html file I scraped.
I saved the information in [parsed_files](https://github.com/huiyuy0913/ECON860_midterm/tree/main/parsed_files), named [github_user.csv](https://github.com/huiyuy0913/ECON860_midterm/blob/main/parsed_files/github_users.csv). In the csv file, 

login_id: login names

repo_count: number of repositories

follower_count: number of followers

member_since: thee date they become a Github user

### [part1_webpage_checking.py](https://github.com/huiyuy0913/ECON860_midterm/blob/main/part1_webpage_checking.py)

In this code, I removed the None cells at first since the parsed code I used counted the column title (Login ID, Repo Count, Follower Count, Member Since)
in the website as the None cells. 

Then, after getting the summary statistics from the github_user.csv, I found there were some weird data, such as the negative number of repositories and number of followers,
 and the 0000-00-00 version of member since. So, I removed these data. The reason I can move them together is that I found there was 0000-00-00 for member since
  after I deleted the negative number of repositories and number of followers.
  
In the end, I found the duplicate login IDs and dropped them.

The cleared data were save in [parsed_files](https://github.com/huiyuy0913/ECON860_midterm/tree/main/parsed_files), named [github_user_clear.csv](https://github.com/huiyuy0913/ECON860_midterm/blob/main/parsed_files/github_users_clear.csv).

## Part 2

### [part2_github_request.py](https://github.com/huiyuy0913/ECON860_midterm/blob/main/part2_github_request.py)

With this code, I used the cleared login ID and Github API to scrape the Github users' websites. All the json files are saved in the [json_files](https://github.com/huiyuy0913/ECON860_midterm/tree/main/json_files) folder.

### [part2_github_request_starred.py](https://github.com/huiyuy0913/ECON860_midterm/blob/main/part2_github_request_starred.py)

I used the cleared login ID and the starred_url to scrape the data of their starred repositories in this code. All the json files are saved in the [json_files_starred](https://github.com/huiyuy0913/ECON860_midterm/tree/main/json_files_starred) folder.

### [part2_github_parse.py](https://github.com/huiyuy0913/ECON860_midterm/blob/main/part2_github_parse.py)

With this code, I obtained the login ID, avatar url, number of following, full name, company, blog, location, email, hireable, bio, starting time and last updated time
from the json files in the [json_files](https://github.com/huiyuy0913/ECON860_midterm/tree/main/json_files) folder. And, I calculated the number of starred by the data parsed from the [json_files_starred](https://github.com/huiyuy0913/ECON860_midterm/tree/main/json_files_starred) folder. 
("the number of starred" I obtained is not accurate since I didn't find a way to scrape multiple pages at the same time and the Github API can only provide
100 data in one page)

I saved all the information into [github_parsed_files](https://github.com/huiyuy0913/ECON860_midterm/tree/main/github_parsed_files), named [github_dataset.csv](https://github.com/huiyuy0913/ECON860_midterm/blob/main/github_parsed_files/github_dataset.csv).


### [part2_github_checking.py](https://github.com/huiyuy0913/ECON860_midterm/blob/main/part2_github_checking.py)

I compared the [github_users_clear.csv](https://github.com/huiyuy0913/ECON860_midterm/blob/main/parsed_files/github_users_clear.csv) obtained in part 1 with the [github_dataset.csv](https://github.com/huiyuy0913/ECON860_midterm/blob/main/github_parsed_files/github_dataset.csv) obtained in part 2. By merging these two files, I found there were several differences. 

First, there are 6 users don't exist. Their names have been printed in [part2_github_parse.py](https://github.com/huiyuy0913/ECON860_midterm/blob/main/part2_github_parse.py).

Second, some of them have updated their repositories. You can find who (and the numbers) have updated their repositories in the code.

Third, some users' followers have changed. You can find whose (and the numbers) followers have changed in the code.

### [part2_github_request_bonus.py](https://github.com/huiyuy0913/ECON860_midterm/blob/main/part2_github_request_bonus.py)

In this code, I scraped all the cleared login IDs' repository information by repos_url. All the json files were saved in the [json_files_bonus](https://github.com/huiyuy0913/ECON860_midterm/tree/main/json_files_bonus) folder.
(I still didn't scrape all the pages this time, and I didn't change the number of repositories one page can show. So, it only has 30 repositories information 
per page by default.)

### [part2_github_parse_bonus.py](https://github.com/huiyuy0913/ECON860_midterm/blob/main/part2_github_parse_bonus.py)

With this code, I calculated the total starred times of the user's first 30 repos by "stargazers count" (if that user doesn't have 30 repos, then I calculate
 total starred times of the user's all repos). The data were saved as [github_bonus_dataset.csv](https://github.com/huiyuy0913/ECON860_midterm/blob/main/github_bonus_parsed_files/github_bonus_dataset.csv) in [github_bonus_parsed_files](https://github.com/huiyuy0913/ECON860_midterm/tree/main/github_bonus_parsed_files) folder.

## Part 3

### [part3_summary.py](https://github.com/huiyuy0913/ECON860_midterm/blob/main/part3_summary.py)

I used the [github_dataset.csv](https://github.com/huiyuy0913/ECON860_midterm/blob/main/github_parsed_files/github_dataset.csv) to get the summary statistics. First, I calculated the mean, standard deviation, median(50%), min, max and quantiles for repository counts,
number of starred, number of followings and number of followers.

Then, I got the maximum and minimum of the starting time and last updated time.

Finally, I got the modes of repository counts, number of starred, number of followings and number of followers.

Since I have deleted the user IDs with weird information (the negative number of repositories and number of followers,
 and the 0000-00-00 version of member since) in part 1, I did't find any unreasonable information here.

### [part3_scatterplots.py](https://github.com/huiyuy0913/ECON860_midterm/blob/main/part3_scatterplots.py)

I drew ten pictures here with the data from [github_dataset.csv](https://github.com/huiyuy0913/ECON860_midterm/blob/main/github_parsed_files/github_dataset.csv).

For [figure1](https://github.com/huiyuy0913/ECON860_midterm/blob/main/figure1.png), I plotted the length of ID with the length of full name. It seems the longer your full name is, the shorter your ID would be. 
Since the mean of the length of full name conditional on the the length of ID is decreasing with the length of ID. It is reasonable since people 
with longer full name may know that longer name is harder for people to remember in the reality. 

[Figure2](https://github.com/huiyuy0913/ECON860_midterm/blob/main/figure2.png) suggests that the users with more followers tend to have the blog information on Github. It also makes sense because people with more followers
 probably would like to attract their followers to follow their other accounts as well.

[Figure3](https://github.com/huiyuy0913/ECON860_midterm/blob/main/figure3.png) suggests that the users with more followers tend to have the bio information on Github. It's probably because bio can increase the credibility
of the context they write which will attract more followers.

[Figure4](https://github.com/huiyuy0913/ECON860_midterm/blob/main/figure4.png) suggests the relationship between starting time and the number of repositories. It seems no matter when you start your Github account, 
most of users will end up with four public repositories. In other words, after creating four public repositories, most users may feel boring and stop 
updating the account. 

[Figure5](https://github.com/huiyuy0913/ECON860_midterm/blob/main/figure5.png) suggests the the longer the ID you have, the less followers you will attract. Since the mean of the number of followers conditional on 
the the length of ID is decreasing with the length of ID. It is reasonable since longer ID is hard for people to remember.

[Figure6](https://github.com/huiyuy0913/ECON860_midterm/blob/main/figure6.png) shows the relationship between the number of repositories and the number of followers, and the size of the point reflects the number of 
followings. This figure suggests there is a positive correlation between the number of repositories and the number of followers. It makes sense since 
people with more followers would like to update the account frequently. The possibility that accounts with more repositories have higher quality 
context would be higher, which leads to more followers. 

Conditional on the repository counts, the more followers, the more followings. It also makes sense because when the attraction to people is fixed 
(repo count can be such proxy although it's not accurate), the more accounts you follow, the more likely they will follow back and then increase your
followers.

[Figure7](https://github.com/huiyuy0913/ECON860_midterm/blob/main/figure7.png) suggests the relationship between the number of followings and the number of followers, and the size of the point represents the length of ID.
This figure verifies the prediction in figure 6 which is the number of following is positively correlated with the number of followers. The more people 
you follow, the more likely they will follow back and then increase your followers. The length of ID doesn't seem to have any effects here.

[Figure8](https://github.com/huiyuy0913/ECON860_midterm/blob/main/figure8.png) shows the relationship between the number of repositories and the number of followings, and the color reflects the number of 
followers. The numer of repositories is positively correlated with the number of followings, since people who follow more users are more eager to learn 
something from the Github, then they would like to update frequently as well. I also found that the color becomes lighter when the increase of the number 
of followings which verifies the positive correlation between followers and followings again.

For the rest of graphs, I changed the dataset. I only consider the users who have more followers than followings, trying to avoid the "follow back" effect
 and find if the number of repositories can increase the followers.
 
[Figure9](https://github.com/huiyuy0913/ECON860_midterm/blob/main/figure9.png) suggests the relationship between the length of ID and the number of followers. Same for [Figure5](https://github.com/huiyuy0913/ECON860_midterm/blob/main/figure5.png), it shows there is a negative correlation
 between them and such effect is more obvious here.
 
[Figure10](https://github.com/huiyuy0913/ECON860_midterm/blob/main/figure10.png), same as [Figure6](https://github.com/huiyuy0913/ECON860_midterm/blob/main/figure6.png), shows the relationship between the number of repositories and the number of follower. It also suggests a positive
correlation between them and this correlation is more obviuos here. The color represents the lenth of ID which still doesn't have any specific meanings.

[Figure11](https://github.com/huiyuy0913/ECON860_midterm/blob/main/figure11.png), same as [Figure8](https://github.com/huiyuy0913/ECON860_midterm/blob/main/figure8.png), shows the relationship between the number of repositories and the number of followings. It suggests a positive
correlation between them as well and this correlation is more obviuos here. The color represents the lenth of ID which still doesn't 
have any specific meanings.
