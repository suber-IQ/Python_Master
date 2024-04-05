# 👉 Function & Method  Dictionary
# 🎏 Function & Method:- get(), keys(),values(),items(), del(),pop() ,dict(),update(),clear()

# 🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠

# d = {
#       'name' : 'Python',
#       'fees': 8000,
#       'duration': '2 months',
# }

# n = d.get('name')
# print(n) # 🎉 output:- Python

# 🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠

# d = {
#       'name' : 'Python',
#       'fees': 8000,
#       'duration': '2 months',
# }

# for a in d.keys(): # 🎉 output:- name,fees,duration
#       print(a)

# 🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠

# d = {
#       'name' : 'Python',
#       'fees': 8000,
#       'duration': '2 months',
# }

# for a in d.values(): # 🎉 output:- Python,8000,2 months
#       print(a)

# 🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠

# d = {
#       'name' : 'Python',
#       'fees': 8000,
#       'duration': '2 months',
# }

# for a,b in d.items(): # 🎉 output:- name Python,fees 8000,duration 2 months
#       print(a,b)

# 🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠

# d = {
#       'name' : 'Python',
#       'fees': 2000,
#       'duration': '2 months',
# }

# del d['fees'] # 🎉 output:- {'name': 'Python', 'duration': '2 months'}
# print(d) 

# a = d.pop('name')
# print(a) #🎉 output:- Python
# print(d) #🎉 output:- {'fees': 2000, 'duration': '2 months'}

# 🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠

# d = dict(name ='Python', duration ='2 months')

# print(d) #🎉 output:- {'name': 'Python', 'duration': '2 months'}

# 🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠

# d = {
#       'name' : 'Python',
#       'fees': 2000,
#       'duration': '2 months',
# }

# d.update({'fees' : 8000}) # 🎉 output:- {'name': 'Python', 'fees': 8000, 'duration': '2 months'}
# print(d)

# 🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠

# d = {
#       'name' : 'Python',
#       'fees': 2000,
#       'duration': '2 months',
# }

# d.clear()  #🎉 output:- {}
# print(d) 

# 🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠

# d = {
#       'name' : 'Python',
#       'fees': 2000,
#       'duration': '2 months',
# }

# d['desc']='This is Python' #🎉 output:- {'name': 'Python', 'fees': 2000, 'duration': '2 months', 'desc': 'This is Python'}
# print(d) 
# d['name']='django' #🎉 output:- {'name': 'django', 'fees': 2000, 'duration': '2 months', 'desc': 'This is Python'}
# print(d) 