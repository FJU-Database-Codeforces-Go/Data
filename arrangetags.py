import json

with open('./Data/problems.json', 'r') as reader:
    jf = json.loads(reader.read())

tags = set()

for line in jf:
    for problem in line:
        for tag in problem[2]:
            tags.add(tag)

file = open('tags.json', 'w')
json.dump(list(tags), file)