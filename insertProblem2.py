import json
import MySQLdb
import random

db = MySQLdb.connect(host='localhost',
    user='root',
    passwd='root',
    db='codeforces')
cursor = db.cursor()

with open('./Data/problems.json', 'r') as reader:
    jf = json.loads(reader.read())

idSet = set()

# for line in jf:
#     for problem in line:
#         for tag in problem[2]:
#             idSet.add(problem[0])
            

for i in range(1, 3):
    for j in 'E':
        problemid = '324' + j + str(i)
        if problemid in idSet:
            continue
        print(problemid)
        rating = random.randint(10, 25) * 100
        cursor.execute("""INSERT INTO codeforces_problem(problem_id, problem_name, problem_rating)
                      VALUES(%s, %s, %s)
                   """, [problemid, problemid, rating])

# db.commit()
cursor.close()
print("Done")