# 👉 sets :- unorder data type ,Unindex , set() | {}
# 👉 functions:- set(),add(),pop(),remove(),clear(),discard() and update()

# 🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠


# s = { 10,20,30,40}


# for a in s:
#       print(a)

# 🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠

# l = [ 10,20,10,30,40]

# s = set(l) # 🎉 output:- {40, 10, 20, 30}
# print(s)

# 🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠

# 👉  add()

# s = {10,20,30}
# s.add(40)
# print(s)  # 🎉 output:- {40, 10, 20, 30}

# 🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠

# 👉  pop()

# s = {10,20,30,40}
# s.pop()
# print(s)  # 🎉 output:- {10, 20, 30} ( with any element to delete)
# print(s.pop())

# 🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠

# 👉  remove()

# s = {10,20,30,40}
# s.remove(20)
# print(s)  # 🎉 output:- 20 is removed ( with value to delete)

# 🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠

# 👉  discard()

# s = {10,20,30,40}
# s.discard(20)
# print(s)  # 🎉 output:- {40, 10, 30}

# 🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠

# 👉  discard()

# s = {10,20,30,40}

# s.clear()  # 🎉 output:- set()
# print(s)

# 🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠

# 👉  update()

# s = {10,20,30,40}
# l = [30,50,60]

# s.update(l)
# print(s) #🎉 output:-{40, 10, 50, 20, 60, 30}