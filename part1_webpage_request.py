import requests  # you can also use requests to do it
import os


if not os.path.exists("html_files"):
    os.mkdir("html_files")

headers = {
 	'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
 	'accept-encoding': 'gzip, deflate',
    'accept-language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'cookie': '_myapp_session=Iua%2Bp34xABAsw5dl8BEDm3uUje26obkiI1xiM6cUmDLSr8ABlAO2DM5ls5k6NdfR%2FGfCV2QLZ5WOXiE3xvxVlgFCF4Jb27Kn0i%2F03Qal0xIPbrk9cwIpvgXBqDkNs8lV2IP7g2SXo%2FMo9rmCNqlWmL15TZLxeDCp03hcC6i7%2BEPmogSLVHr1tcig%2FyYGq%2B732DQv5gEm8nUa9a9NEMd9hkGz4QFMg6g0o%2B8KKiwcBNmlAsdITnIFd%2FIxoEJhIlgATm0BFsd1OWn4y7OeESrE762jgozF2A%3D%3D--awLkUsiUzc5Z0YID--TUyg%2B3kwVFWq4JvHep9IRw%3D%3D',
    'Host': '45.56.117.197',
    'If-None-Match': 'W/"47ad481f62f229903c1ada8decf02fa6"',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
	
}


f = open("html_files/github_users.html","w")
# r = requests.Session()
response = requests.get("http://charcoalpaper.com", headers = headers)

html = response.text
# html = response
# print(response)
f.write(html)
f.close()

print("done")




