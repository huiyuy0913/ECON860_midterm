import pandas
import numpy
import glob
import matplotlib.pyplot as plt

github_dataset = pandas.read_csv("github_parsed_files/github_dataset.csv")

sub_github_dataset = github_dataset
login_id = sub_github_dataset['login_id']
repo_count = sub_github_dataset['repo_count']
number_of_follower = sub_github_dataset['number_of_follower']
number_of_following = sub_github_dataset['number_of_following']
starting_time = sub_github_dataset['starting_time'].str.extract(r'(\d{4}-\d+-\d+)')
last_update_time = sub_github_dataset['last_update_time'].str.extract(r'(\d{4}-\d+-\d+)')
full_full_name = sub_github_dataset['full_name']

group = ['full_name', 'company', 'blog', 'location', 'email', 'hireable', 'bio']
# print(group)
for i in group:
	sub_github_dataset[i] = sub_github_dataset[i].fillna("")
	sub_github_dataset[i] = (sub_github_dataset[i] != '')*1

full_name = sub_github_dataset['full_name']
company = sub_github_dataset['company']
blog = sub_github_dataset['blog']
location = sub_github_dataset['location']
email = sub_github_dataset['email']
hireable = sub_github_dataset['hireable']
bio = sub_github_dataset['bio']

sub_github_dataset['total'] = ((sub_github_dataset['full_name'] == 1 )& (sub_github_dataset['company'] == 1)& (sub_github_dataset['blog'] == 1) & (sub_github_dataset['location'] == 1) & (sub_github_dataset['email'] == 1) & (sub_github_dataset['hireable'] == 1) & (sub_github_dataset['bio'] == 1))*1
total = sub_github_dataset['total']
# print((total == 0).sum())

logrepo = numpy.log(repo_count+1)
logfollower = numpy.log(number_of_follower+1)
logfollowing = numpy.log(number_of_following+1)

len_id = []	
for i in login_id:
	len_id.append(len(i)) 
sub_github_dataset['len_id'] = len_id
len_id = sub_github_dataset['len_id']

len_full_name = []
for i in full_full_name:
	len_full_name.append(len(str(i)))
sub_github_dataset['len_full_name'] = len_full_name
len_full_name = sub_github_dataset['len_full_name']



plt.figure()
plt.scatter(len_id , len_full_name, s=1, c='blue')
plt.title("Length of ID and Length of Full Name")
plt.xlabel("Length of ID")
plt.ylabel("Length of Full Name")
plt.savefig('figure1.png')


plt.figure()
plt.scatter(logfollower, blog, s=1.5)
plt.title("Number of Followers and Blog")
plt.xlabel("Number of Followers")
plt.ylabel("Blog")
plt.savefig('figure2.png')

plt.figure()
plt.scatter(logfollower, bio, s=1.5)
plt.title("Number of Followers and Bio")
plt.xlabel("Number of Followers")
plt.ylabel("Bio")
plt.savefig('figure3.png')


plt.figure()
plt.scatter(starting_time[0] ,logrepo)
plt.title("Starting Time and Repos")
plt.xlabel("Starting Time")
plt.ylabel("Repo Count")
plt.savefig('figure4.png')


plt.figure()
plt.scatter(len_id ,logfollower, s=2)
plt.title("Length of ID and # Follower")
plt.xlabel("Length of ID")
plt.ylabel("Number of Followers")
plt.savefig('figure5.png')



plt.figure()
plt.scatter(logrepo, logfollower, s = logfollowing, c='blue')
plt.title("Repos and Number of Followers with # Following")
plt.xlabel("Repo Count")
plt.ylabel("Number of Followers")
plt.savefig('figure6.png')



plt.figure()
plt.scatter(logfollowing, logfollower, s = len_id, c='blue')
plt.title("# Following and # Followers with Length of ID")
plt.xlabel("Number of Following")
plt.ylabel("Number of Followers")
cb = plt.colorbar()
cb.remove()
plt.savefig('figure7.png')



plt.figure()
plt.scatter(logrepo ,logfollowing, c=logfollower)
plt.title("Repos and Number of Following with # Followers")
plt.xlabel("Repo Count")
plt.ylabel("Number of Following")
plt.colorbar()
plt.savefig('figure8.png')

sub_github_dataset = github_dataset[(github_dataset['number_of_following']<github_dataset['number_of_follower'])]
repo_count = sub_github_dataset['repo_count']
number_of_follower = sub_github_dataset['number_of_follower']
number_of_following = sub_github_dataset['number_of_following']
login_id = sub_github_dataset['login_id']
len_id_new = []	
for i in login_id:
	len_id_new.append(len(i)) 

logrepo = numpy.log(repo_count+1)
logfollower = numpy.log(number_of_follower+1)
logfollowing = numpy.log(number_of_following+1)

plt.figure()
plt.scatter(len_id_new ,logfollower, s=2)
plt.title("Length of ID and # Follower")
plt.xlabel("Length of ID")
plt.ylabel("Number of Followers")
plt.savefig('figure9.png')

plt.figure()
plt.scatter(logrepo ,logfollower, c=len_id_new)
plt.title("Repos and # Follower with Length of ID")
plt.xlabel("Repo Count")
plt.ylabel("Number of Followers")
plt.colorbar()
plt.savefig('figure10.png')

plt.figure()
plt.scatter(logrepo ,logfollowing, c=len_id_new)
plt.title("Repos and # Following with Length of ID")
plt.xlabel("Repo Count")
plt.ylabel("Number of Followings")
plt.colorbar()
plt.savefig('figure11.png')




