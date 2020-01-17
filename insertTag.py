import json
import MySQLdb

db = MySQLdb.connect(host='localhost',
    user='root',
    passwd='root',
    db='codeforces')
cursor = db.cursor()

with open('tags.json', 'r') as reader:
    tags = json.loads(reader.read())

i = 0
for tag in tags:
    cursor.execute("""INSERT INTO codeforces_tag(tag_id, tag_name)
                      VALUES(%s, %s)
                   """, [i, tag])
    i += 1

db.commit()
cursor.close()
print("Done")