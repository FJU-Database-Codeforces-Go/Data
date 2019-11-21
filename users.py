import re
import requests
import json
from bs4 import BeautifulSoup

header={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36"}
users = []
this_page = []
pre_page = []
page = 1
while 1:
    url="https://codeforces.com/ratings/page/" + str(page)
    r = requests.get(url,headers=header)
    print(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    res = soup.select("div.ratingsDatatable table td")
    this_page = []
    tmp = []
    i = 0
    for r1 in res:
        tmp2 = r1.text.replace("\r","").replace("\n","").replace(" ", "")
        if i % 4 == 1:
            tmp = []
            tmp.append(tmp2)
        elif i % 4 == 3:
            tmp.append(tmp2)
            this_page.append(tmp)
        i += 1
    if this_page == pre_page:
        break
    users.append(this_page)
    pre_page = this_page
    page += 1
with open('Crawler/users.json', 'w') as outfile:
    json.dump(users, outfile)
