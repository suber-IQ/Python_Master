# 👉 List Function in Python
# 🎏 Function for Delete Element from List :- del ,pop(),remove(),clear() 
# 🎏 Function for Update Element from List :- insert(),append(),extends() 
# 🎏 Function :- count,Max,Min,Sort,Reverse, & Index 


# 🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠

# 👉 del : work on index

# l = [20,30,40,50,60]
# del l[1] # 🎉 output:- [20, 40, 50, 60] (30 is deleted)
# print(l)

# 🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠

# 👉 pop() : work on index

# l = [20,30,40,50,60]
 # l.pop(3) # 🎉 output:- [20, 30, 40, 60] (50 is deleted)
# k = l.pop(3) # 🎉 output:- 50 deleted (50 will return)
# print(k)
# print(l)

# 🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠

# 👉 remove() : work on value

# l = [20,30,40,50,60]

# l.remove(40)  # 🎉 output:- [20, 30, 50, 60] (40 is deleted)
# print(l)  



# 🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠

# 👉 clear() : all list is blank(all element delete)


# l = [20,30,40,50,60]

# l.clear()  # 🎉 output:- [] (all element deleted)
# print(l)  

# 🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠

# 👉 Update Element from List:-

# l = [20,30,40,50,60]
# l[3]=80
# print(l)  # 🎉 output:- [20,30,40,80,60] 
# print(type(l))



# 🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠

# 👉 Update Element from List:- insert()

# l = [20,30,40,50,60]

# l.insert(0,10)  # 🎉 output:- [10, 20, 30, 40, 50, 60]
# print(l)

# 🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠

# 👉 Update Element from List:- append() (on last position)

# l = [20,30,40,50,60]
# n = [50,60]
# l.append(n)  # 🎉 output:- [20, 30, 40, 50, 60, [50, 60]]
# l.append(70)  # 🎉 output:- [10, 20, 30, 40, 50, 60,70]
# print(l)
# 🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠

# 👉 Update Element from List:- extend() (on last position)

# l = [20,30,40,50,60]
# n = [50,60]
# l.extend(n)  # 🎉 output:- [20, 30, 40, 50, 60, 50, 60]
# print(l)

# 🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠

# 👉 Count

# l = [10,20,10,30,50,10];

# a = l.count(10) # 🎉 output:- 3
# print(a)

# 🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠

# 👉 Max

# l = [10,20,10,30,50];

# m = max(l) # 🎉 output:- 50
# print(m)

# n = ["hello","world"]

# k = max(n) # 🎉 output:- world
# print(k)

# 🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠

# 👉 Min

# l = [10,20,10,30,50];

# m = min(l) # 🎉 output:- 10
# print(m)


# n = ["hello","world"]

# k = min(n) # 🎉 output:- hello
# print(k)

# 🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠

# 👉 sort

# l = [10,20,10,30,50];

# l.sort() # 🎉 output:- [10, 10, 20, 30, 50]
# print(l)

# 🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠

# 👉 reverse

# l = [10,20,10,30,50];

# l.reverse() # 🎉 output:- [50, 30, 10, 20, 10]
# print(l)

# 🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠

# 👉 index : (not found element then give error)

# l = [10,20,10,30,50];

# k = l.index(30) # 🎉 output:- 3
# print(k)


