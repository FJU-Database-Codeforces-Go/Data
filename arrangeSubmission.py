import json
import os

problemList = []

for i in range(1, 1255):
    route = './Data/submissions/' + str(i) + '.json'
    if os.path.isfile(route) == False:
        continue

    with open(route, 'r') as reader:
        jf = json.loads(reader.read())
    line_number = 0
    for line in jf:
        for problem in line:
            problemList.append(problem)
        line_number += 1
        if line_number == 8:
            break
    print("Done:" + route)

file = open('submissions.json', 'w')
json.dump(list(problemList), file)
