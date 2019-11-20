import re
import requests
from bs4 import BeautifulSoup


header={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36"}
contest = 1253
url="https://codeforces.com/contest/" + str(contest) + "/status/page/1?order=BY_JUDGED_DESC"
print(url)
r= requests.get(url,headers=header)
soup = BeautifulSoup(r.text, 'html.parser')
res = soup.select("div.datatable table td")
submissions = []
submission = []
i = 0
for r in res:
    attr = r.text.replace("\r","").replace("\n","")
    attr = re.sub(r" {2,}", ",", attr).replace(",", "")
    if i % 8 == 0:
        submission = []
        submission.append(attr)
    elif i % 8 == 2:
        attr = attr.replace(" ", "")
        submission.append(attr)
    elif i % 8 == 3:
        attr = [x.strip() for x in attr.split('-')]
        submission.append(str(contest) + attr[0])
    elif i % 8 == 4:
        submission.append(attr)
    elif i % 8 == 5:
        if attr[0:2] == "Wr":
            submission.append("Wrong answer")
        elif attr[0:2] == "Ru":
            submission.append("Runtime error")
        elif attr[0:2] == "Ti":
            submission.append("Time limit exceeded")
        elif attr[0:2] == "Me":
            submission.append("Memory limit exceeded")
        else:
            submission.append(attr)
    elif i % 8 == 6:
        attr = attr.replace("\xa0", "")
        submission.append(attr)
    elif i % 8 == 7:
        attr = attr.replace("\xa0", "")
        submission.append(attr)
        submissions.append(submission)
    i += 1
for submission in submissions:
    print(submission)
