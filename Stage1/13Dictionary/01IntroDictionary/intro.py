# 👉 Dictionary in Python
# 🎏 unorder data types, key value pairs and {}

# 🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠

d = {
      'name': 'Python',
      'fees': 8000,
      'duration': '2 months'
}

# print(type(d)) # 🎉 output:- <class 'dict'>
# print(d['name']) # 🎉 output:- Python
# print(d['fees']) # 🎉 output:- 8000
# d['fees'] = 5000;
# print(d['fees'])  # 🎉 output:- 5000

for n in d:
      print(n,": ",d[n])