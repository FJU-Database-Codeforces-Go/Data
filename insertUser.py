import MySQLdb
import json

db = MySQLdb.connect(host='localhost',
    user='root',
    passwd='root',
    db='codeforces')
cursor = db.cursor()

with open('./Data/users.json', 'r') as reader:
    jf = json.loads(reader.read())

for line in jf:
    for user in line:
        cursor.execute("""INSERT INTO codeforces_user(user_name, user_rating)
                          VALUES(%s, %s)
                       """, user)

db.commit()
cursor.close()
print("Done")