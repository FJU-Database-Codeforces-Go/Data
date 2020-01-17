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

for lines in jf:
    for problem in lines:
        i = random.randint(1, 5)
        for _ in (0, i + 10):
            j = random.randint(0, 77)
            print([problem[0], j])
            cursor.execute("""INSERT INTO codeforces_HasTag(problem_id_id, tag_id_id)
                            VALUES(%s, %s)
                        """, [problem[0], j])


db.commit()
cursor.close()
print("Done")