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
submissionIdSet.add(jf[40575][0])
submissionIdSet.add(jf[119117][0])

L = int(input('L:'))
R = int(input('R:'))

# print(jf[78712])

for i in range(L, R):
    # break
    submission = jf[i]
    print(i)
    # break
    # print([submission[0], submission[2]])
    if submission[1] == jf[40575][1] or submission[1] == jf[119117][1]:
        continue
    if submission[0] == '':
        print(submission)
        continue
    if submission[0] in submissionIdSet:
        continue
    submissionIdSet.add(submission[0])
    cursor.execute("""INSERT INTO codeforces_originfrom(submission_id_id, problem_id_id)
                      VALUES(%s, %s)
                   """, [submission[0], submission[2]])


db.commit()
cursor.close()
print("Done")