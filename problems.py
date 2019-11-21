import re
import requests
import json
from bs4 import BeautifulSoup

header={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36"}
problems = []
this_page = []
pre_page = []
page = 1

while 1:
    url="https://codeforces.com/problemset/page/" + str(page)
    print(url)
    r= requests.get(url,headers=header)
    soup = BeautifulSoup(r.text, 'html.parser')
    res = soup.select("div.datatable table td")
    this_page = []
    problem = []
    i = 0
    for r in res:
        attr = r.text.replace("\r","").replace("\n","")
        if i % 5 == 1:
            attr = re.sub(r" {2,}", ",", attr).replace(",,", ",")
        else:
            attr = attr.replace(" ", "")
        if i % 5 == 0:
            problem = []
            problem.append(attr)
        elif i % 5 == 1:
            attr = [x.strip() for x in attr.split(',')]
            problem.append(attr[0])
            tag = []
            for j in (1, len(attr) - 1):
                tag.append(attr[j])
            problem.append(tag)
        elif i % 5 == 3:
            problem.append(attr)
            this_page.append(problem)
        i += 1
    if this_page == pre_page:
        break
    problems.append(this_page)
    pre_page = this_page
    page += 1
with open('Crawler/Data/problems.json', 'w') as outfile:
    json.dump(problems, outfile)