import json
data={'name':'Misha','age':22}
with open('module2/lection1/file.json', 'w') as f:
     f.write(json.dumps(data))