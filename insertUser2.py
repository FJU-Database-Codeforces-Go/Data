import MySQLdb
import json
import random

db = MySQLdb.connect(host='localhost',
    user='root',
    passwd='root',
    db='codeforces')
cursor = db.cursor()

with open('./Data/users.json', 'r') as reader:
    jf = json.loads(reader.read())

userSet = []

for line in jf:
    for user in line:
        userSet.append(user[0])

with open('./submissions.json', 'r') as reader:
    jf2 = json.loads(reader.read())     

for i in range(0, 120000):
    submission = jf2[i]
    user = submission[1]
    if user in userSet:
        continue
    userSet.append(user)
    if i < 1200 or i == 40575 or i == 119117:
        continue
    print(i)
    rating = random.randint(1000, 2500)
    cursor.execute("""INSERT INTO codeforces_user(user_name, user_rating)
                          VALUES(%s, %s)
                       """, [user, rating])

db.commit()
cursor.close()
print("Done")