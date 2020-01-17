import json
import MySQLdb

db = MySQLdb.connect(host='localhost',
    user='root',
    passwd='root',
    db='codeforces')
cursor = db.cursor()

with open('./Data/problems.json', 'r') as reader:
    jf = json.loads(reader.read())

idSet = set()

for line in jf:
    for problem in line:
        for tag in problem[2]:
            if problem[0] in idSet:
                continue
            idSet.add(problem[0])
            print(problem[0])
            cursor.execute("""INSERT INTO codeforces_problem(problem_id, problem_name, problem_rating)
                      VALUES(%s, %s, %s)
                   """, [problem[0], problem[1], problem[3]])

db.commit()
cursor.close()
print("Done")