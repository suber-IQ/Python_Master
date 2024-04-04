# 👉 Data Types in Python

# 🎏  Data Type List:- 
#  1. Numeric :- Integers, Float, Complex Numbers
#  2. Sequence :- String, List, Tuple
#  3. Dictionary 
#  4. Set 

# 🎏  Mutable object can change its state or contents and immutable objects cannot

# 1. Mutable Data Types:-
  # ⏩ List, Dictionary, Byte array 

# 2. Immutable Data Types:-
  # ⏩ Int, Float, Complex, String , Tuple, set 



# 🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠


# 👉 1. Number

# a = 5
# print(a,type(a)) # 🎉 Output:-  5 (<class 'int'>)
# a = 5.5
# print(a,type(a)) # 🎉 Output:-  5.5 (<class 'float'>)
# a = 2 + 5j
# print(a,type(a)) # 🎉 Output:-  2 + 5j (<class 'complex'>)

# 🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠


# 👉 2. Sequence (String,List,Tuple)

  #  ⏩ String

# s = 'Hello@123'
# print(s,type(s)) # 🎉 Output:-  Hello@123 (<class 'str'>)
# s = "Sumitkumar"
# print(s,type(s)) # 🎉 Output:-  Sumitkumar (<class 'str'>)
# s = '''
#   Hello 
#   Sumit kumar Welcome to World

# '''
# print(s,type(s)) # 🎉 Output:- Hello Sumit kumar Welcome to World  (<class 'str'>)
# s = '10'
# print(s,type(s)) # 🎉 Output:-  10 (<class 'str'>)

  #  ⏩ List :- 💧List is an ordered sequence of items.
               #💧It is one of the most used data types in python and is very flexible.
               #💧[]


# l = [10, 'sk', 5.5]
# l[2] = 10; # updated with 10 (mutable data type)
# print(l,type(l))  #🎉  Output: [10, 'sk', 5.5] (<class 'list'>)


  #  ⏩ Tuple :- 💧Tuple is an ordered sequence of items same as a list.
               #💧It is defined within parentheses() where items are separated by commas.
               #💧define more than one value

# t = (10,20,'Hello')
# print(t,type(t)) # 🎉 Output:- (10,20,'Hello') (<class 'tuple'>)
# t = (10) 
# print(t,type(t)) # 🎉 Output:- 10 (<class 'int'>)


# 🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠


# 👉 3. Dictionary :- 💧Dictionary is an unordered collection of key-value pairs.
               #💧 In Python, dictionaries are defined within braces {} with each item being a pair in the form key:value.

# d = {
#       'course_name': "Python",
#       'course_duration': '3 Month'
# }
# print(d['course_name'],type(d['course_name'])) # 🎉 Output:- Python (<class 'str'>)
# print(d,type(d)) # 🎉 Output:- {'course_name': 'Python', 'course_duration': '3 Month'} (<class 'dict'>)

# 🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠


# 👉 4. Set :- 💧A Set is an unordered collection of items.
               #💧 Every set element is unique (no duplicates) and must be immutable (cannot be changed).
               #💧 {}

# s = {10,20,30,40,50,10}
# print(s,type(s)) # 🎉 Output:- {50,20,40,10,30} (<class 'set'>)
