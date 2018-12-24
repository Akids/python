import requests
from bs4 import BeautifulSoup
r = requests.get("https://hg.adblockplus.org/easylistchina/file/3b38de7a10f7/easylistchina.txt")
soup = BeautifulSoup(r.text,'lxml')
a = soup.find_all('span')
with open ("easylistchina.txt","a") as f:
	for i in range(14701):
		f.write(a[i].text + "\n")
