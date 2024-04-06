# 👉 JSON (JavaScript Object Notation).
# 🎏 It is mainly used for storing and transferring data between the browser and the server.
# 🎏 JSON is text, written with JavaScript object notation.
# 🎏 Python too supports JSON with a built-in package called json.

# 🎏 Json supports mainly 6 data types:- string,number,boolean,null,object,array

import json

# 🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠

d = {
      'name':'Python',
      'fees':3800
}

f = json.dumps(d)

print(f)

