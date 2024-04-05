# 👉 Nested Dictionary:- Nesting Dictionary means putting a dictionary inside another dictionary.
# 👉 It's collection of dictionaries into one single dictionary.


# 🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠

#❓ Create a Nested Dictionary

course = {
      'php': { 'duration': '2 months','fees': '1500'},
      'python': { 'duration': '2 months','fees': '2800'},
      'java': { 'duration': '3 months','fees': '1800'},
}

# print(course) # 🎉 output:- {'php': {'duration': '2 months', 'fees': '1500'}, 'python': {'duration': '2 months', 'fees': '2800'}, 'java': {'duration': '3 months', 'fees': '1800'}}
# print(course['php']) # 🎉 output:- {'duration': '2 months', 'fees': '1500'}
# print(course['php']['fees']) # 🎉 output:- 1500

# for k,v in course.items():
#       print(k,v)

for k,v in course.items():
      print(k,v['duration'],v['fees'])


# course['java']['fees'] = 3500; # update
# print(course)