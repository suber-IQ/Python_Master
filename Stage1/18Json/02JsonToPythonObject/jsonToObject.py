# 👉 Convert Json Data to Python Object

import json

# 🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠

j = '{"cname":"Pythons","fees":4800,"duration": "2 months"}'

d = json.loads(j)
print(type(d)) # 🎉 output:- <class 'dict'>
print(d)