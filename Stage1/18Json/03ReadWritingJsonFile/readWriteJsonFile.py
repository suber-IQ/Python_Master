# 👉  Reading and writing Json file

import json

# 🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠

# 👉 Reading

# file = open('posts.json','r')
# x = file.read()
# finaldata = json.loads(x)
# print(type(finaldata)) # 🎉 output:- <class 'list'>
# print(finaldata)

# for a in finaldata:
#       print(a['title'],a['id'])
#       print()


# 👉 new Method 

with open('posts.json','r') as file:
      data = json.load(file)

for n in data:
      print(n['id'])
      print(n['title'])

# 🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠

# 👉 Writing json file

# d = {
#       'name': 'sumit',
#        'class': 12,
#        'qulification': 'MBA'
# }

# with open("dummy.json","w") as file:
#       json.dump(d,file)

