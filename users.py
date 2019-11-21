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
    print(url)
    r = requests.get(url,headers=header)
    soup = BeautifulSoup(r.text, 'html.parser')
    res = soup.select("div.ratingsDatatable table td")
    this_page = []
    user = []
    i = 0
    for r1 in res:
        attr = r1.text.replace("\r","").replace("\n","").replace(" ", "")
        if i % 4 == 1:
            user = []
            user.append(attr)
        elif i % 4 == 3:
            user.append(attr)
            this_page.append(user)
        i += 1
    if this_page == pre_page:
        break
    users.append(this_page)
    pre_page = this_page
    page += 1
with open('Crawler/Data/users.json', 'w') as outfile:
    json.dump(users, outfile)
