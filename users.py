import re
import requests
from bs4 import BeautifulSoup


header={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36"}
url="https://codeforces.com/ratings/page/1"
print(url)
r= requests.get(url,headers=header)
soup = BeautifulSoup(r.text, 'html.parser')
res = soup.select("div.ratingsDatatable table td")
users = []
tmp = []
i = 0
for r1 in res:
    tmp2 = r1.text.replace("\r","").replace("\n","").replace(" ", "")
    if i % 4 == 1:
        tmp = []
        tmp.append(tmp2)
    elif i % 4 == 3:
        tmp.append(tmp2)
        users.append(tmp)
    i += 1
for user in users:
    print(user)
