import re
import requests
import json
import concurrent.futures
from bs4 import BeautifulSoup

def get_contest_submissions(contest):
    header={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36"}
    submissions = []
    this_page = []
    pre_page = []
    page = 1

    while 1:
        url = "https://codeforces.com/contest/" + str(contest) + "/status/page/" + str(page) + "?order=BY_JUDGED_DESC"
        print(url)
        r = requests.get(url,headers=header)
        soup = BeautifulSoup(r.text, 'html.parser')
        res = soup.select("div.datatable table td")
        this_page = []
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
                if attr[0:2] == "Ac":
                    submission.append("OK")
                elif attr[0:2] == "Co":
                    submission.append("COMPILATION_ERROR")
                elif attr[0:2] == "Wr":
                    submission.append("WRONG_ANSWER")
                elif attr[0:4] == "Runt":
                    submission.append("RUNTIME_ERROR")
                elif attr[0:2] == "Ti":
                    submission.append("TIME_LIMIT_EXCEEDED")
                elif attr[0:2] == "Me":
                    submission.append("MEMORY_LIMIT_EXCEEDED")
                else:
                    submission.append("OTHER")
            elif i % 8 == 6:
                attr = attr.replace("\xa0", "")
                submission.append(attr)
            elif i % 8 == 7:
                attr = attr.replace("\xa0", "")
                submission.append(attr)
                this_page.append(submission)
            i += 1
        if this_page == pre_page:
            break
        submissions.append(this_page)
        pre_page = this_page
        page += 1
    with open(str(contest) + '.json', 'w') as outfile:
        json.dump(submissions, outfile)

def get_contest():
    L, R = input().split()
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    # Start the load operations and mark each future with its URL
        future_to_url = {executor.submit(get_contest_submissions, contestID): contestID for contestID in range(int(L),int(R))}
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                data = future.result()
            except Exception as exc:
                print('%r generated an exception: %s' % (url, exc))
            else:
                print('%r page is %d bytes' % (url, len(data)))
    return

if __name__ == "__main__":
    get_contest()