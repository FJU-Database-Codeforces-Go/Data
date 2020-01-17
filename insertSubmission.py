import MySQLdb
import json

db = MySQLdb.connect(host='localhost',
    user='root',
    passwd='root',
    db='codeforces')
cursor = db.cursor()

with open('./submissions.json', 'r') as reader:
    jf = json.loads(reader.read())

submissionIdSet = set()

L = int(input('L:'))
R = int(input('R:'))

for i in range(L, R):
    submission = jf[i]
    if submission[0] == '':
        print(submission)
        continue
    if submission[0] in submissionIdSet:
        continue
    submissionIdSet.add(submission[0])
    cursor.execute("""INSERT INTO codeforces_submission(submission_id, language_name, verdict_name, time, memory)
                      VALUES(%s, %s, %s, %s, %s)
                   """, [submission[0], submission[3], submission[4], submission[5], submission[6]])


db.commit()
cursor.close()
print("Done")