import re
import requests
from bs4 import BeautifulSoup


header={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36"}
contest = 1253
url="https://codeforces.com/problemset/page/1"
print(url)
r= requests.get(url,headers=header)
soup = BeautifulSoup(r.text, 'html.parser')
res = soup.select("div.datatable table td")
problems = []
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
        problems.append(problem)
    i += 1
for problem in problems:
    print(problem)