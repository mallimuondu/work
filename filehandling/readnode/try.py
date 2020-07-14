import json
a = {"malli" : "2010"}
with open ('person.txt') as f:
    dater = json.load(f)
dater.uppdate(a)
with open('test.json') as f:
    json.dump(dater,f)