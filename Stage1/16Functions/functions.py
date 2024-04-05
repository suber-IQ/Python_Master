# 👉 Functions in Python
# 🎏 Inbuild Function and User defined functions

# 🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠

# 👉 User Define Function :- simple function, function argument and return type

# def simpleFunc():
#       print("Welcome to SuberIQ")

# simpleFunc() # 🎉 output:- Welcome to SuberIQ

# 🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠

# def sumData(a,b):
#       print(a + b)

# n = 10
# n2 = 20
# sumData(n,n2) # 🎉 output:- 30

# m1 = 10
# m2 = 50
# sumData(m1,m2) # 🎉 output:- 60

# 🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠

# def sumData(a,b = 10):
#       print(a + b)

# sumData(5) # 🎉 output:- 15
# sumData(5,5) # 🎉 output:- 10


# 🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠

def sumData(a,b = 10):
      c = a + b
      return c

result = sumData(20,30)
print(result)