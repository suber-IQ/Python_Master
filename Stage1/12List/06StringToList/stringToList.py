# 👉 Python program to convert String to a list

# 🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠

# n= input("Enter the Value:- ")
# print(n)

# l = n.split();
# print(l) # 🎉 output:- ['welcome', 'to', 'Home']

# 🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠

l = []
for a in range(1,4):
      n = input("Enter the Value" + str(a) + ":- ")
      l.append(n)

print(l)

# 🎉 example with Output:- Enter the Value1:- Red
                          # Enter the Value2:- Green
                          # Enter the Value3:- Yellow
                          # ['Red', 'Green', 'Yellow'] 