import json
f = open('swogi.json')
data = json.loads(f.read())
print data['id_to_card']